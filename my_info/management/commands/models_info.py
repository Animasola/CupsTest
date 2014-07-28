from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.db.utils import DatabaseError


class Command(BaseCommand):
    help = "Prints all project models and the count of objects in every model"

    def handle(self, *args, **options):
        try:
            for model in ContentType.objects.all():
                out = "%s: %s - %s\n" % (
                    model.app_label,
                    model.model,
                    model.model_class().objects.count()
                )
                self.stdout.write(out)
                self.stderr.write('Error: %s' % out)
        except:
            DatabaseError
