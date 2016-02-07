#!/usr/bin/env python3

import socket
import json
import sys
import os

class User():
    """contains methods for creating and getting user attributes from
    user.json"""


    DAWS = {
        'default': 'some_path',
        'reaper' : 'some_path',
        'cubase' : 'some_path',
    }

    def __init__(self):
        """
            self.user_file : The name of the user.json file
	    self.conf_file : The json object of the user file
	    self.os : The inferred name of the user's OS
	    self.name : The inferred name of the user
	    self.plugin_path : A default path


	"""
        self.user_file = 'user.json'
        self.conf_file = self.load_user_file()

        self.os = self.get_property("os")
        self.name = self.get_property("name")
        self.plugin_path = self.get_property("plugin-path")


    def load_user_file(self):
        """does a quick test to see if we have a user file. if not, we create one.
	this should use an if not a try though..."""
        try :
            json_file = open(self.user_file)
        except FileNotFoundError :
            print('User configuration file not found. Creating default.')
            self.create_default_json()
        else :	    
            json_obj = json.load(json_file)
            json_file.close()
            return json_obj

    def create_default_json(self):
        """Creates a 'default' user if the user hasn't done any configuration yet"""
        default_user  = {
            "user" : {
                "name" : socket.gethostname(),
                "os" : sys.platform,
                "plugin-path" : self.create_default_plugin_path(),
                "packages" : []           
            }
        }

        with open(self.user_file, 'w') as user_json:
            json.dump(default_user, user_json)

        self.plugin_path = default_user["user"]["plugin-path"]
        self.name = default_user["user"]["name"]
        self.os = default_user["user"]["os"]

    def create_default_plugin_path(self):
        """Creates a default plugin path that won't work. Forcing the user to specify one..."""
        return "please/set/a/plugin/path/"    

    def add_package(self, package_name):
        """Adds the installed package to the user.json configuration file.
        This is later used to uninstall the package if the user wishes to do so"""
        json_file = open(self.user_file)
        json_obj  = json.load(json_file)
        json_obj['user']['packages'].append(
            {
                'name' : package_name
            }
        )

        with open(self.user_file, 'w') as user_json:
            json.dump(json_obj, user_json)
    
    def get_property(self, json_property):
        """Returns the name field from the user.json file"""
        return self.conf_file['user'][json_property] 


    def set_property(self, attr, value):
        """Sets the ['user'][attr] to [value]
        i.e.
            set_json_attr('name', 'kevin')
            would set the name field to kevin"""
        json_file = open(self.user_file)
        json_obj  = json.load(json_file)
        json_obj['user'][attr] = value

        with open(self.user_file, 'w') as user_json:
            json.dump(json_obj, user_json)
