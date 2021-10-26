from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI
from app.api.ui_routes import router as ui_routes
from app.api.data_routes import router as data_routes
import logging
logging.config.fileConfig("./app/logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

if os.getenv("BYPASS_CORS", "false").lower() == "true":
    logger.warn("[Potential security lapse] Bypass Cross origin resource sharing option is set to TRUE.. Please check if this can be turned OFF.")
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=["*"],
        allow_origin_regex='https?://.*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def startup():
    print("SYSTEM STARTED")


app.include_router(ui_routes)

app.include_router(data_routes, prefix="/data")
