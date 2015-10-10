import json

class JSONHelper():
    """Helper class(bleh) to ease the retrieval of JSON"""

    json_file = open('packages.json')
    json_obj = json.load(json_file)

    @staticmethod
    def get_sources(package_name):
        """Returns an array of all of the sources for a package"""
        return JSONHelper.json_obj[package_name]['sources']

    def add_package():
        """Adds a package to the JSON file, this will be used for the
        web interface for users adding packages"""
        pass


