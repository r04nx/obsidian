import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.http
import logging

logger = logging.getLogger(__name__)

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT_SECRETS_FILE = 'client_secret.json'

def get_authenticated_service(force_new_auth=False):
    """Get an authenticated YouTube API service instance."""
    # Check if client secrets file exists
    if not os.path.exists(CLIENT_SECRETS_FILE):
        logger.error(f"Client secrets file '{CLIENT_SECRETS_FILE}' not found.")
        raise FileNotFoundError(f"Client secrets file '{CLIENT_SECRETS_FILE}' not found. Please download it from the Google API Console.")
    
    credentials = None
    
    # Only check for existing token if not forcing new auth
    if not force_new_auth and os.path.exists('token.json'):
        try:
            with open('token.json', 'r') as token_file:
                token_info = token_file.read()
                credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(
                    info=eval(token_info))
            logger.info("Using existing YouTube credentials from token.json")
        except Exception as e:
            logger.error(f"Error loading token.json: {str(e)}")
            credentials = None
    
    # If credentials are invalid, don't exist, or force_new_auth is True
    if not credentials or not credentials.valid or force_new_auth:
        try:
            # Remove existing token.json if forcing new auth
            if force_new_auth and os.path.exists('token.json'):
                os.remove('token.json')
                logger.info("Removed existing token.json for new authentication")
            
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=8080)
            
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(str(credentials.to_json()))
            logger.info("New YouTube credentials saved to token.json")
        except Exception as e:
            logger.error(f"Error during OAuth flow: {str(e)}")
            raise
    
    try:
        service = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials)
        logger.info("YouTube API service created successfully")
        return service
    except Exception as e:
        logger.error(f"Error building YouTube API service: {str(e)}")
        raise

def format_timestamps(timestamps):
    """Format timestamps for YouTube description"""
    if not timestamps:
        return ""
    
    formatted = "\n\n📋 Timestamps:\n"
    for ts in timestamps:
        minutes = int(ts['time'] // 60)
        seconds = int(ts['time'] % 60)
        name = ts['name']
        time_str = f"{minutes}:{seconds:02d}"
        
        # Add emoji based on type
        if ts['type'] == 'video':
            emoji = "🎬"
        else:
            emoji = "🖼️"
        
        formatted += f"{emoji} {time_str} - {name}\n"
    
    return formatted

def upload_to_youtube(file_path, title, description, privacy_status='private', tags=None, timestamps=None):
    """Upload a video to YouTube."""
    try:
        if not os.path.exists(file_path):
            error_msg = f"Video file not found: {file_path}"
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)
        
        logger.info(f"Starting YouTube upload for: {file_path}")
        logger.info(f"Title: {title}, Privacy: {privacy_status}")
        
        youtube = get_authenticated_service()
        
        # Enhance description with timestamps if available
        if timestamps:
            timestamp_text = format_timestamps(timestamps)
            description += timestamp_text
            logger.info(f"Added {len(timestamps)} timestamps to description")
        
        # Add a signature to the description
        description += "\n\n🔄 Created with Memento - Memory Slideshow Creator"
        
        # Default tags if none provided
        if tags is None:
            tags = ['memories', 'slideshow', 'memento']
        
        # Define the video metadata
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': '22'  # People & Blogs category
            },
            'status': {
                'privacyStatus': privacy_status,
                'selfDeclaredMadeForKids': False
            }
        }
        
        # Call the API's videos.insert method to create and upload the video
        logger.info(f"Creating YouTube insert request")
        media = googleapiclient.http.MediaFileUpload(
            file_path, 
            chunksize=1024*1024, 
            resumable=True
        )
        
        insert_request = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )
        
        # Execute the upload with progress tracking
        logger.info("Executing YouTube upload request")
        response = None
        while response is None:
            status, response = insert_request.next_chunk()
            if status:
                logger.info(f"Upload progress: {int(status.progress() * 100)}%")
        
        video_id = response['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        logger.info(f"Video uploaded successfully: {video_url}")
        return video_id
    
    except Exception as e:
        logger.error(f"Error uploading to YouTube: {str(e)}")
        raise
