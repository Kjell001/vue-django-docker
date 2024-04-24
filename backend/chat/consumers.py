import json
from datetime import datetime, timezone
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    GROUP_NAME = "chat"

    async def connect(self):
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.GROUP_NAME, self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.GROUP_NAME,
            {
                # Special 'type' key specifies consumer method to call
                "type": "chat_message",
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "user": data["user"],
                "content": data["content"],
            },
        )
    
    # Handle chat_message group event
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
