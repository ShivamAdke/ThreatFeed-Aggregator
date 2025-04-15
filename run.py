from flask import Flask
from app.routes import routes
from app.db import init_db
from app.collector import fetch_abuseipdb, fetch_otx
from app.db import insert_indicator
from app.notifier import send_alert

init_db()

app = Flask(__name__)
app.register_blueprint(routes)

# Fetch OTX feeds and insert into DB with alerts
for ip in fetch_otx():
    if ip.strip():
        insert_indicator("OTX", ip.strip())
        send_alert(f"[OTX] New IP Detected: {ip.strip()}")

if __name__ == "__main__":
    app.run(debug=True)

