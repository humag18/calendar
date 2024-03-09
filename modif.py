
import icalendar
from datetime import datetime
import pytz

def extraire_informations_evenement(ical_event):
    # Récupérer les informations de l'événement
    summary = ical_event.get('SUMMARY')
    dtstart = ical_event.get('DTSTART').dt
    dtend = ical_event.get('DTEND').dt
    location = ical_event.get('LOCATION')

    # Formater les informations
    nom_cours = summary.split('-')[0].strip()
    date_heure = f"{dtstart.strftime('%Y-%m-%d %H:%M')} - {dtend.strftime('%H:%M')}"
    lieu = location if location else "Non spécifié"

    return nom_cours, date_heure, lieu

# Exemple d'utilisation avec le nouveau fichier iCal
fichier_nouveau_ical = 'nouveau_fichier.ical'
fichier_resultat_ical = 'informations_cours.ical'

with open(fichier_nouveau_ical, 'rb') as f:
    cal_nouveau = icalendar.Calendar.from_ical(f.read())

    nouveau_cal = icalendar.Calendar()

    for event_nouveau in cal_nouveau.walk('VEVENT'):
        nom_cours, date_heure, lieu = extraire_informations_evenement(event_nouveau)

        # Ajouter une condition pour exclure certains noms de cours
        noms_a_exclure = ["Technologie de sauvegarde des informations", 
                          "OPTION: Allemand ou Néerlandais ou Anglais renforcement (Anglais renfo uniquement pour les 2 TI A)", 
                          "Programmation orientée systèmes d'exploitation"]

        if nom_cours not in noms_a_exclure:
            # Créer un nouvel événement iCal avec les informations extraites
            nouvel_event = icalendar.Event()
            nouvel_event.add('dtstart', event_nouveau.get('DTSTART').dt)
            nouvel_event.add('dtend', event_nouveau.get('DTEND').dt)
            nouvel_event.add('summary', nom_cours)
            nouvel_event.add('location', lieu)
            nouvel_event.add('description', f"Heure et date: {date_heure}\nLieu: {lieu}")

            nouveau_cal.add_component(nouvel_event)

# Enregistrez les événements extraits dans un nouveau fichier iCal
with open(fichier_resultat_ical, 'wb') as f:
    f.write(nouveau_cal.to_ical())

