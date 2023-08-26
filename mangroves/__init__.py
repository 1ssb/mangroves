try:
    from .mangrove import Mangrove
except Exception as e:
    raise ImportError(f"Failed to import Mangrove class: {e}")
