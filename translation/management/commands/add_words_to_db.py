import json
import time

from django.core.management.base import BaseCommand, CommandError
from translation.models import Translation

class Command(BaseCommand):
    help = 'Add records to database'

    def handle(self, *args, **options):
        with open('words.json') as fin:
            for line in fin:
                try:
                    d = json.loads(line)
                    new_word = Translation(meaning=d['definition'], example=d['example'], word=d['word'])
                    new_word.save()
                except:
                    continue