import logging

logging.basicConfig(filename='example_program.txt', level=logging.DEBUG, format='%(asctime)s - 5(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) - this mesage disables everything from CRITICAL and messages states lower than that

#logging levels:
#debug(lowest) - logging.debug()
#info - logging.info()
#warning - logging.warning()
#error - logging.error()
#critical(highest) - logging.CRITICAL()

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
