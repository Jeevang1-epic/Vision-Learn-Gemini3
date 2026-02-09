import google.generativeai as genai

# Setup
API_KEY = "api_key_goes_here"
genai.configure(api_key=API_KEY)

# List available models to find the right name for Gemini 3
print("Finding available models...")
for m in genai.list_models():
    if 'gemini' in m.name:
        print(m.name)

# Simple Test
try:
    # We will try to use the latest experimental model
    model = genai.GenerativeModel('gemini-3-flash-preview')
    response = model.generate_content("Hello, are you ready for the hackathon?")
    print("\nSUCCESS! Response from AI:")
    print(response.text)
except Exception as e:
    print("\nError:", e)