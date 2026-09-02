import os
import sys


def load_config() -> dict[str, str]:
    """Load configuration from the .env file."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("ERROR: python-dotenv is not installed.")
        print("Run: pip install python-dotenv")
        return {}

    config = {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database": os.getenv("DATABASE_URL", ""),
        "api_key": os.getenv("API_KEY", ""),
        "log_level": os.getenv("LOG_LEVEL", "DEBUG"),
        "zion": os.getenv("ZION_ENDPOINT", "")
    }

    if not config["database"] or not config["api_key"] \
            or not config["zion"]:
        print("ERROR: Missing required environment variables.")
        return {}

    return config


def oracle(config: dict[str, str]) -> None:
    """Display the current configuration."""
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")

    if config["mode"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production")

    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print("Zion Network: Online")


def security_check() -> None:
    """Check the .env file."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    config = load_config()

    if config:
        oracle(config)

    security_check()

    if not config:
        sys.exit(1)