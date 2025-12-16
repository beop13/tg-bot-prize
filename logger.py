import logging
import sys

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

def setup_logging(level: int = logging.INFO) -> None:
    """
    Настраивает глобальный логгер приложения
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # чтобы не дублировать хендлеры при повторном вызове
    if root_logger.handlers:
        return

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    handler.flush = sys.stdout.flush 

    root_logger.addHandler(handler)
