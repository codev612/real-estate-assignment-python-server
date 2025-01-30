from flask import Blueprint, jsonify
from app.scraping.scraper import scrape_listings

scrape_bp = Blueprint('scrape', __name__)

@scrape_bp.route('/scrape', methods=['GET'])
def scrape():
    listings = scrape_listings()
    return jsonify(listings)
