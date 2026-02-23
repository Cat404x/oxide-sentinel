use chrono::Utc;
use serde::Serialize;

#[derive(Serialize)]
struct SystemData {
    os_name: String,
    os_version: String,
    hostname: String,
}

#[derive(Serialize)]
struct TelemetryEnvelope {
    collector: String,
    timestamp: String,
    data: SystemData,
}

fn main() {
    let data = SystemData {
        os_name: std::env::consts::OS.to_string(),
        os_version: os_version(),
        hostname: hostname::get()
            .map(|h| h.to_string_lossy().into_owned())
            .unwrap_or_else(|_| "unknown".to_string()),
    };

    let envelope = TelemetryEnvelope {
        collector: "system_info".to_string(),
        timestamp: Utc::now().to_rfc3339(),
        data,
    };

    // Output only JSON – no other text to stdout.
    println!("{}", serde_json::to_string_pretty(&envelope).unwrap());
}

/// Return a best-effort OS version string.
fn os_version() -> String {
    // On Linux read /etc/os-release; on other platforms fall back gracefully.
    #[cfg(target_os = "linux")]
    {
        if let Ok(contents) = std::fs::read_to_string("/etc/os-release") {
            for line in contents.lines() {
                if let Some(val) = line.strip_prefix("PRETTY_NAME=") {
                    return val.trim_matches('"').to_string();
                }
            }
        }
    }
    // Fallback: use the compile-time target family.
    std::env::consts::FAMILY.to_string()
}
