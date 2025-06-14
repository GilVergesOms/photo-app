from django.core.mail import send_mail

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'gil.verges21@gmail.com'
EMAIL_HOST_PASSWORD = 'tnyo cnwo prpb orgwa'

def send_otp_email(user, code):
    subject = "Verificación de correo electrónico"
    message = f"Tu código de verificación es: {code}. Expira en 24 horas."
    
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,  # Remitente
        [user.email],  # Destinatario
        fail_silently=False,
        auth_user=EMAIL_HOST_USER,  # Autenticación
        auth_password=EMAIL_HOST_PASSWORD
    )