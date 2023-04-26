from fastapi import FastAPI

app = FastAPI()

from .routers import players, events

# from .database import models
# from .database import engine

# models.Base.metadata.create_all(bind=engine)


app.include_router(players.router)
app.include_router(events.router)
