import os
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_POLL_STRATEGY"] = "poll"
import google.generativeai as genai
from flask.cli import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY,transport="rest")

def get_gemini_response(prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt)
    return response.text


# Test the function
if __name__ == "__main__":
    print(get_gemini_response("What is your refund policy?"))