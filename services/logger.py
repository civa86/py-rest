import logging
from datetime import datetime
import config

LOG_LEVEL = config.get('LOG_LEVEL').upper()

log = logging.getLogger('werkzeug')


def set_log_level():
    # Set Logging Level
    logging_level = None
    try:
        logging_level = getattr(logging, LOG_LEVEL)
    except:
        log.error('Logging level "' + LOG_LEVEL + '" not valid!')

    if logging_level is not None:
        log.setLevel(logging_level)


def info(msg):
    log.info(msg)


def warn(msg):
    log.warning(msg)


def error(msg):
    log.error(msg)


def print_timing(time_start, msg):
    time_end = datetime.now()
    warn("[TIME] " + msg + ": " +
         '{0:.10f}'.format((time_end - time_start).total_seconds()))
