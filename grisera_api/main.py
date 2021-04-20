from fastapi import FastAPI
from hateoas import get_links
from participant.participant_router import router as participant_router
from experiment.experiment_router import router as experiment_router

app = FastAPI()

app.include_router(participant_router)
app.include_router(experiment_router)


@app.get("/", tags=["root"])
async def root():
    """
    Return home page of api
    """
    response = {"title": "GRISERA API"}
    response.update({'links': get_links(app)})
    return response
