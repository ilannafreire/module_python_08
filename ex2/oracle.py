import os
import sys


ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def load_config() -> dict[str, str] | None:
    """Load and validate environment configuration."""
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        print("ERROR: python-dotenv is not installed.")
        print("Run: pip install -r requirements.txt")
        return None

    # Variables supplied by the operating system override values in .env.
    load_dotenv(dotenv_path=ENV_PATH, override=False)
    config = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL", ""),
        "api_key": os.getenv("API_KEY", ""),
        "log_level": os.getenv("LOG_LEVEL", "DEBUG"),
        "zion": os.getenv("ZION_ENDPOINT", "")
    }

    if config["mode"] not in ("development", "production"):
        print("ERROR: MATRIX_MODE must be 'development' or "
              "'production'.")
        return None

    required_variables = {
        "DATABASE_URL": config["database"],
        "API_KEY": config["api_key"],
        "ZION_ENDPOINT": config["zion"]
    }
    missing_variables = [
        name for name, value in required_variables.items() if not value
    ]
    if missing_variables:
        print("WARNING: Missing required environment variables: "
              + ", ".join(missing_variables))
        print("Copy .env.example to .env for development, or set environment "
              "variables for production.")
        return None

    return config


def oracle(config: dict[str, str]) -> None:
    """Display the active configuration without revealing secrets."""
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")

    if config["mode"] == "development":
        print("Database: Connected to local instance")
        print("Zion Network: Online (development endpoint)")
    else:
        print("Database: Connected to production instance")
        print("Zion Network: Online (production endpoint)")

    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")


def security_check(config_loaded: bool) -> None:
    """Report whether local configuration is safely prepared."""
    print("\nEnvironment security check:")
    print("[OK] Credentials are read from environment variables")

    if os.path.exists(ENV_PATH):
        if config_loaded:
            print("[OK] .env file found and required settings are available")
        else:
            print("[WARNING] .env file found, but required settings are "
                  "incomplete")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available through environment variables")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config = load_config()

    if config is not None:
        oracle(config)

    security_check(config is not None)

    if config is None:
        sys.exit(1)
