from fastapi import FastAPI, Query
from collections import Counter
from typing import Optional

app = FastAPI(title="DevOps Log Analyzer API")


def analyze_logs(file_path: str, level: Optional[str] = None):
    counts = Counter()

    try:
        with open(file_path, "r") as file:
            for line in file:
                if "INFO" in line:
                    counts["INFO"] += 1
                elif "ERROR" in line:
                    counts["ERROR"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
    except FileNotFoundError:
        return {"error": "Log file not found"}

    if level:
        return {level: counts.get(level, 0)}

    return dict(counts)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "log-analyzer-api"
    }


@app.get("/logs")
def get_logs(
    file: str = Query(..., description="Path to log file"),
    level: Optional[str] = Query(
        None, description="Filter by log level (INFO, ERROR, WARNING)"
    )
):
    result = analyze_logs(file, level)
    return {
        "file": file,
        "summary": result
    }


@app.get("/aws")
def aws_summary():
    return {
        "message": "AWS summary endpoint (to be implemented)",
        "status": "not implemented"
    }
