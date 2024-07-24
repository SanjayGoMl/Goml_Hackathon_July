from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router)


from fastapi import FastAPI
from pyngrok import ngrok
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
# Import your routes
from routes.route import router

app = FastAPI()
# print(os.getenv("NGROK_AUTHTOKEN"))

# Include your router
app.include_router(router)

if __name__ == "__main__":
    # Authenticate with ngrok using your authtoken
    ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))

    # Create a public URL for the FastAPI app
    public_url = ngrok.connect(8000)
    print("ngrok tunnel \"{}\" -> \"http://127.0.0.1:8000\"")
    print(public_url)

    # Start the FastAPI app with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
