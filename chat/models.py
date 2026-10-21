from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(blank=True, null=True, help_text="Texto del mensaje")
    
    # URL de Firebase para fotos enviadas por el chat
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text="Enlace de Firebase si envían foto")
    
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordenamos del más antiguo al más nuevo (como en WhatsApp)
        ordering = ['timestamp']

    def __str__(self):
        return f"De {self.sender.username} para {self.receiver.username} - {self.timestamp.strftime('%H:%M')}"