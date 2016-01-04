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
        """ Memoized property for accessing remote data"""
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
                print(package['sources'])
                return package['sources']

    def get_packages(self):
        """Returns an array of package names"""
        #messy
        return [self.data[package]['name'] for package in range(len(self.data))]
    
