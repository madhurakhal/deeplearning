from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'weareLearningDeepLearxingokjalsf2oue'

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/search', methods=['POST', ])
def search():
    search_query = request.form.get('search')
    return render_template('pages/result.html', query=search_query)

@app.route('/feedback')
def feedback():
    return "thankyou for your feedback"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    # TODO: Please remove while going to production
    app.run(debug=True)
