# Government Wealth Tracking Models
from .government_wealth import Base as GovWealthBase

# Core models from models.py — re-exported so `from .models import Entity` resolves correctly
# when the models/ package shadows models.py
import importlib as _il
import os as _os
import sys as _sys

_models_py = _os.path.join(_os.path.dirname(_os.path.dirname(__file__)), 'models.py')
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("app.models_flat", _models_py)
_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

Entity = _mod.Entity
Evidence = _mod.Evidence
Relationship_ = _mod.Relationship_
TimelineEvent = _mod.TimelineEvent
