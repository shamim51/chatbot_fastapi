from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.functions.genResponse import genResponse



app = FastAPI()

# Configure CORS to allow cross-origin requests
origins = ["*"]  # Update this list to restrict access to specific domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str


@app.post("/predict")
async def predict(message: Message):
    try:
        print(message.message)
        #print(Message)
        #response = {"answer": f"This is a dummy response to: '{message.message}'"}
        response = genResponse(message.message)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
