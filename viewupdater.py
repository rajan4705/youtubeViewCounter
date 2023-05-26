# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import google_auth_oauthlib.flow 
import googleapiclient.discovery 
import googleapiclient.errors
import json
from time import sleep

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

ID_Video = "L1vOfCmRZ3c"
authfile = "./client_secret_367904571290-shfdpnh9i76t5tls5vjlgre0acg312eb.apps.googleusercontent.com.json"

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = authfile
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)
    
    
    while(True):
        try:

            # Now you can use the 'youtube' object to make API requests
            request = youtube.videos().list(
            part="snippet,statistics",
            id=ID_Video
            )
            response = request.execute()

            item = response["items"][0]
          

            vid_snippet = item["snippet"]
            titleName = str(item["snippet"]["title"])
            viewcount = str(item["statistics"]["viewCount"])

            print("Views: " + viewcount)
            print("title: "+titleName)

            #print(json.dumps(response, indent=4, sort_keys=True))
            
            #to actually update the title

            if(viewcount not in titleName):
                title_upd = "Cringe" + " | " + "This has " + viewcount + " views!"
                vid_snippet["title"] = title_upd

                request = youtube.videos().update(
                part="snippet",
                body={
                    "id": ID_Video,
                    "snippet": vid_snippet
                }
                )
                response = request.execute()
            
                print("Worked!")
                #so to not spam the api
                sleep(600)
            else:
                print("Already updated! No changes made.")

        except:
            print("Error! Trying again...")
        #so to not spam the api    
        sleep(60)    
            



          

if __name__ == "__main__":
    main()
