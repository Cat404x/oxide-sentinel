"""Oxide Sentinel – orchestrator.

Runs Rust collector executables via subprocess and returns parsed JSON telemetry.
Collectors are expected to reside at: collectors/bin/<collector_name>
"""

import json
import os
import subprocess
from pathlib import Path


# Resolve the path to collectors/bin relative to this file's location.
_REPO_ROOT = Path(__file__).resolve().parent.parent
_BIN_DIR = _REPO_ROOT / "collectors" / "bin"


def run_collector(collector_name: str) -> dict:
    """Run a named collector and return its parsed JSON output.

    Args:
        collector_name: The name of the collector (matches an executable in
                        collectors/bin/).

    Returns:
        A dict representing the parsed JSON telemetry from the collector.

    Raises:
        FileNotFoundError: If the collector executable does not exist.
        RuntimeError: If the collector exits with a non-zero return code.
        ValueError: If the collector output is not valid JSON.
    """
    executable = _BIN_DIR / collector_name
    if not executable.exists():
        raise FileNotFoundError(
            f"Collector executable not found: {executable}\n"
            "Build the collector and copy it to collectors/bin/ before running."
        )

    result = subprocess.run(
        [str(executable)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Collector '{collector_name}' exited with code {result.returncode}.\n"
            f"stderr: {result.stderr.strip()}"
        )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Collector '{collector_name}' produced invalid JSON: {exc}\n"
            f"stdout: {result.stdout!r}"
        ) from exc
