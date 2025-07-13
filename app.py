from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Initialize Flask app w/ folders
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = os.getenv('SECRET_KEY')

# Store moods in memory
mood_log = []

# Datetime helper function for cleaner look
def time_ago(dt):
    now = datetime.now()
    diff = now - dt

    if diff < timedelta(minutes=1):
        return "just now"
    elif diff < timedelta(hours=1):
        mins = diff.seconds // 60
        return f"{mins} minute{'s' if mins != 1 else ''} ago"
    elif diff < timedelta(days=1):
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif diff < timedelta(days=7):
        days = diff.days
        return f"{days} day{'s' if days != 1 else ''} ago"
    else:
        return dt.strftime("%Y-%m-%d")
    
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
        timestamp = datetime.now()

        # Store and append entry
        entry = {
            'name': name,
            'mood': mood,
            'timestamp': timestamp
        }
        
        mood_log.append(entry)
        
        flash('Mood submitted successfully!', 'success')
        return redirect(url_for('index'))
    
    # Convert timestamps
    friendly_log = [
        {
            'name': entry['name'],
            'mood': entry['mood'],
            'timestamp': time_ago(entry['timestamp'])
        }
        for entry in reversed(mood_log)
    ]
    
    return render_template('index.html', mood_log=friendly_log)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)