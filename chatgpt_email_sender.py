
# Zapisz rozmowę do pliku tekstowego
def save_conversation_to_file(conversation, filename="conversation.txt"):
    with open(filename, 'w') as file:
        for line in conversation:
            file.write(line + "\n")

# Wysyłanie emaila
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient_email, sender_email, sender_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Zintegrowana funkcja do zapisu rozmowy i wysłania e-maila
def send_conversation_via_email(conversation, recipient_email, sender_email, sender_password):
    filename = "conversation.txt"
    save_conversation_to_file(conversation, filename)

    with open(filename, 'r') as file:
        conversation_text = file.read()

    send_email("ChatGPT Conversation", conversation_text, recipient_email, sender_email, sender_password)
