import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
sio_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    # In a real app, you would authenticate the user here via token from environ
    # and add them to a specific room (e.g., their user ID room)

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

async def notify_user(user_id: str, message: str, notification_type: str):
    # Sends a message to a specific user (if they joined a room named after their user_id)
    await sio.emit("notification", {"message": message, "type": notification_type}, room=user_id)
