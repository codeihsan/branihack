from flask import *
import glob
import logging
from werkzeug.contrib.cache import SimpleCache
import logging

cache = SimpleCache()
app = Flask(__name__)
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# add ch to logger
logger.addHandler(ch)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/image")
def image():
	images = [infile for infile in glob.glob("static/images/*.jpg")]
	return jsonify(data="idiot")

if __name__ == "__main__":
    app.run(debug=True)

