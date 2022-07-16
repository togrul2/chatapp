import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from chat.models import Friendship, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.user_id = self._get_chat_id(self.user.id)
        await self.channel_layer.group_add(self.user_id, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.user_id, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_parsed = json.loads(text_data)
        receiver_id = text_data_parsed['receiver_id']
        message = {
            'message': text_data_parsed['message'],
            'sender_id': text_data_parsed['sender_id'],
            'receiver_id': text_data_parsed['receiver_id'],
        }
        message_obj = await self._create_message(message)
        message['created_at'] = message_obj.created_at.isoformat()

        await self.channel_layer.group_send(self._get_chat_id(receiver_id), {
            'type': 'chat_message',
            **message
        })

    async def chat_message(self, event):
        message = {
            'message': event['message'],
            'sender_id': event['sender_id'],
            'receiver_id': event['receiver_id'],
            'created_at': event['created_at']
        }

        await self.send(text_data=json.dumps(message))

    @staticmethod
    def _get_chat_id(user_id):
        return f"user_chat_{user_id}"

    @database_sync_to_async
    def _create_message(self, message):
        sender = User.objects.get(id=message['sender_id'])
        receiver = User.objects.get(id=message['receiver_id'])
        return Message.objects.create(chat=Friendship.get_friendship(sender, receiver).chat,
                                      text=message['message'],
                                      sender=sender,
                                      receiver=receiver)
