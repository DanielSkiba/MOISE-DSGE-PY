"""MOISE-DSGE-PY: independent replication of the Bank of Israel MOISE DSGE model.

Not affiliated with or endorsed by the Bank of Israel.

The package is generic: it loads any linear rational-expectations model written in the YAML
format of ``docs/equation-spec.md`` and solves it. The MOISE model itself is ``model/moise.yaml``.
"""

from .expr import ExprError, parse, parse_equation
from .irf import impulse_response, simulate, variance_decomposition
from .model import LinearSystem, Model, ModelError
from .solve import Solution, SolveError, solve

__version__ = "0.1.0"

__all__ = [
    "ExprError", "parse", "parse_equation",
    "Model", "ModelError", "LinearSystem",
    "solve", "Solution", "SolveError",
    "impulse_response", "simulate", "variance_decomposition",
    "load", "__version__",
]


def load(path: str = None, **kwargs) -> Model:
    """Load a model file (default: the bundled MOISE model, model/moise.yaml in the repository)."""
    import os
    if path is None:
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(here, "..", "..", "model", "moise.yaml")
    return Model.from_yaml(path, **kwargs)
