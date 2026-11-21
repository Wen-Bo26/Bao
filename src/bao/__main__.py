"""Allow ``python -m bao``."""

from bao.main import main

if __name__ == "__main__":
    raise SystemExit(main())
