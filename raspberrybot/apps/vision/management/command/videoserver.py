from django.core.management.base import BaseCommand

from bushlog.apps.location.models import Coordinate, Polygon


class Command(BaseCommand):
    args = 'coordinate_file'
    help = "Import border coordinates from file."

    def handle(self, *args, **options):
        coordinate_input = open(args[0]).read()
        polygon = Polygon.objects.create()

        # parse the input file and create the coordinate
        lines = coordinate_input.split(';')
        for line in lines:
            latitude, longitude = line.split(',')
            obj = Coordinate.objects.create(
                polygon=polygon,
                latitude=latitude,
                longitude=longitude
            )
            print "Coordinate created: ", obj.id

        print "**************************"
        print "Border polygon created: ", polygon.id
