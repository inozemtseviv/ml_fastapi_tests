from fastapi import APIRouter


def get_root_router():
    router = APIRouter()

    @router.get("/")
    def root():
        return {"message": "Hello World"}

    return router
