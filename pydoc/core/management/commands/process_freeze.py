"""
Management command for loading all the known packages from the official
pypi.
"""

import sys
from django.core.management.base import BaseCommand
from pydoc.taskapp.celery import build


class Command(BaseCommand):
    help = """Build docs from pip freeze output"""

    def handle(self, *args, **options):
        for line in sys.stdin:
            line = line.strip()
            package, version = line.split('==')
            print("Building %s:%s" % (package, version))
            build.delay(project=package, version=version)
