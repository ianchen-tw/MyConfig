from . import setup
from . import load
import sys

message=(
"""
Must supplied with 'load' or 'install' keywords
    load: save current user settings to the package
    install: install the package 
 example:
    python -m autosetup load
    python -m autosetup install
""")

if __name__ == "__main__":
    if len(sys.argv)<2:
        print(message)
        exit(1)
    cmd = sys.argv[1]
    if cmd == 'load':
        load.main()
    elif cmd == 'install':
        setup.main()
    else:
        print(message)
        exit(1)