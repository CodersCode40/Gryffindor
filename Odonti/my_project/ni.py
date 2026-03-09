from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if "hello" in incoming_msg:
        msg.body("Hello! Welcome to ODONTI Media Bot 🤖")

    elif "price" in incoming_msg:
        msg.body("Our charges are very affordable.")

    elif "location" in incoming_msg:
        msg.body("We are located at Kokofu.")

    elif "time" in incoming_msg:
        msg.body("Our office opens at 8:00 AM and closes at 9:00 PM.")

    else:
        msg.body("Sorry, I didn't understand that message.")

    return str(response)

if __name__ == "__main__":
    app.run()