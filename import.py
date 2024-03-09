import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime
import pytz
from icalendar import Calendar

# Créez une fonction pour authentifier et obtenir le service Google Calendar
def authenticate_google_calendar():
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Si le fichier token.pickle n'existe pas, l'utilisateur doit s'authentifier
    if os.path.exists('credentials.json'):
        with open('credentials.json', 'rb') as token:
            creds = credentials.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            '/home/kitsensas/Desktop/Programming/python/calendar/credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('credentials.json', 'wb') as token:
            pickle.dump(creds, token)

    # Construire le service Google Calendar
    service = build('calendar', 'v3', credentials=creds)
    return service

# Fonction pour importer le fichier iCal dans Google Agenda
def import_ical_to_google_calendar(file_path, calendar_id='primary'):
    service = authenticate_google_calendar()

    # Charger le fichier iCal
    with open(file_path, 'rb') as file:
        cal = Calendar.from_ical(file.read())

    # Parcourir les événements du calendrier iCal
    for event in cal.walk('VEVENT'):
        event_summary = event.get('summary')
        event_description = event.get('description', '')
        start_time = event.get('dtstart').dt
        end_time = event.get('dtend').dt

        # Créer un événement dans Google Agenda
        event_body = {
            'summary': event_summary,
            'description': event_description,
            'start': {'dateTime': start_time.isoformat(), 'timeZone': 'UTC'},
            'end': {'dateTime': end_time.isoformat(), 'timeZone': 'UTC'},
        }

        # Ajouter l'événement au calendrier Google
        service.events().insert(calendarId=calendar_id, body=event_body).execute()

    print("Importation terminée avec succès!")

# Utilisation de la fonction pour importer le fichier iCal
import_ical_to_google_calendar('informations_cours.ical')



