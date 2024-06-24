# this program takes authors name from newsapi then searchs them in spotify 
# that give the preview
# in console the authors name and preview url is provided
import os, json, requests
from requests.auth import HTTPBasicAuth 

i=0
clientID = os.environ['clientID']
clientSecret = os.environ['clientSecret']
newsKey = os.environ['news_api_key']

# news api start
country = "us" # change country here
news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"
news_respons = requests.get(news_url)
news_data = news_respons.json()
# news api stop
# spotify api start (search querry)
spotify_url = "https://accounts.spotify.com/api/token"
sp_grant_data = {"grant_type": "client_credentials"}
spotify_auth = HTTPBasicAuth(clientID, clientSecret)

spotify_respons = requests.post(url=spotify_url, data=sp_grant_data, auth=spotify_auth)
# print(spotify_respons)
access_token = spotify_respons.json()['access_token']
# print(json.dumps(news_data, indent=2))

for article in news_data['articles']:
  i += 1
  author = article['author']
  print(author)
  # print(article['url'])

  # finding artist
  spotify_search_url = "https://api.spotify.com/v1/search"
  header = {"Authorization": f"Bearer {access_token}"}
  spotify_search = f"?query=artists%3A{author}&type=track&locale=en-US%2Cen%3Bq%3D0.9%2Cbn%3Bq%3D0.8&offset=0&limit=20"
  spotify_full_url = f"{spotify_search_url}{spotify_search}"
  
  spotify_respons = requests.get(spotify_full_url, headers=header)
  # spotify api stop
  spotify_data = spotify_respons.json()
  # print(spotify_data)
  track = spotify_data['tracks']['items']
  # print(track)
  for track in spotify_data['tracks']['items']:
    print(track['preview_url'], end="\n\n")
    break
  
  if i==5: break
    




