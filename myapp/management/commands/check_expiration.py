# myapp/management/commands/check_expiration.py

import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import *
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Command(BaseCommand):
    help = 'Example periodic cronjob task'

    def handle(self, *args, **kwargs):
        # just print a string as an example
        print("Executed the example periodic task successfully.")
       