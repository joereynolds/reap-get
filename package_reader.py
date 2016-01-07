#!/usr/bin/env python3

import json
import urllib.request
from functools import lru_cache


class JSONReader():
    """Reads package data to send across to the PackageManager class where it can
    be downloaded, viewed etc...
    
    
    @json_path = The path to the json file. In this case that would be the assets folder of reap-get
    @data = The packages.json file
    """

    def __init__(self):
        self.json_path = 'http://reap-get.com/assets/packages.json'

    @property
    @lru_cache(4)
    def data(self):
        """Memoized property for accessing remote data"""
        return self._load_json()
            
    def _load_json(self):
        data = urllib.request.urlopen(self.json_path)
        str_response = data.read().decode('utf-8')
        json_data = json.loads(str_response)
        return json_data

    def get_sources(self, package_name):
        """Returns an array of all of the sources for a package"""
        for package in self.data:
            if package_name == package['name']:
                return package['sources']

    #Now that we have this, we can probably remove get_sources
    #and get_type_from_name
    def get_property(self, package_name, package_property):
        """Returns the value of a packages key
        i.e. get_property('synth1', 'type')
        would return 'instrument'"""
        for package in self.data:
            if package_name == package['name']:
                if package_property in package:
                    return package[package_property]

    def get_type(self, package_type):
        """Returns an array of all packages that have the supplied type.
        The supplied type is an array on the website-side that includes
        'instrument' and 'effect' and a few others"""
        matches = []
        for package in self.data:
            if 'type' in package:
                if package_type == package['type']:
                    matches.append(package)
        return matches            

    def get_packages(self):
        """Returns an array of package names"""
        return [self.data[package]['name'] for package in range(len(self.data))]
    
