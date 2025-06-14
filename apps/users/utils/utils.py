from django.core.mail import send_mail
from apps.users.models import User, OTPCode
from django.utils import timezone
from datetime import timedelta
import random
import string


def generate_otp():
    return ''.join(random.choices(string.digits, k=6))  # OTP de 6 dígitos


def send_otp_email(user, code):
    subject = "Verificación de correo electrónico"
    message = f"Tu código de verificación es: {code}. Expira en 10 minutos."
    from_email = "tu-correo@dominio.com"
    recipient_list = [user.email]
    
    send_mail(subject, message, from_email, recipient_list)


def create_otp(user):
    otp_instance = OTPCode.objects.create(
        user=user,
        code=generate_otp(),
        otp_type="email",
        expires_at=timezone.now() + timedelta(hours=24)
    )
    return otp_instance  # Retorna la instancia de OTP si necesitas usarla