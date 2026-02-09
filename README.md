# Vision-Learn: Real-Time AI Tutor

**[CLICK HERE FOR LIVE DEMO](https://vision-learn-gemini3-shi88gzkagkmlwmsozzxvf.streamlit.app)**

A real-time AI assistant built for the Google Gemini 3 Hackathon. This application uses the Gemini 3 Flash model to analyze visual inputs (webcam or screen) and acts as a personal tutor, providing voice explanations for math problems, code errors, and diagrams.

## Features

- **Camera View:** Analyzes handwritten notes and diagrams via webcam.
- **Screen View:** Captures and debugs code or summarizes documents directly from your screen.
- **Voice Feedback:** Uses Text-to-Speech to explain solutions out loud.
- **Smart Memory:** Caches responses to prevent overuse of the API quota.

## Tech Stack

- Python 3.14
- Google Gemini 3 API (gemini-3-flash-preview)
- Streamlit (Web UI)
- gTTS (Google Text-to-Speech)
- Pillow (Image Processing)

## Installation (Local)

1. Clone the repository:
   git clone https://github.com/Jeevang1-epic/Vision-Learn-Gemini3.git
   cd Vision-Learn-Gemini3

2. Install dependencies:
   pip install -r requirements.txt

3. Configure API Key:
   Open app.py and paste your Google Gemini API key into the API_KEY variable.

## Usage

Run the application using the following command:

python -m streamlit run app.py
