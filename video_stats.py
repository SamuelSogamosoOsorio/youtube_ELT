import requests
import json
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./.env")
API_KEY=os.getenv("API_KEY")


CHANNEL_HANDLER="MrBeast"



def get_playlist_id():
    
    try:
            
        url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLER}&key={API_KEY}"

        response = requests.get(url)
        data_extracted=response.json()

        channel_items= data_extracted['items'][0]
        channel_playlist_id=channel_items['contentDetails']['relatedPlaylists']['uploads']
        
        print(channel_playlist_id)
        
        return channel_playlist_id
    
    except requests.exceptions.RequestException as e:
        raise e
    

if __name__ == "__main__":
    get_playlist_id()

   
        


