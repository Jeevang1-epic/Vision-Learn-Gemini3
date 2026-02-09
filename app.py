import streamlit as st
import google.generativeai as genai #make sure it is pip installed through terminal 
from PIL import Image, ImageGrab
from gtts import gTTS 
import os
import time

# I am pasting my API Key here so the app can talk to Google servers
API_KEY = "api_key_goes_here" #api is important

# I am configuring the model to use the Gemini 3 Flash version
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')

# I am setting up the web page title and layout
st.set_page_config(page_title="Vision-Learn", layout="wide")

st.title("Vision-Learn: Real-Time AI Tutor")
st.write("G1 Personal Assistant")

# I am creating a sidebar for settings so I can toggle audio
with st.sidebar:
    st.header("Settings")
    # I am making a checkbox to turn the voice ON or OFF
    enable_audio = st.checkbox("Enable Audio Voice", value=True)

# I am creating two tabs: one for the webcam and one for screen sharing
tab1, tab2 = st.tabs(["Camera View", "Screen View"])

# --- TAB 1: WEBCAM LOGIC ---
with tab1:
    st.write("Show me a math problem or handwritten notes.")
    
    # I am creating the camera input widget here
    picture = st.camera_input("Take a picture")

    if picture:
        # I am showing a loading spinner while Gemini thinks
        with st.spinner("Analyzing..."):
            # I am opening the image file from the camera
            img = Image.open(picture)
            
            # I am sending the image to Gemini with a prompt to act like a tutor
            response = model.generate_content([
                "You are a tutor. Explain this solution. If it is math, solve it. If it is a diagram, explain it.", 
                img
            ])
            
            # I am displaying the text answer on the screen
            st.subheader("Explanation")
            st.write(response.text)
            
            # I am checking if audio is enabled, then generating speech
            if enable_audio:
                try:
                    # I am converting the text response to an MP3 file
                    tts = gTTS(text=response.text, lang='en', slow=False)
                    tts.save("response_cam.mp3")
                    # I am playing the audio file
                    st.audio("response_cam.mp3")
                except:
                    st.error("Audio error")

# --- TAB 2: SCREEN SHARE LOGIC ---
with tab2:
    st.write("Analyze code errors or documents directly from my screen.")
    
    # I am creating two columns to organize the layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # I am creating a button to trigger the screen capture
        if st.button("Capture My Screen"):
            # I am waiting 2 seconds so I have time to switch to my code window
            with st.spinner("Wait 2 seconds... switch windows now!"):
                time.sleep(2)
                
                # I am taking a screenshot of my entire screen
                screenshot = ImageGrab.grab()
                
                # I am showing the screenshot in the app so I know what it captured
                st.image(screenshot, caption="Captured Screen", use_container_width=True)
                
                # I am asking Gemini to look for bugs or summarize text
                with st.spinner("Gemini is reading the screen..."):
                    response = model.generate_content([
                        "Look at this screen. If it is code, find the bug and fix it. If it is text, summarize it.", 
                        screenshot
                    ])
                    
                    st.success("Done!")
                    st.subheader("Insight")
                    st.write(response.text)
                    
                    # I am generating the audio explanation for the screen analysis
                    if enable_audio:
                        try:
                            tts = gTTS(text=response.text, lang='en', slow=False)
                            tts.save("response_screen.mp3")
                            st.audio("response_screen.mp3")
                        except:

                            pass

