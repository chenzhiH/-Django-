import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE','assistant.settings')
django.setup()

def logdemo():
    logger=logging.getLogger("django")
    logger.info('hello my daniuniu')


if __name__=='__main__':
    logdemo()