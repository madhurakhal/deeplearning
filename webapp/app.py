import os
import json
from PIL import Image
from io import StringIO
from flask import Response, abort
from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory


app = Flask(__name__)
app.config['SECRET_KEY'] = 'weareLearningDeepLearxingokjalsf2oue'

## handling static images
current_directory = os.getcwd()

## handleing feedback_dir
feedback_dir = current_directory + '/feedbacks/'

parent_path = "/".join(current_directory.split('/')[:-1])
file_dir = parent_path + '/' + 'images/'
@app.route('/<path:filename>', methods=['get', ])
def image(filename):
    try:
        return send_from_directory(file_dir, filename)
    except:
        abort(404)


@app.route('/', methods=['get', ])
def index():
    return render_template('pages/index.html')

@app.route('/search', methods=['POST', ])
def search():
    search_query = request.form.get('search')
    rand_images = ['01.jpg']
    return render_template('pages/result.html', query=search_query, images=rand_images)

@app.route('/feedback', methods=['POST', ])
def feedback():
    feedback_raw = request.form.to_dict()
    feedback_dict = json.loads(feedback_raw['feedback'])
    query = feedback_dict['query']
    images = feedback_dict['images']
    if query is not None:
        return "There is no query "
    return "thankyou for your feedback"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    # TODO: Please remove while going to production
    app.run(debug=True)
