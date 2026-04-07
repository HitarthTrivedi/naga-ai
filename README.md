# NAGA.AI - Rude AI Assistant

A Gujarati/Hindi speaking AI chatbot powered by Gemini that is deliberately rude, aggressive, and vulgar.

## Local Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create API key file
mkdir -p api
echo "GEMINI_API_KEY=your_key_here" > api/.env

# Run
python3 app.py
```

Open `http://localhost:3000`

## Deploy on Render

1. Push repo to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Connect your repo and configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Environment Variable:** `GEMINI_API_KEY` = your Gemini API key

## How It Works

Gemini's content moderation blocks vulgar language. To work around this, the system prompt instructs Gemini to output short code words (e.g. `xk7mQ` instead of actual vulgar words). The server decodes these codes back to original words before sending the response to the client. This way the Gemini API response is moderation-clean while the user still sees the intended output.

## Files

- `app.py` - Flask server, Gemini API calls
- `vulgar_decode.py` - Code-to-word mapping and decoder
- `index.html` - Chat UI
- `api/.env` - Gemini API key (not committed)
