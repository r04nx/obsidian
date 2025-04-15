#!/usr/bin/env python3
"""
YouTube Video Uploader

This script demonstrates how to authenticate with OAuth 2.0 and upload videos to YouTube
using the YouTube Data API v3.

Prerequisites:
1. Create a Google Cloud project: https://console.cloud.google.com/
2. Enable the YouTube Data API v3
3. Create OAuth 2.0 credentials (OAuth client ID)
4. Download the client secrets JSON file and save it as 'client_secrets.json'
   in the same directory as this script

Required packages:
- google-api-python-client
- google-auth-oauthlib
- google-auth-httplib2

Install them in a virtual environment:
$ python -m venv youtube_env
$ source youtube_env/bin/activate
$ pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
"""

import os
import argparse
import http.client
import httplib2
import random
import time
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Cloud Console at https://console.cloud.google.com/.
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Maximum number of retries for HTTP errors
MAX_RETRIES = 10
# Initial backoff time in seconds
RETRIABLE_BACKOFF = 1

# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
                        http.client.IncompleteRead, http.client.ImproperConnectionState,
                        http.client.CannotSendRequest, http.client.CannotSendHeader,
                        http.client.ResponseNotReady, http.client.BadStatusLine)

# Sometimes the server may return a HTTP error
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]


def get_authenticated_service():
    """
    Authenticates with OAuth 2.0 and returns the YouTube API service.
    
    Handles token caching so users only need to authenticate once.
    
    Returns:
        A YouTube API service object.
    """
    credentials = None
    
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists('token.json'):
        try:
            credentials = Credentials.from_authorized_user_info(
                json.loads(open('token.json', 'r').read()), SCOPES)
        except Exception as e:
            print(f"Error loading credentials: {e}")
    
    # If there are no valid credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
                credentials = None
        
        if not credentials:
            try:
                if not os.path.exists(CLIENT_SECRETS_FILE):
                    print(f"Error: {CLIENT_SECRETS_FILE} not found.")
                    print("Please download OAuth 2.0 credentials from Google Cloud Console")
                    print("and save them as 'client_secrets.json' in the current directory.")
                    return None
                
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
                credentials = flow.run_local_server(port=8080)
                
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(credentials.to_json())
            except Exception as e:
                print(f"Error during authentication flow: {e}")
                return None
    
    try:
        return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    except Exception as e:
        print(f"Error building service: {e}")
        return None


def upload_video(youtube, options):
    """
    Uploads a video to YouTube with the specified options.
    
    Args:
        youtube: Authenticated YouTube API service object
        options: Dictionary containing video metadata and file path
        
    Returns:
        YouTube video ID if successful, None otherwise
    """
    tags = None
    if options.get('keywords'):
        tags = options['keywords'].split(',')
    
    # Create the video metadata
    body = {
        'snippet': {
            'title': options['title'],
            'description': options['description'],
            'tags': tags,
            'categoryId': options.get('category', '22')  # 22 = People & Blogs
        },
        'status': {
            'privacyStatus': options['privacy_status'],
            'selfDeclaredMadeForKids': False
        }
    }
    
    # Call the API's videos.insert method to create and upload the video
    video_path = options['file']
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return None
    
    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(video_path, chunksize=-1, resumable=True)
    )
    
    video_id = resumable_upload(insert_request)
    return video_id


def resumable_upload(insert_request):
    """
    Implements resumable upload with retries.
    
    Args:
        insert_request: A YouTube API videos.insert request
        
    Returns:
        YouTube video ID if successful, None otherwise
    """
    response = None
    error = None
    retry = 0
    
    print("Uploading file...")
    
    while response is None:
        try:
            print("Uploading file...")
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print(f"Video id '{response['id']}' was successfully uploaded.")
                    return response['id']
                else:
                    print(f"The upload failed with an unexpected response: {response}")
                    return None
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occurred: {e}"
        
        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                print("No longer attempting to retry.")
                return None
            
            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print(f"Sleeping {sleep_seconds} seconds and then retrying...")
            time.sleep(sleep_seconds)
    
    return None


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Upload a video to YouTube.')
    parser.add_argument('--file', required=True, help='Video file to upload')
    parser.add_argument('--title', default='Test Title', help='Video title')
    parser.add_argument('--description', default='Test Description', help='Video description')
    parser.add_argument('--keywords', default='', help='Video keywords, comma separated')
    parser.add_argument('--category', default='22', help='Numeric video category. See https://developers.google.com/youtube/v3/docs/videoCategories/list')
    parser.add_argument('--privacy-status', default='private',
                        choices=['public', 'private', 'unlisted'],
                        help='Video privacy status')
    return parser.parse_args()


def main():
    """Main function to run the script."""
    # Parse command line arguments
    args = parse_args()
    
    print("YouTube Video Uploader")
    print("======================")
    print(f"File: {args.file}")
    print(f"Title: {args.title}")
    print(f"Description: {args.description}")
    print(f"Privacy Status: {args.privacy_status}")
    print()
    
    # Get authenticated service
    youtube = get_authenticated_service()
    if not youtube:
        print("Failed to create YouTube service. Make sure you have valid credentials.")
        return
    
    try:
        # Convert args namespace to a dictionary
        options = {
            'file': args.file,
            'title': args.title,
            'description': args.description,
            'keywords': args.keywords,
            'category': args.category,
            'privacy_status': args.privacy_status
        }
        
        # Upload the video
        video_id = upload_video(youtube, options)
        
        if video_id:
            print(f"Upload successful! Video ID: {video_id}")
            print(f"Video URL: https://www.youtube.com/watch?v={video_id}")
        else:
            print("Upload failed.")
    
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

