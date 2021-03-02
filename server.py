import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

import csv
import os
import pandas as pd

app = Flask(__name__)
cors = CORS(app)

@app.route('/get-basic-data', methods=['GET'])
def get_basic_data() -> str:
    return 'hi'

@app.route('/')
def start():
    return 'start'

def main():
    app.run(host='0.0.0.0', port=5006)
    # app.run()

if __name__ == '__main__':
    main()