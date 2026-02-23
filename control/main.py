"""Oxide Sentinel – CLI entry point."""

import argparse
import json
import sys

from orchestrator import run_collector
from scoring import score_telemetry


def main():
    parser = argparse.ArgumentParser(
        description="Oxide Sentinel – host integrity framework"
    )
    parser.add_argument(
        "--collector",
        default="system_info",
        help="Name of the collector to run (default: system_info)",
    )
    args = parser.parse_args()

    telemetry = run_collector(args.collector)

    print("=== Telemetry ===")
    print(json.dumps(telemetry, indent=2))

    result = score_telemetry(telemetry)
    print("\n=== Risk Score ===")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
