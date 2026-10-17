"""Checks of model/moise.yaml against docs/paper and for internal consistency.

These tests do not check that the model is economically right (that is test_replication.py and the
human verification in docs/verification-log.md). They check that the YAML is a faithful, complete
transcription: every Appendix D equation is there with its printed code form, every departure from
the print is tied to a documented decision, and every number comes from the paper's tables.
"""
import csv
import json
from pathlib import Path

import numpy as np
import pytest
import yaml

import moise
from moise import ModelError

ROOT = Path(__file__).resolve().parents[1]
SPEC = yaml.safe_load((ROOT / "model" / "moise.yaml").read_text(encoding="utf-8"))
PAPER_EQS = [b for b in json.loads((ROOT / "docs/paper/equations.json").read_text(encoding="utf-8"))
             if b["file"] == "10-log-linear-model.md" and b["kind"] == "eq"]
EQ = {e["id"]: e for e in SPEC["equations"]}
DEC = {d["id"]: d for d in SPEC["decisions"]}
DATA = ROOT / "docs" / "paper" / "data"


@pytest.fixture(scope="module")
def model():
    return moise.load()


# ----------------------------------------------------------------------------- completeness
def test_every_appendix_d_equation_is_present_once():
    ids = [e["id"] for e in SPEC["equations"]]
    assert len(ids) == len(set(ids)), "duplicate equation ids"
    paper_ids = [b["id"] for b in PAPER_EQS]
    assert paper_ids == [str(n) for n in range(212, 332)]
    missing = [i for i in paper_ids if i not in EQ]
    assert not missing, f"Appendix D equations missing from moise.yaml: {missing}"


def test_printed_is_the_docs_paper_code_form():
    for b in PAPER_EQS:
        e = EQ[b["id"]]
        assert e["printed"] == b["code"], f"({b['id']}): printed differs from docs/paper"
        assert e["paper_eq"] == f"({b['id']})"
        assert e["page"] == int(b["page"])
        assert e["section"] == b["section"]


def test_every_change_is_covered_by_a_decision():
    for e in SPEC["equations"]:
        if e["printed"] is None:
            # added equation (not printed in Appendix D) or a printed ellipsis expanded under a decision
            assert e["section"] == "added" or e.get("decision") in DEC, e["id"]
            assert e.get("notes"), f"{e['id']}: explain where the equation comes from"
        elif e["expr"] != e["printed"]:
            assert e.get("decision") in DEC, f"({e['id']}) differs from the print without a decision"
        for alt in (e.get("alternatives") or {}):
            assert alt in DEC[e["decision"]]["alternatives"], f"({e['id']}): alternative {alt} not in its decision"


def test_decisions_are_documented_and_referenced():
    refs = set()
    for section in ("equations", "parameters", "shocks", "steady_state", "aliases", "exogenous_zero"):
        for item in SPEC[section]:
            if item.get("decision"):
                refs.add(item["decision"])
            refs.update(item.get("see") or [])
    unknown = refs - set(DEC)
    assert not unknown, f"undocumented decisions referenced: {sorted(unknown)}"
    for d in SPEC["decisions"]:
        assert d["status"] in ("proposed", "accepted", "rejected"), d["id"]
        for field in ("title", "printed", "adopted", "applies_to"):
            assert d.get(field), f"{d['id']}: missing {field}"


def test_verified_flags():
    for e in SPEC["equations"]:
        assert e["verified"] in (True, False), e["id"]
        if e["verified"]:
            assert e.get("verified_by"), f"({e['id']}) is marked verified without a name"


# ----------------------------------------------------------------------------- names
def test_all_names_declared_and_all_variables_used(model):
    assert model.check_names() == []
    declared = {v["name"] for v in SPEC["variables"]}
    assert set(model.endogenous) == declared, "declared variables that no equation uses"


def test_names_follow_notation_codes():
    """Variables taken from Appendix D keep the code names of docs/paper/data/notation_codes.csv."""
    codes = {r["code_name"] for r in csv.DictReader((DATA / "notation_codes.csv").open(encoding="utf-8"))}
    new = {"nu", "epsilon_Pistar", "s_C", "pibar_OB"}            # introduced by decisions D22, D06, D04, D19
    for v in SPEC["variables"]:
        assert v["name"] in codes or v["name"] in new, v["name"]


# ----------------------------------------------------------------------------- numbers
def _table(path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _symbol(s):
    s = s.strip()
    if s.startswith("S.D.(") and s.endswith(")"):
        s = s[5:-1]
    return s.strip("$")


def test_estimated_values_match_tables_2_to_4():
    rows = {}
    for t in ("table2_structural.csv", "table3_observation_and_shocks.csv", "table4_world.csv"):
        for r in _table(DATA / t):
            if r["row_type"] == "data":
                rows[_symbol(r["symbol"])] = r
    checked = 0
    for item in SPEC["parameters"] + SPEC["shocks"]:
        if not str(item.get("source", "")).startswith("Table ") or item.get("source") == "Table 1":
            continue
        r = rows.get(item["paper_symbol"])
        assert r is not None, f"{item['name']}: symbol {item['paper_symbol']} not found in Tables 2-4"
        value = item["value"] if "value" in item else item["std"]
        assert value == pytest.approx(float(r["post_mode"])), item["name"]
        assert item["posterior_mean"] == pytest.approx(float(r["post_mean"])), item["name"]
        assert item["prior"]["mean"] == pytest.approx(float(r["prior_mean"])), item["name"]
        checked += 1
    assert checked == len(rows), f"{len(rows) - checked} table rows have no YAML entry"


def test_calibrated_values_match_table_1():
    rows = {_symbol(r["symbol"]): float(r["value"]) for r in _table(DATA / "table1_calibrated.csv")}
    used = set()
    for p in SPEC["parameters"]:
        if p.get("source") == "Table 1":
            assert p["value"] == pytest.approx(rows[p["paper_symbol"]]), p["name"]
            used.add(p["paper_symbol"])
    assert used == set(rows), f"Table 1 entries without a parameter: {set(rows) - used}"


def test_parameters_have_sources():
    for p in SPEC["parameters"]:
        assert p.get("value") is not None, p["name"]
        assert p["kind"] in ("calibrated", "fixed", "estimated", "derived", "assumed"), p["name"]
        if p["kind"] == "assumed":
            assert p.get("decision") in DEC, f"{p['name']}: an assumed value needs a decision"
        else:
            assert p.get("source"), f"{p['name']}: no source"
        if p["kind"] == "estimated":
            assert "posterior_mean" in p and "prior" in p, p["name"]


# ----------------------------------------------------------------------------- steady state
def test_steady_state_identities(model):
    v = model.values
    y = v["y_ss"]
    resource = (v["c_ss"] + v["p_I_ss"] * v["i_ss"] + v["dinv_ss"] * v["p_I_ss"] * y + v["p_G_ss"] * v["g_ss"]
                + v["s_ss"] * v["p_X_ss"] * v["p_Y_ss"] * v["x_ss"] - v["p_IM_ss"] * v["im_ss"])
    assert v["p_Y_ss"] * y == pytest.approx(resource, rel=1e-12)                                   # (153)
    value_added = v["p_H_ss"] * v["h_ss"] + v["s_ss"] * v["p_X_ss"] * v["p_Y_ss"] * v["x_ss"] - v["p_DX_ss"] * v["q_X_ss"]
    assert v["p_Y_ss"] * y == pytest.approx(value_added, rel=1e-12)                                # (152)
    assert v["q_X_ss"] == pytest.approx(v["x_ss"] + v["psi_X"], rel=1e-12)                        # (151)
    assert v["s_X_ss"] - v["s_IM_ss"] == pytest.approx(-v["s_FTR_ss"])                             # (141), (144)
    assert v["g_ss"] / y == pytest.approx(v["s_G"])                                                # (140)
    assert v["i_ss"] == pytest.approx((1 - (1 - v["delta"]) / v["g_z_ss"]) * v["k_ss"])            # (113)
    for name in ("c_ss", "i_ss", "x_ss", "im_ss", "h_C_ss", "h_I_ss", "h_G_ss", "h_X_ss", "N_ss", "psi"):
        assert v[name] > 0, name
    # the great ratios stated in Section 4.4.1, in percent of GDP
    ratios = {"c_ss": 55, "i_ss": 21, "g_ss": 26, "im_ss": 42}
    for name, pct in ratios.items():
        assert round(100 * v[name] / y) == pct, name
    assert round(100 * v["s_X_ss"]) == 39                                                          # exports
    # 167.u1 normalizes the relative prices to one
    for name in ("p_H_ss", "p_Y_ss", "p_IM_ss", "p_I_ss", "p_G_ss", "p_DX_ss"):
        assert v[name] == pytest.approx(1.0), name


# ----------------------------------------------------------------------------- solution
@pytest.mark.parametrize("param_set", ["value", "posterior_mean"])
def test_model_has_a_unique_stable_solution(param_set):
    sol = moise.solve(moise.load(param_set=param_set).linear_system())
    assert sol.n_stable == len(sol.variables)
    assert sol.residual < 1e-8
    assert sol.ybar is not None and np.all(np.isfinite(sol.ybar))


def test_structural_block_does_not_depend_on_measurement():
    full = moise.solve(moise.load().linear_system())
    core = moise.solve(moise.load(blocks_excluded=("measurement",)).linear_system())
    a = moise.impulse_response(full, "eta_R", periods=12, variables=["y", "pi_C", "r", "s"])
    b = moise.impulse_response(core, "eta_R", periods=12, variables=["y", "pi_C", "r", "s"])
    for k in a:
        np.testing.assert_allclose(a[k], b[k], atol=1e-12)


EXPECTED_TO_FAIL = {("D32", "printed"): "negative steady-state consumption",
                    ("D06", "printed"): "indeterminate"}


def test_every_decision_alternative_loads():
    for d in SPEC["decisions"]:
        for alt in d["alternatives"]:
            key = (d["id"], alt)
            if key in EXPECTED_TO_FAIL:
                with pytest.raises((ModelError, moise.SolveError)):
                    moise.solve(moise.load(decisions={d["id"]: alt}).linear_system())
                continue
            sol = moise.solve(moise.load(decisions={d["id"]: alt}).linear_system())
            assert sol.n_stable == len(sol.variables), key
