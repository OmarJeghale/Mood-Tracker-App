from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os

# Initialize Flask app w/ folders
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = os.getenv('SECRET_KEY')

# Load .env variables
load_dotenv()

# Store moods in memory
mood_log = []

# Homepage route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name', '').strip()
        mood = request.form.get('mood', '').strip()
        
        # Validate the input
        if not name:
            flash('Please enter your name.', 'error')
            return redirect(url_for('index'))
        if not mood:
            flash('Please select your mood.', 'error')
            return redirect(url_for('index'))

        # Clean up formatting
        name = name.title()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Store and append entry
        entry = {
            'name': name,
            'mood': mood,
            'timestamp': timestamp
        }
        
        mood_log.append(entry)
        
        flash('Mood submitted successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html', mood_log=mood_log)
# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
    