from fastapi import FastAPI
import uvicorn

from Routers.Main_Router import router


app = FastAPI()

app.include_router(router)
