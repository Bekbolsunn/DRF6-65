from csv import Error

from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    print("START")
    sleep(20)
    raise Error
    print("FINISH")
    return x + y
