from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def authenticate():
    """Authenticate and generate token.json"""
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES, redirect_uri="http://localhost:8080/"
    )
    creds = flow.run_local_server(port=8080)  # Match the registered redirect URI

    with open("token.json", "w") as token_file:
        token_file.write(creds.to_json())

    print("Authentication successful! token.json generated.")

if __name__ == "__main__":
    authenticate()
