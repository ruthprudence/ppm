# app/utils/email_service.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

def send_maintenance_request(data):
    msg = MIMEMultipart()
    msg['Subject'] = f'Maintenance Request - Unit {data["unit"]} - {data["priority"]} Priority'
    
    body = f"""
    New Maintenance Request:
    
    Unit: {data['unit']}
    Priority: {data['priority']}
    Description: {data['description']}
    Contact: {data['contact']}
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Configure with your SMTP settings
    with smtplib.SMTP('smtp.dreamhost.com', 587) as server:
        server.starttls()
        server.login('your-email@domain.com', 'your-password')
        for recipient in current_app.config['MAIL_RECIPIENTS']:
            msg['To'] = recipient
            server.send_message(msg)
