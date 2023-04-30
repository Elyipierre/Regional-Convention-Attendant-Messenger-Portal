import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedTk
from twilio.rest import Client
from twilio.base.exceptions import TwilioException

# Function to send SMS
def send_sms():
    try:
        # Your Twilio account SID and auth token
        account_sid = 'AC923cc1d4f47e95e93c2c111da4cafdf8'
        auth_token = '233b35ef14cfa8bf8aa26d1695c128ce'

        # Initialize the Twilio client
        client = Client(account_sid, auth_token)

        # The SMS message to be sent
        message_body = message_text.get("1.0", tk.END).strip()

        # List of recipients
        recipients = [
            ("Elyi Pierre", "3473582131"),
            ("Eurial McFarlane", "3472650138"),
            ("Anthony Scandiffio", "9144335481"),
            ("Michael Sloggott", "6315219344"),
            # Add the rest of the recipients here
        ]

        progress_bar["maximum"] = len(recipients)
        progress_bar["value"] = 0

        # Send the SMS to each recipient
        for name, phone_number in recipients:
            client.messages.create(
                body=message_body,
                from_='+18447542226',
                to=f'+1{phone_number}'
            )
            progress_bar["value"] += 1
            root.update_idletasks()

        messagebox.showinfo("Success", "SMS sent successfully to all recipients")

    except TwilioException as e:
        messagebox.showerror("Error", f"Failed to send SMS. Error: {e}")

# Initialize the main window
root = ThemedTk(theme="arc")  # Choose the 'arc' theme for a modern look
root.title("Regional Convention Attendant Messenger")
root.geometry("550x600")

# Create a frame for the message input field
message_frame = ttk.Frame(root)
message_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Create the message input field
message_text = tk.Text(message_frame, wrap=tk.WORD)
message_text.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)

# Create a scrollbar for the message input field
scrollbar = ttk.Scrollbar(message_frame, orient=tk.VERTICAL, command=message_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_text["yscrollcommand"] = scrollbar.set

# Create the send button
send_button = ttk.Button(root, text="Send", command=send_sms)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
progress_bar.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

# Start the main loop
root.mainloop()
