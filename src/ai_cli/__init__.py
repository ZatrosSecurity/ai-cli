__version__ = "0.3.7"

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

HOME = Path.home()

CONFIG_DIR = Path.home() / ".config/ai_cli"
LOG_DIR = CONFIG_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def init_logging(log_level: int = logging.INFO):
    log_format = "%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s"
    log_file = LOG_DIR / "ai_cli.log"
    fh = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 10, backupCount=7)
    logging.basicConfig(level=logging.WARNING, handlers=[fh], format=log_format)
    # set ai_cli logger level to INFO
    logging.getLogger("ai_cli").setLevel(level=log_level)
