from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Message(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/predict")
async def predict(message: Message):
    try:
        print(message.message)
        #print(Message)
        response = {"answer": f"This is a dummy response to: '{message.message}'"}
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
