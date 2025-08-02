import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class GeminiChatbot:
    def __init__(self):
        # Configure Gemini
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Store chat sessions (in production, use proper session management)
        self.chat_sessions = {}
        
        print("🤖 Gemini Chatbot backend initialized!")
    
    def get_or_create_chat(self, session_id="default"):
        """Get existing chat session or create new one"""
        if session_id not in self.chat_sessions:
            self.chat_sessions[session_id] = self.model.start_chat(history=[])
        return self.chat_sessions[session_id]
    
    def send_message(self, message, session_id="default"):
        """Send a message and get response"""
        try:
            chat = self.get_or_create_chat(session_id)
            response = chat.send_message(message)
            return {"success": True, "response": response.text}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def clear_chat(self, session_id="default"):
        """Clear chat history for a session"""
        if session_id in self.chat_sessions:
            del self.chat_sessions[session_id]
        return {"success": True, "message": "Chat history cleared"}

# Initialize chatbot
chatbot = GeminiChatbot()

@app.route('/')
def index():
    """Serve the HTML page"""
    # Read the HTML file content
    try:
        with open('chatbot.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        return """
        <h1>Error: chatbot.html not found</h1>
        <p>Please make sure chatbot.html is in the same directory as this Python file.</p>
        """, 404

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not message:
            return jsonify({"success": False, "error": "Message cannot be empty"}), 400
        
        # Get response from Gemini
        result = chatbot.send_message(message, session_id)
        
        if result["success"]:
            return jsonify({
                "success": True,
                "response": result["response"]
            })
        else:
            return jsonify({
                "success": False,
                "error": result["error"]
            }), 500
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear():
    """Clear chat history"""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        
        result = chatbot.clear_chat(session_id)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Chatbot backend is running"})

if __name__ == "__main__":
    # Check if API key exists
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in .env file")
        print("Please create a .env file with your Gemini API key")
        exit(1)
    
    print("\n🚀 Starting Gemini Chatbot Web Server...")
    print("📝 Make sure chatbot.html is in the same directory")
    print("🌐 Open http://localhost:5000 in your browser")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)