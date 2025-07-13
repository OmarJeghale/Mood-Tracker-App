from flask import Flask, render_template, request
from datetime import datetime

# Initialize Flask app w/ folders
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

# Store moods in memory
mood_log = []

# Homepage route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form['name'].title()
        mood = request.form['mood']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        entry = {
            'name' : name,
            'mood' : mood,
            'timestamp' : timestamp
        }
        
        mood_log.append(entry)
        
    return render_template('index.html', mood_log=mood_log)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    