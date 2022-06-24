from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

celery = Celery("app", 
            broker='redis://redis:6379/0',
            backend='redis://redis:6379/0',
            include=['tasks']
            )

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

@celery.task(name='calculator.tasks.prime_service')
def prime_service(index):
    print("Task loaded")
    logger.info('Requested.Task Started')
    result = []
    start = 2
    counter = 0
    logger.info(f'Calculating prime {index}')
    while counter < index:
        if is_prime(start):
            result.append(start)
            counter += 1
        start += 1
    logger.info('Task Completed')
    return result[index-1]
    
@celery.task(name='calculator.tasks.prime_palindrome_service')
def prime_palindrome_service(index):
    print("Task loaded")
    logger.info('Requested.Task Started')
    result = []
    start = 2
    counter = 0
    print(f"Calculating prime palindrome {index}")
    while counter < index:
        if is_palindrome(start):
            if is_prime(start):
                result.append(start)
                counter += 1
        start += 1
    logger.info('Task Completed')
    return result[index-1]
    