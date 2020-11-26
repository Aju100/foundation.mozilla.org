from django.db import connection
from django.core.cache import cache
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Removes the people app - use post-deploy'

    def handle(self, *args, **options):
        DEL_APPS = ['people']
        contentTypes = ContentType.objects.all().order_by('app_label', 'model')
        for entry in contentTypes:
            if (entry.app_label in DEL_APPS):
                print(f'Deleting Content Type {entry.app_label} {entry.model}')
                entry.delete()

        with connection.cursor() as cursor:
            cursor.execute("DROP SEQUENCE IF EXISTS people_affiliation_id_seq CASCADE")
            cursor.execute("DROP SEQUENCE IF EXISTS people_internethealthissue_id_seq CASCADE")
            cursor.execute("DROP SEQUENCE IF EXISTS people_person_id_seq CASCADE")
            cursor.execute("DROP SEQUENCE IF EXISTS people_person_internet_health_issues_id_seq CASCADE")
            cursor.execute("DROP TABLE IF EXISTS people_affiliation CASCADE")
            cursor.execute("DROP TABLE IF EXISTS people_internethealthissue CASCADE")
            cursor.execute("DROP TABLE IF EXISTS people_person CASCADE")
            cursor.execute("DROP TABLE IF EXISTS people_person_internet_health_issues CASCADE")
