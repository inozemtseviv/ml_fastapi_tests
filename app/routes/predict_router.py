from fastapi import APIRouter

from app.models import Item


def get_predict_router(classifier):
    router = APIRouter()

    @router.post("/predict/")
    def predict(item: Item):
        return classifier(item.text)[0]

    return router
