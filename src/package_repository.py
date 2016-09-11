#!/usr/bin/env python3

import json
import urllib.request
from typing import List
from functools import lru_cache


class PackageRepository():
    """Reads package data to send across to the PackageManager class where it can
    be downloaded, viewed etc...
    
    
    @json_path = The path to the json file. In this case that would be the assets folder of reap-get
    @data = The packages.json file
    """

    def __init__(self, json_path = 'http://reap-get.com/assets/packages.json'):
        self.json_path = json_path

    @property
    @lru_cache(4)
    def data(self):
        """Memoized property for accessing remote data"""
        return self._load_json()
            
    def _load_json(self):
        #This is a giant hack, basically we check for http
        #if it doesn't have that in the string, then in theory
        #we're passing it raw json.
        #this is mainly useful for testing. I'm sorry...
        if 'http' in self.json_path:
            data = urllib.request.urlopen(self.json_path)
            str_response = data.read().decode('utf-8')
            json_data = json.loads(str_response)
        else:
            json_data = json.loads(json.dumps(self.json_path))
        return json_data

    def get_property(self, package_name: str, package_property: str) -> str:
        """Returns the value of a packages key
        i.e. get_property('synth1', 'type')
        would return 'instrument'"""
        for package in self.data:
            if package_name == package['name']:
                if package_property in package:
                    return package[package_property]

    def get_properties(self, package_property: str) -> List[str]:
        """Similar to get_property except that it returns
        multiple of the result.
        
        For example, 
            get_properties('os')
        Would return an array of the os for each package
        such as
            [window, mac, mac, windows, windows, windows, windows]"""
        matches = []
        for package in self.data:
            if package_property in package:
                matches.append(package[package_property])
            else:
                #I consider this a hack.
                #Really all of our plugins should have
                #The data required and keyerrors wouldn't happen
                matches.append('None')
        return matches    

    def filter_where(self, package_type: str, value: str) -> List[str]:
        """Returns an array of all packages that have the supplied type.
        The supplied type is an array on the website-side that includes
        'instrument' and 'effect' and a few others"""
        matches = []
        for package in self.data:
            if package_type in package:
                if value == package[package_type]:
                    matches.append(package)
        return matches            

    def get_installed_packages(self):
        json_file = open('user.json')
        json_obj = json.load(json_file)
        return [package['name'] for package in json_obj['user']['packages']]
        
    def get_sources(self, package_name: str) -> List[str]:
        """Returns an array of all of the sources for a package"""
        return self.get_property(package_name, 'sources')
