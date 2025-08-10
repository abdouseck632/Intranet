from flask import Flask, render_template, request, redirect, url_for,session
import json



app = Flask(__name__)
app.secret_key = "clé_très_secrète_à_changer" 
# Identifiants fixes
VALID_USERNAME = "admin"
VALID_PASSWORD = "secret1234"
@app.route('/invites')
def invites():
    return render_template('invites.html')
@app.route('/')
def home():
    if 'logged_in' in session and session['logged_in']:
        return render_template('home.html')
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username," - ", password)
        # Vérification des identifiants
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            # Identifiants incorrects
            return render_template('login.html', error="Identifiant ou mot de passe incorrect")
    
    # Méthode GET - Afficher le formulaire
    return render_template('login.html')

def get_color_for_type(event_type):
    """Retourne la couleur correspondant au type d'événement"""
    colors = {
        'conference': '#3a86ff',  # Bleu vif
        'workshop': '#8338ec',    # Violet
        'thesis': '#ff006e',      # Rose
        'meeting': '#fb5607',     # Orange
        'other': '#3a5a40'        # Vert foncé
    }
    return colors.get(event_type.lower(), '#3a5a40')  # Couleur par défaut
def load_events():
    with open('static/data/events.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_end_time(start_time, duration_minutes):
    hours, minutes = map(int, start_time.split(':'))
    total_minutes = hours * 60 + minutes + duration_minutes
    return f"{total_minutes // 60:02d}:{total_minutes % 60:02d}"
@app.route('/add_seminaire', methods=['POST'])
def add_seminaire():
    events = load_events()
    
    new_event = {
        'id': len(events) + 1,
        'title': request.form['title'],
        'speaker': request.form['speaker'],
        'date': request.form['date'],
        'time': request.form['time'],
        'duration': int(request.form['duration']),
        'location': request.form['location'],
        'description': request.form['description'],
        'type': request.form['type'],
        'color': get_color_for_type(request.form['type'])
    }
    
    events.append(new_event)
    save_events(events)
    
    return redirect(url_for('seminaires'))
def save_events(events):
    with open('static/data/events.json', 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=2, ensure_ascii=False)
@app.route('/seminaires')
def seminaires():
    events = load_events()
    
    # Ajout des couleurs et formatage pour FullCalendar
    for event in events:
        event['color'] = get_color_for_type(event.get('type', 'other'))
        event['start_iso'] = f"{event['date']}T{event['time']}"
        event['end_iso'] = f"{event['date']}T{calculate_end_time(event['time'], event['duration'])}"
    
    return render_template('seminaires.html', events=events)
if __name__ == '__main__':
    app.run(debug=True)