# Memory Slideshow Creator

A Flask web application that allows users to create slideshows from their photos and videos and automatically upload them to YouTube as private videos.

## Features

- Modern, responsive UI with drag-and-drop file upload
- Supports multiple image and video formats
- GPU-accelerated video processing (when available)
- Automatic YouTube upload with private access
- Secure file handling

## Setup

1. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Set up YouTube API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project
   - Enable the YouTube Data API v3
   - Create OAuth 2.0 credentials
   - Download the client secrets file and save it as `client_secrets.json` in the project root

3. Create a `.env` file in the project root with the following content:
```
FLASK_SECRET_KEY=your-secret-key
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=1073741824  # 1GB
```

4. Run the application:
```bash
python app.py
```

The application will be available at http://localhost:5000

## Usage

1. Open the application in your web browser
2. Drag and drop or select your media files
3. Click "Create Slideshow" to process the files
4. Wait for the processing and upload to complete
5. Access your private video using the provided YouTube link
