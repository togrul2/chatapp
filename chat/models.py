from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Friendship(models.Model):
    sender = models.ForeignKey(User, related_name='friends_received', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='friends_sent', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_friendship(cls, user1: User, user2: User):
        return cls.objects.filter(Q(sender=user1, receiver=user2) | Q(sender=user2, receiver=user1)).first()

    def __str__(self):
        return f'friendship: {self.sender} - {self.receiver}'


class Chat(models.Model):
    friendship = models.OneToOneField(Friendship, on_delete=models.CASCADE, related_name='chat')

    def __str__(self):
        return f'chat: {self.friendship.sender} - {self.friendship.receiver}'


class Message(models.Model):
    class Meta:
        ordering = 'created_at',

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_send', on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.receiver}: {self.text}'
