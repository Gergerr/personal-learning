# Logging with real world example

import logging

# Logging Settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',  # Optional, specifies the timestamp format
    handlers= [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger= logging.getLogger('ArithmeticApp')
def add(a, b):
    result= a+b
    logger.debug(f'Adding {a}+{b}= {result}')
    return result

def substract(a, b):
    result= a-b
    logger.debug(f'Substracting {a}-{b}= {result}')
    return result

def multiply(a, b):
    result= a+b
    logger.debug(f'Multiplying {a}*{b}= {result}')
    return result

def divide(a, b):
    try:
        result= a/b
        logger.debug(f'Dividing {a}/{b}= {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero error')
        return None
    
divide(19, 0)
