# import Flask
from flask import *

# create app with folder paths
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# default route
@app.route('/')
def index():
    return render_template('index.html')

# run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    