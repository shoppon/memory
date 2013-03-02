from django.core.management.base import BaseCommand

class Commend(BaseCommand):
    def handle(self, *args, **options):
        BaseCommand.handle(self, *args, **options)