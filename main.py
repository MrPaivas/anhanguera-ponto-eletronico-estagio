from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session


from endpoints import users, face_verify




app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
app.include_router(face_verify.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="10.151.22.132", port=8000)