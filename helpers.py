import temp_db

class JSONHelper():
    """Helper class(bleh) to ease the retrieve of JSON"""

    @staticmethod
    def get_sources(package_name):
        """Returns an array of all of the sources for a package"""
        return temp_db.json['package'][package_name]['sources']


