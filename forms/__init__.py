'''Forms package.'''

import sys
import os
from resources import resources_rc
import resources

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "resources"))

__all__ = ['Ui_main']
