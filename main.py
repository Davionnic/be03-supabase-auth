import os
from dotenv import load_dotenv
from fastapi import FastAPI
from supabase import create_client, Client
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI(
    title="FlyRank BE-03 Auth API",
    description="Authentication system using FastAPI and Supabase",
    version="1.0.0"
)

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

@app.get("/")
async def root():
    return {"message": "FlyRank BE-03 Auth API is running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)