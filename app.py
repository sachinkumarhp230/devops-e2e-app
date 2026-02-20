from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Total request counter
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "http_status"]
)

# Request latency histogram
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "HTTP request latency"
)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    latency = time.time() - request.start_time
    REQUEST_LATENCY.observe(latency)

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        http_status=response.status_code
    ).inc()

    return response

@app.route("/")
def home():
    return "DevOps E2E Platform — DEV"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)