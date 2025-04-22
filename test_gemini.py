from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

print(f"API Key found: {'Yes' if api_key else 'No'}")
print(f"API Key starts with: {api_key[:10] if api_key else 'None'}")

try:
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Create and test the model
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content('Say hello!')
    print("\nGemini Response:", response.text)
    
except Exception as e:
    print(f"\nError occurred: {str(e)}") 