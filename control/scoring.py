"""Oxide Sentinel – placeholder risk scoring module."""


def score_telemetry(telemetry: dict) -> dict:
    """Compute a simple risk score from collector telemetry.

    This is a placeholder implementation. Real scoring logic would inspect
    the telemetry payload and apply rule-based or ML-driven heuristics.

    Args:
        telemetry: Parsed JSON telemetry dict from a collector.

    Returns:
        A dict with keys:
            - ``risk_score`` (int): 0–100, where 0 is lowest risk.
            - ``reasons`` (list[str]): Human-readable reasons for the score.
    """
    reasons = []
    risk_score = 0

    data = telemetry.get("data", {})
    os_name = data.get("os_name", "")

    if not os_name:
        risk_score += 10
        reasons.append("OS name could not be determined")

    if risk_score == 0:
        reasons.append("No risk indicators detected")

    return {"risk_score": risk_score, "reasons": reasons}
