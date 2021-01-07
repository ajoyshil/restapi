import urllib


class GoogleMaps(object):
    """ Google Maps utility class """
    def __init__(self, source_lat, source_lng, destination_lat, destination_lng):
        self.static_maps_dimension = "1920x1080"
        #self.gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
        self.source = (float(source_lat), float(source_lng))
        self.destination = (float(destination_lat), float(destination_lng))

    def make_direction_request(self):
        
        try:
            self.direction_data = self.gmaps.directions(self.source,self.destination,mode="driving")
            self.direction_data = self.direction_data[0]
            self.polyline = urllib.parse.quote_plus(self.direction_data['overview_polyline']['points'])
            # self.source_marker_point = (self.direction_data['bounds']['southwest']['lat'],self.direction_data['bounds']['southwest']['lng'])
            # self.destination_marker_point = (self.direction_data['bounds']['northeast']['lat'],self.direction_data['bounds']['northeast']['lng'])
            self.source_marker_point = (
                self.direction_data['legs'][0]['steps'][0]['start_location']['lat'],
                self.direction_data['legs'][0]['steps'][0]['start_location']['lng']
            )
            for point in self.direction_data['legs'][0]['steps']:
                self.destination_marker_point = (point['end_location']['lat'],point['end_location']['lng'])
            return True
        except:
            return False

    def get_polyline(self):
        try:
            return self.polyline
        except:
            return None

    def get_source_marker_point(self):
        try:
            return self.source_marker_point
        except:
            return None

    def get_destination_marker_point(self):
        try:
            return self.destination_marker_point
        except:
            return None

    def get_static_map_url(self):
        try:
            #self.static_maps_url = "https://maps.googleapis.com/maps/api/staticmap?size="+self.static_maps_dimension+"&sensor=true&key="+GOOGLEMAPS_API_KEY+"&maptype=terrain&markers=color:green%7C"+str(self.source_marker_point[0])+",%20"+str(self.source_marker_point[1])+"&markers=color:red%7C"+str(self.destination_marker_point[0])+",%20"+str(self.destination_marker_point[1])+"&path=weight:4%7Ccolor:black%7Cenc:"+self.polyline
            return self.static_maps_url
        except:
            raise
            return None
