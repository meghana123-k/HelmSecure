from flask import Flask

from routes.dashboard_routes import dashboard_bp
from routes.monitoring_routes import monitoring_bp

app = Flask(__name__)
app.register_blueprint(dashboard_bp)
app.register_blueprint(monitoring_bp)

print(app.url_map)
if __name__ == "__main__":
    app.run(debug=False, threaded=True)
