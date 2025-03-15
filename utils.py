import subprocess
import platform
import os

def get_log_path():
    """Determine the correct log file path based on the OS."""
    os_name = platform.system().lower()
    
    if "linux" in os_name:
        if os.path.exists("/var/log/auth.log"):
            return "/var/log/auth.log"
        elif os.path.exists("/var/log/secure"):  # Red Hat-based distros
            return "/var/log/secure"
        else:
            return None  # Use journalctl as a fallback

    elif "darwin" in os_name:  # macOS
        return "/var/log/system.log"

    elif "windows" in os_name:
        return "C:\\Windows\\System32\\winevt\\Logs\\Security.evtx"

    return None

def get_failed_logins():
    """Retrieve failed login attempts dynamically based on available logs."""
    log_path = get_log_path()

    if log_path:
        try:
            with open(log_path, "r") as log_file:
                logs = log_file.readlines()
            return [line for line in logs if "Failed password" in line]
        except Exception as e:
            print(f"Error reading log file: {e}")
            return []
    
    # If log file isn't found, use journalctl as a fallback
    try:
        output = subprocess.run(
            ["journalctl", "-u", "ssh", "--no-pager", "--grep", "Failed password"],
            capture_output=True,
            text=True
        )
        return output.stdout.split("\n")
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return []

