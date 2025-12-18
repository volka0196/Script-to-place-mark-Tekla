import ctypes
import sys
import subprocess
from Tekla1 import ScriptController    # type: ignore

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def request_admin_privileges():
    try:
        result = ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        return result > 32
    except Exception as e:
        print("Error:", str(e))
        return False

if not is_admin():
    success = request_admin_privileges()
    sys.exit()
else:
    print("Running with admin privileges")

if __name__ == "__main__":
    script = ScriptController()
    script.start()
    script.loop()