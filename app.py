from flask import Flask, request, jsonify, render_template
from twilio.rest import Client
from twilio.base.exceptions import TwilioException

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    message_body = request.form.get('message')

    # Your Twilio account SID and auth token
    account_sid = 'AC923cc1d4f47e95e93c2c111da4cafdf8'
    auth_token = '233b35ef14cfa8bf8aa26d1695c128ce'

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # List of recipients
    recipients = [
        ("Elyi Pierre", "3473582131"),
        ("Eurial McFarlane", "3472650138"),
        ("Anthony Scandiffio", "9144335481"),
        ("Michael Sloggatt", "6315219344"),
        # Add the rest of the recipients here
    ]

    try:
        for name, phone_number in recipients:
            client.messages.create(
                body=message_body,
                from_='+18447542226',
                to=f'+1{phone_number}'
            )

        return jsonify({"result": "success"})

    except TwilioException as e:
        return jsonify({"result": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
