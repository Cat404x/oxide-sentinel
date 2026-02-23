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

Running Oxide Sentinel

Oxide Sentinel requires:
	•	Python 3.8+
	•	Rust (via rustup)
	•	Cargo (installed with Rust)

⸻

🐧 Linux (Ubuntu / Debian)

1️⃣ Install Dependencies

sudo apt update
sudo apt install build-essential curl git python3 python3-pip -y

Install Rust:

curl https://sh.rustup.rs -sSf | sh

Restart your terminal, then verify:

rustc --version
cargo --version
python3 --version


⸻

2️⃣ Clone Repository

git clone https://github.com/Cat404x/oxide-sentinel.git
cd oxide-sentinel


⸻

3️⃣ Build Rust Collector

cd collectors/system_info
cargo build --release
cp target/release/system_info ../bin/
cd ../../


⸻

4️⃣ Run Control Plane

cd control
python3 main.py


⸻

🪟 Windows

You have two options.

⸻

✅ Recommended: Windows + WSL (Cleanest)

Install WSL

Open PowerShell (Admin):

wsl --install

Restart PC.

Open Ubuntu app.

Then follow the Linux instructions above.

This is the cleanest setup.

⸻

⚙️ Native Windows (No WSL)

1️⃣ Install Rust

Download and run:

https://rustup.rs

Then verify in PowerShell:

rustc --version
cargo --version


⸻

2️⃣ Install Python

Download from:

https://python.org

Verify:

python --version


⸻

3️⃣ Clone Repo

git clone https://github.com/Cat404x/oxide-sentinel.git
cd oxide-sentinel


⸻

4️⃣ Build Rust Collector

cd collectors\system_info
cargo build --release
copy target\release\system_info.exe ..\bin\
cd ..\..\control


⸻

5️⃣ Run Control Plane

python main.py


⸻

Expected Output

The control plane should:
	•	Execute the Rust collector
	•	Receive JSON over stdout
	•	Aggregate telemetry
	•	Print structured output

⸻

Common Errors

Rust not found

Add Cargo to PATH:

$env:Path += ";$env:USERPROFILE\.cargo\bin"

Python not found

Ensure Python is added to PATH during installation.
