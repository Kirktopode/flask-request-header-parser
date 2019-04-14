#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, render_template, jsonify
# from dateutil.parser import parse
# from datetime import datetime

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

@app.route('/')
def homepage():
    # print("index")
    """Displays thot hormeparger."""
    return render_template('index.html')
    
@app.route('/api/whoami/', methods=['GET', 'POST'])
def whoami():
    """Simple API my hoes anddreas.
    """
    dict = {
      "ipaddress":request.headers["X-Forwarded-For"][:13],
      "language":request.headers["Accept-Language"],
      "software":request.headers["User-Agent"],
    }
    print(request.headers)
    return jsonify(dict)

if __name__ == '__main__':
    app.run()