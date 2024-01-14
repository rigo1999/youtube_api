from googleapiclient.discovery import build
api_key = "AIzaSyCfjFkEdKqt7jBalDapJaILBzvq6hbAbr4"

youtube = build('youtube', 'v3', developerKey = api_key)

request = youtube.channels().list(part='contentDetails', forUsername='DanKoeTalks')
response = request.execute()

print(response)
