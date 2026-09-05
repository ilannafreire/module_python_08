import os
import site
import sys


def construct() -> None:
    """Display information about the Python environment."""
    virtual_env = os.environ.get("VIRTUAL_ENV")
    is_virtual_env = sys.prefix != sys.base_prefix

    if is_virtual_env:
        environment_path = virtual_env or sys.prefix
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(environment_path)}")
        print(f"Environment Path: {environment_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("Global package installation path:")
        print(site.getsitepackages()[0])

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")

        print("Then run this program again.")


if __name__ == "__main__":
    construct()
