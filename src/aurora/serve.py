"""aurora.serve — minimal HTTP entry point (stub for L93 Docker demo).

This module is referenced in the L93 MLOps Dockerfile ENTRYPOINT:
    ENTRYPOINT ["python", "-m", "aurora.serve"]

It currently prints version/health info and exits.  Replace with a real
FastAPI/Flask app when deploying Aurora as a service.
"""

from aurora import __version__  # type: ignore[import]
import sys


def main() -> None:
    print(f"Aurora serve stub  version={__version__}")
    print("Status: healthy")
    print("(This is a placeholder — implement a real server here.)")
    sys.exit(0)


if __name__ == "__main__":
    main()
