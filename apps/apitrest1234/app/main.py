import logging
import sys
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("app")

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    logger.info("health check")
    return {"status": "ok"}
