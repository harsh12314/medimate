from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Medicine
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send medicine reminder emails'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        upcoming_time = now + timedelta(minutes=30)

        medicines = Medicine.objects.filter(next_dose_time__range=(now, upcoming_time))

        for med in medicines:
            user = med.user
            email = user.email

            subject = f"⏰ Time to take your medicine: {med.name}"
            message = (
                f"Hi {user.username},\n\n"
                f"This is a reminder to take your medicine:\n"
                f"➡️ Name: {med.name}\n"
                f"➡️ Dosage: {med.dosage}\n"
                f"➡️ Frequency: {med.frequency}\n"
                f"➡️ Scheduled at: {med.next_dose_time.strftime('%Y-%m-%d %H:%M')}\n\n"
                "Stay healthy!\n- MediMate"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

        self.stdout.write(f"✅ Sent {medicines.count()} medicine reminder(s)")
