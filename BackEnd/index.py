from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from datetime import datetime, timedelta
from cachetools import TTLCache
import json
from main import get_place_info

app = Flask(__name__)
CORS(app)
@app.route('/getThirdPlace', methods=['GET'])
def get_third_place():
    
    api_key = "AIzaSyA5L1utCSQOnj7d-MKRU8kLUopQ3DUVE38"
    #first arg is the string from front end
    string = request.args.get('string')
    dict = get_place_info(string, api_key)
    return json.dumps(dict, indent=4)

@app.route('/getCommunity', methods=['GET'])
def get_community():
    activity = request.args.get('whatever')
    #call function that returns the
    dict = getCommunities(activity)
    return json.dumps(dict, indent = 4)

if __name__ == '__main__':
    port = 3000
    app.run(port=port)
    print(f'Open the URL: http://localhost:{port} in your browser')

