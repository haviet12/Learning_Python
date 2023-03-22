import cx_Freeze
import sys
from cx_Freeze import setup, Executable

base=None
if sys.platform == 'win32':
    base=='WIN32GUI'

setup(name='program', version='1.0', description='BINARY CONVERTION',executables=[Executable('NGUYEN_VIET_HA_20146489.py',base=base)])

