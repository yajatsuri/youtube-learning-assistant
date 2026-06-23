import time
import logging

from fastapi import Request


logger = logging.getLogger(__name__)


async def logging_middleware(
    request: Request,
    call_next
):

    start_time = time.time()

    logger.info(
        f"{request.method} {request.url.path} | Started"
    )

    response = await call_next(
        request
    )

    duration = round(
        time.time() - start_time,
        2
    )

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"| Completed "
        f"| Status: {response.status_code} "
        f"| Duration: {duration}s"
    )

    return response
