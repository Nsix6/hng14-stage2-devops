import logging
import os
import signal
import time

import redis
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
QUEUE_NAME = os.getenv("QUEUE_NAME", "job")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

shutdown = False


def handle_shutdown(signum, frame):
    global shutdown
    shutdown = True
    logging.info("Shutdown signal received")


signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)


def process_job(job_id):
    try:
        logging.info(f"Processing job {job_id}")
        r.hset(
            f"job:{job_id}",
            mapping={"status": "processing", "started_at": int(time.time())},
        )

        time.sleep(2)

        r.hset(
            f"job:{job_id}",
            mapping={"status": "completed", "completed_at": int(time.time())},
        )

        logging.info(f"Completed job {job_id}")

    except Exception as e:
        logging.error(f"Job {job_id} failed: {str(e)}")
        r.hset(f"job:{job_id}", mapping={"status": "failed", "error": str(e)})


while not shutdown:
    try:
        job = r.brpop(QUEUE_NAME, timeout=5)
        if job:
            _, job_id = job
            process_job(job_id)
    except redis.exceptions.RedisError as e:
        logging.error(f"Redis error: {str(e)}")
        time.sleep(2)

logging.info("Worker shutting down cleanly")
