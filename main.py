import smtplib
import threading
from tkinter import Tk, Label, Entry, Text, Button, END
from email.mime.text import MIMEText

def send_email_thread():
    threading.Thread(target=send_email).start()

def send_email():
    sender_email = sender_entry.get()
    receiver_email = receiver_entry.get()
    password = password_entry.get()

    body = body_text.get("1.0", END)

    message = MIMEText(body)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject_entry.get()

    try:
        print("creating server")
        with smtplib.SMTP("smtp-mail.outlook.com", smtplib.SMTP_PORT) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)
            status_label.config(text="Email sent successfully!", fg="green")
    except smtplib.SMTPAuthenticationError as e:
        status_label.config(text="Authentication failed. Check your email and password.", fg="red")
        print(f"Authentication error: {e}")
    except smtplib.SMTPConnectError as e:
        status_label.config(text="Failed to connect to the server. Check your network.", fg="red")
        print(f"Connection error: {e}")
    except smtplib.SMTPServerDisconnected as e:
        status_label.config(text="Server unexpectedly disconnected. Try again later.", fg="red")
        print(f"Server disconnected: {e}")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
        print(f"Failed to send email: {e}")

root = Tk()
root.title("Email Sender")

sender_label = Label(root, text="Sender Email:")
sender_label.grid(row=0, column=0)
sender_entry = Entry(root)
sender_entry.grid(row=0, column=1)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

receiver_label = Label(root, text="Receiver Email:")
receiver_label.grid(row=2, column=0)
receiver_entry = Entry(root)
receiver_entry.grid(row=2, column=1)

subject_label = Label(root, text="Subject:")
subject_label.grid(row=3, column=0)
subject_entry = Entry(root)
subject_entry.grid(row=3, column=1)

body_label = Label(root, text="Body:")
body_label.grid(row=4, column=0)
body_text = Text(root, height=10, width=30)
body_text.grid(row=4, column=1)

send_button = Button(root, text="Send Email", command=send_email_thread)
send_button.grid(row=5, column=1)

status_label = Label(root, text="")
status_label.grid(row=6, column=0, columnspan=2)

root.mainloop()