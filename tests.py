import random
import json
from datetime import datetime, timedelta

EVENTS_FILE = 'static/data/events.json'

TYPES = [
    ("Séminaire Machine Learning", "conference", "#3a86ff"),
    ("Atelier Python Avancé", "workshop", "#8338ec"),
    ("Conférence IA et Santé", "conference", "#ff006e"),
    ("Formation Deep Learning", "workshop", "#fb5607"),
    ("Table ronde sur l'IA", "conference", "#ffbe0b")
]

SAMPLE_EVENTS = []

start_date = datetime.now()
current_date = start_date

for i in range(1, 351):
    # Décalage de 2 à 4 jours pour garder de la variété
    days_jump = random.randint(2, 4)
    current_date += timedelta(days=days_jump)

    # Si on dépasse un an, on arrête
    if (current_date - start_date).days > 100:
        break

    title, type_event, color = random.choice(TYPES)

    SAMPLE_EVENTS.append({
        "id": i,
        "title": title,
        "speaker": f"Dr. {random.choice(['Sophie', 'Jean', 'Luc', 'Emma', 'Paul'])} {random.choice(['Martin', 'Dupont', 'Durand', 'Petit', 'Lefèvre'])}",
        "date": current_date.strftime('%Y-%m-%d'),
        "time": f"{random.randint(8, 18):02d}:{random.choice(['00', '30'])}",
        "duration": random.choice([60, 90, 120]),
        "location": f"Salle {random.choice(['A', 'B', 'C'])}{random.randint(1, 20):02d}",
        "description": "Description auto-générée de l'événement.",
        "type": type_event,
        "color": color
    })

# Sauvegarder dans le fichier JSON
with open(EVENTS_FILE, 'w', encoding='utf-8') as f:
    json.dump(SAMPLE_EVENTS, f, ensure_ascii=False, indent=4)

print(f"{len(SAMPLE_EVENTS)} événements sauvegardés dans {EVENTS_FILE}")
