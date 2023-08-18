from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.functions.genResponse import genResponse
from app.routers.query import router  # Import the router



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

#app.include_router(query)
app.include_router(router)  # Include the chatbot router with a prefix

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
