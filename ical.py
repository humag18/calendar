import icalendar
from datetime import datetime, timedelta
import pytz  # Importez la bibliothèque pytz

def extraire_semaine(fichier_ical):
    semaine_events = []

    # Obtenez la date et l'heure actuelles en UTC
    ajd_utc = datetime.now(pytz.utc)

    # Calculez le nombre de jours jusqu'au prochain lundi (0 correspond à lundi, 1 à mardi, etc.)
    jours_jusqu_au_lundi_suivant = (0 - ajd_utc.weekday() + 6) % 7

    # Ajoutez le nombre de jours calculé à la date actuelle pour obtenir la date du lundi suivant
    date_debut_semaine_utc = ajd_utc + timedelta(days=jours_jusqu_au_lundi_suivant)

    with open(fichier_ical, 'rb') as f:
        cal = icalendar.Calendar.from_ical(f.read())

        for event in cal.walk('VEVENT'):
            event_start = event.get('DTSTART').dt
            if isinstance(event_start, datetime):

                # Assurez-vous que les dates sont timezone-aware
                if not event_start.tzinfo:
                    event_start = event_start.replace(tzinfo=pytz.utc)

                # Vérifier si l'événement se trouve dans la semaine spécifiée
                if event_start >= date_debut_semaine_utc and event_start < date_debut_semaine_utc + timedelta(days=7):
                    semaine_events.append(event)

    return semaine_events

# Exemple d'utilisation
fichier_ical = 'portail.ical'
evenements_semaine = extraire_semaine(fichier_ical)
# Créer un nouveau fichier iCal avec les événements de la semaine
nouveau_cal = icalendar.Calendar()

for event in evenements_semaine:
    nouveau_cal.add_component(event)
# Enregistrez les événements de la semaine dans un nouveau fichier iCal
with open('nouveau_fichier.ical', 'wb') as f:
    f.write(nouveau_cal.to_ical())

print("nouveau fichier ical créer")
