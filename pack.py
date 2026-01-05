import subprocess
import sys
import os
from . import header

def boot():
    header.banner()
    subprocess.run([sys.executable, '-m','pip','install','-r','requirements.txt'])
