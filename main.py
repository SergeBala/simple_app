from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Echo API", description="A simple echo service for learning deployment")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Echo Service</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
            }
            .input-group {
                margin: 20px 0;
            }
            input[type="text"] {
                width: 100%;
                padding: 12px;
                font-size: 16px;
                border: 2px solid #ddd;
                border-radius: 5px;
                box-sizing: border-box;
            }
            button {
                width: 100%;
                padding: 12px;
                font-size: 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 10px;
            }
            button:hover {
                background-color: #45a049;
            }
            .response {
                margin-top: 20px;
                padding: 15px;
                background-color: #e7f3fe;
                border-left: 4px solid #2196F3;
                border-radius: 5px;
                display: none;
            }
            .response.show {
                display: block;
            }
            .response-text {
                color: #333;
                word-wrap: break-word;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔊 Echo Service</h1>
            <p style="text-align: center; color: #666;">Enter a message and get it echoed back!</p>
            
            <div class="input-group">
                <input type="text" id="messageInput" placeholder="Type your message here..." />
                <button onclick="sendMessage()">Send Echo Request</button>
            </div>
            
            <div id="response" class="response">
                <strong>Response:</strong>
                <p class="response-text" id="responseText"></p>
            </div>
        </div>

        <script>
            async function sendMessage() {
                const message = document.getElementById('messageInput').value;
                
                if (!message.trim()) {
                    alert('Please enter a message!');
                    return;
                }
                
                try {
                    const response = await fetch(`/api/echo?message=${encodeURIComponent(message)}`);
                    const data = await response.json();
                    
                    document.getElementById('responseText').textContent = 
                        `Original: "${data.original_message}" | Echo: "${data.echo}" | Timestamp: ${data.timestamp}`;
                    document.getElementById('response').classList.add('show');
                } catch (error) {
                    alert('Error: ' + error.message);
                }
            }
            
            // Allow Enter key to submit
            document.getElementById('messageInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
        </script>
    </body>
    </html>
    """

@app.get("/api/echo")
async def echo(message: str = Query(..., description="The message to echo back")):
    """
    Echo endpoint that takes a message via query parameter and returns it back
    
    Example: /api/echo?message=Hello%20World
    """
    from datetime import datetime
    
    return {
        "original_message": message,
        "echo": message,
        "length": len(message),
        "timestamp": datetime.utcnow().isoformat(),
        "status": "success"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "service": "echo-api"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
