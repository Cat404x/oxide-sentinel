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

## Project Structure (Planned)

```
oxide-sentinel/
├── control/        # Python control plane
├── collectors/     # Rust collectors
├── schemas/        # JSON schemas
├── reports/        # Output formatting
└── docs/
```

---

## Status

Initial scaffold phase.
Architecture being defined.
Collectors not yet implemented.
