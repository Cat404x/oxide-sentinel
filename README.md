# Oxide Sentinel

Oxide Sentinel is a modular telemetry-driven host integrity framework.

---

## Architecture Overview

Oxide Sentinel is built around strict separation of responsibilities:

- **Python** → Control plane (orchestration, scoring, reporting, CLI)
- **Rust** → High-performance telemetry collectors
- **JSON boundary** between layers
- No FFI
- No shared memory
- Fault-isolated collectors

---

## Design Principles

- Deterministic execution
- Telemetry over signatures
- Graceful failure handling
- Modular collector expansion
- Cross-platform future support (Linux, macOS, Windows)

---

## Project Structure

```
oxide-sentinel/
├── control/                        # Python control plane
│   ├── main.py                     # CLI entry point (argparse)
│   ├── orchestrator.py             # Runs Rust collectors via subprocess
│   └── scoring.py                  # Placeholder risk scoring
├── collectors/
│   ├── system_info/                # Rust collector: OS / hostname telemetry
│   │   ├── Cargo.toml
│   │   └── src/main.rs
│   └── bin/                        # Compiled collector executables (gitignored binaries)
├── shared/
│   └── schemas/
│       └── telemetry.schema.json   # JSON schema for the telemetry envelope
└── README.md
```

---

## Quickstart

### 1. Build the `system_info` collector

```bash
cd collectors/system_info
cargo build --release
cp target/release/system_info ../bin/system_info
```

### 2. Run the control plane

```bash
cd control
python main.py                          # uses system_info by default
python main.py --collector system_info  # explicit collector name
```

---

## Status

Initial scaffold complete.
Collectors implemented: `system_info`.
