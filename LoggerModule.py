import logging
import logging.handlers



class MyLogger():

    logger=logging.getLogger('Admin')
    logger.setLevel(logging.DEBUG)

    handler=logging.handlers.RotatingFileHandler(filename='demo.log',maxBytes=5*1024*1024,backupCount=10)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(thread)d | %(message)s'
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)



