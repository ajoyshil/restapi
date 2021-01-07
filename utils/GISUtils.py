from django.contrib.gis.geos import Point


class GISUtils:
    @staticmethod
    def calculate_distance(current_location: Point, last_location: Point):
        print("Current Location: " + str(current_location.coords))
        print("Last Location: " + str(last_location.coords))
        return last_location.distance(current_location)*100000
