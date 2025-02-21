import asyncio
from flask import Flask,request,jsonify
from telegram_service import start_bot
from calendar_service import create_calendar_event
from gemini_ai import get_gemini_response
from gmail_service import send_email

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return jsonify({"message":"AI-Powered Customer Support Agent is running!!"})
@app.route("/ask",methods=["POST"])
def ask():
    data=request.json
    query=data.get("query")

    if not query:
        return jsonify({"message":"Please enter your query"}),400
    response=get_gemini_response(query)
    return jsonify({"response":response})

@app.route("/send-email",methods=["POST"])
def send_email_route():
    data=request.json
    to=data.get("to")
    subject=data.get("subject")
    message=data.get("message")

    if not all([to,subject,message]):
        return jsonify({"error": "Missing fields"}), 400
    send_email(to,subject,message)
    return jsonify({"message":"Email sent"})

@app.route("/schedule-followup",methods=["POST"])
def schedule_followup():
    try:
        data = request.json
        summary = data.get("summary", "Customer Follow-up")
        description = data.get("description", "Follow up on a customer query")
        start_time = data.get("start_time")
        end_time = data.get("end_time")
        email = data.get("email")

        if not all([start_time, end_time, email]):
            return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    event_link = create_calendar_event(summary, description, start_time, end_time, email)
    return jsonify({"message": "Follow-up scheduled", "event_link": event_link})


@app.route("/start-telegram-bot", methods=["GET"])
def start_telegram():
    """API to start the Telegram bot."""
    loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)      # Set the new loop as the current one
    loop.run_until_complete(start_bot())  # Run the bot
    return jsonify({"message": "Telegram bot started"}), 200




if __name__ == "__main__":
    app.run(debug=True)
