"""@file
@brief Entry point for `python -m downloads_organiser`.
"""

import sys

from downloads_organiser.presentation.cli import main

if __name__ == "__main__":
    sys.exit(main())
