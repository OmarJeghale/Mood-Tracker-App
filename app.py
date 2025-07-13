from flask import Flask, render_template, request

# Initialize Flask app w/ folders
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# Homepage route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return ''
    else:
        return ''
        

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    