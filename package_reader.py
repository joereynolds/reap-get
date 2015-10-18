import json
import urllib.request

#maybe not all static methods?
class JSONReader():
    """Reads package data to send across to the PackageManager class where it can
    be downloaded, viewed etc...
    
    
    @json_path = The path to the json file. In this case that would be the assets folder of reap-get
    @data = The packages.json file
    """

    def __init__(self):
        self.json_path = 'http://reap-get.com/assets/packages.json'
        self.data = self.load_json()

    def load_json(self):
        data = urllib.request.urlopen(self.json_path)
        str_response = data.read().decode('utf-8')
        json_data = json.loads(str_response)
        return json_data

    def get_sources(self, package_name):
        """Returns an array of all of the sources for a package"""
        return self.data[package_name]['sources']

    def get_packages(self):
        """Returns an array of package names"""
        return [key for key in self.data.keys()]
    
    def add_package(self):
        """Adds a package to the JSON file, this will be used for the
        web interface for users adding packages"""
        pass