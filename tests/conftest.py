from pathlib import Path
import sys

PACKAGE_ROOT = Path(__file__).parent
PROJECT_ROOT = PACKAGE_ROOT.parent

sys.path.insert(0, str(PROJECT_ROOT.absolute()))

from advent_of_code import day_01, day_02, day_03, day_04
