import smtplib

EMAIL = "sb7160@srmist.edu.in"
PASSWORD = "BabaMaaGagan@1234"  # Use your actual Gmail password

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    print("✅ Email login successful!")
except smtplib.SMTPAuthenticationError:
    print("❌ Email login failed! Check your credentials.")


