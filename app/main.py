from fastapi import FastAPI

app = FastAPI()

from .routers import players, events



app.include_router(players.router)
app.include_router(events.router)
