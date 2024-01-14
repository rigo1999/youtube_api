from googleapiclient.discovery import build
api_key = "AIzaSyAORUA4JPMmdusT6svNYOf3AuGQJFX-diA"

youtube = build('youtube', 'v3', developerKey = api_key)
request = youtube.channels().list(part='statistics', forUsername='woanajoseph')

response = request.execute()

print(response)
