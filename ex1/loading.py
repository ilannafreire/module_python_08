import importlib


def check_dependencies() -> bool:
    """Check if required packages are installed."""
    dependencies = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computation"),
        ("matplotlib", "Visualization")
    ]

    all_ok = True

    print("Checking dependencies:")

    for name, description in dependencies:
        try:
            module = importlib.import_module(name)
            print(
                f"[OK] {name} ({module.__version__}) - "
                f"{description} ready"
            )
        except ImportError:
            all_ok = False
            print(f"[MISSING] {name} - {description} not found")
            print(f"    -> Install with pip: pip install {name}")
            print(f"    -> Or with poetry: poetry add {name}")

    return all_ok


def compare_versions() -> None:
    """Show the installed package versions."""
    packages = ["pandas", "numpy", "matplotlib"]

    print("\nInstalled package versions:")

    for package in packages:
        module = importlib.import_module(package)
        print(f"- {package}: {module.__version__}")


def show_package_management() -> None:
    """Show pip and Poetry commands."""
    print("\nDependency management:")
    print("pip: pip install -r requirements.txt")
    print("Poetry: poetry install")
    print("Poetry: poetry run python loading.py")


def analyse_matrix() -> None:
    """Generate Matrix data and create a visualization."""
    import numpy
    import pandas
    import matplotlib.pyplot as plt

    signal = numpy.random.rand(1000)
    time = numpy.arange(1000)

    data = pandas.DataFrame({
        "time": time,
        "signal": signal
    })

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    plt.figure(figsize=(10, 5))
    plt.plot(data["time"], data["signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.grid(True)
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def loading() -> None:
    """Run the Matrix data analysis."""
    print("\nLOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print("\nERROR: Missing required dependencies. Aborting.")
        print("Install all dependencies with:")
        print("  pip install -r requirements.txt")
        print("or:")
        print("  poetry install")
        return

    compare_versions()
    show_package_management()
    analyse_matrix()


if __name__ == "__main__":
    loading()
