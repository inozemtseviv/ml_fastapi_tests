from fastapi import FastAPI
from transformers import pipeline

from app.routes.root_router import get_root_router
from app.routes.predict_router import get_predict_router

classifier = pipeline("sentiment-analysis")

app = FastAPI()
app.include_router(get_root_router())
app.include_router(get_predict_router(classifier))
