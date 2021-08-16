import collections
import csv

from django.core import management
from django.db.models import F

from casino import models


class Command(management.BaseCommand):
    help = "Imports users."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            'input_file',
            type=open,
            help='CSV file with columns: id, first_name, last_name, email, balance, referrer_email. HEADERS REQUIRED!',
        )

    def handle(self, *args, input_file, **options):
        references = collections.Counter()
        done = 0
        fail = 0
        for row in csv.DictReader(input_file):
            self.stdout.write(f'Importing user {row["id"]}')
            try:
                models.User.objects.create(**row)
                done += 1
                if row['referrer_email']:
                    references[row['referrer_email']] += 1
            except Exception as e:
                self.stderr.write(str(e))
                fail += 1

        for email, count in references.items():
            try:
                models.User.objects.filter(email=email).update(balance=F('balance') + count * 20)
            except Exception as e:
                self.stderr.write(str(e))

        self.stdout.write(f"Done: {done}. Failed: {fail}.")
