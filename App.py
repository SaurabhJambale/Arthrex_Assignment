
from LoggerModule import *

My_logger_obj=MyLogger()

def add (a,b):
    try:
        c=a+b
        My_logger_obj.logger.info(f'Adding {a} and {b}')

    except Exception as e:
        My_logger_obj.logger.exception(e)

def divide(a,b):
    try:
        c=a/b
        My_logger_obj.logger.info(f'Dividing {a} by {b}')
    except Exception as e:
        My_logger_obj.logger.exception(e)

divide(5,7)
add(4,8)
