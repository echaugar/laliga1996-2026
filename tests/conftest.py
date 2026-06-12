"""Configuración de pytest: añade src al path de importación."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
