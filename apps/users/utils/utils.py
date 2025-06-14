from django.core.mail import send_mail
from apps.users.models import User, OTPCode
from django.utils import timezone
from datetime import timedelta
from apps.users.utils.smtpMail import *
import random
import string


def generate_otp():
    return ''.join(random.choices(string.digits, k=6))  # OTP de 6 dígitos



def create_otp(user):
    otpCode=generate_otp()
    otp_instance = OTPCode.objects.create(
        user=user,
        code = otpCode,
        otp_type="email",
        expires_at=timezone.now() + timedelta(hours=24)
    )
    send_otp_email(user, otpCode)  # 🔥 Envía el correo con el código OTP
    return otp_instance  # Retorna la instancia de OTP si necesitas usarla