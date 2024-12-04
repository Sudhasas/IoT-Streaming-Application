import asyncio
import websockets

async def dashboard(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")  # Display received messages

# Example usage: Run WebSocket server
if __name__ == "__main__":
    start_server = websockets.serve(dashboard, "localhost", 6789)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
