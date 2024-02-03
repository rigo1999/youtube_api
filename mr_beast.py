from googleapiclient.discovery import build

#"Youtube Data API key
api_key = "AIzaSyCfjFkEdKqt7jBalDapJaILBzvq6hbAbr4"
#channel id 
channel_id = "UCRFjxLRW-j7_RSc0pm3clCw"
# Rchannel username
channel_username = "woanajoseph"

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Retrieve the channel ID for the specified username
channel_request = youtube.channels().list(part='id', forUsername=channel_username)
channel_response = channel_request.execute()
print(channel_response)
print()
# Use the channel ID to fetch channel data
channel_data_request = youtube.channels().list(
part='snippet,contentDetails,statistics',
id=channel_id)
channel_data_response = channel_data_request.execute()
print(channel_data_response)


