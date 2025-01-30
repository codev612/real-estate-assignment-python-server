from flask import Flask
from app.routes.scrape import scrape_bp
from app.routes.analyze import analyze_bp
from app.routes.add_to_sheet import add_to_sheet_bp

app = Flask(__name__)
app.register_blueprint(scrape_bp)
app.register_blueprint(analyze_bp)
app.register_blueprint(add_to_sheet_bp)

if __name__ == '__main__':
    app.run(debug=True)
