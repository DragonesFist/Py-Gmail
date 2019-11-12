from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId="me").execute()
    list_ids = results['messages']
    # print(list_ids[1]['id'])
    
    list_messages=[]
    for i in range(len(list_ids)):
        temp = service.users().messages().get(userId="me", id=list_ids[i]['id']).execute()
        list_messages.append(temp['payload']['headers'])

    print(list_messages[0][0]['name'])
    list_from=[]
    for j in range(len(list_messages)):
        for k in range(len(list_messages[j])):
            if(list_messages[j][k]['name']=="From"):
                list_from.append(list_messages[j][k]['value'])


    
    print(list_from)
        



    
if __name__ == '__main__':
    main()