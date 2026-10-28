import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

filename = "tasks.json"

try:
    with open(filename, "r", encoding="utf-8") as f:
        tasks = json.load(f)
except FileNotFoundError:
    logger.error(f"File not found: {filename}")
except json.JSONDecodeError:
    logger.error(f"Invalid JSON in {filename}")
else:
    for task in tasks:
        status = "done" if task["done"] else "not done"
        logger.info(f"{task['name']}: {status}")