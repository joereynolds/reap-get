#!/usr/bin/env python3

import json
import sys
import os
import socket

class User():


    DAWS = {
        'default': 'some_path',
        'reaper' : 'some_path',
        'cubase' : 'some_path',
    }

    def __init__(self):
        self.conf_file = self.load_user_file()
        self.plugin_path = self.get_property("plugin-path")
        self.name = self.get_property("name")
        self.os = self.get_property("os")

    def load_user_file(self):
        try :
            open('user.json')
        except FileNotFoundError :
            print('User configuration file not found. Creating default.')
            self.create_default_json()

    def create_default_json(self):
        """Creates a 'default' user if the user hasn't done any configuration yet"""
        default_user  = {
            "user" : {
                "name" : socket.gethostname(),
                "os" : sys.platform,
                "plugin-path" : self.create_default_plugin_path()
            }
        }

        with open('user.json','w') as user_json:
            json.dump(default_user, user_json)

        self.plugin_path = default_user["user"]["plugin-path"]
        self.name = default_user["user"]["name"]
        self.os = default_user["user"]["os"]

    def create_default_plugin_path(self):
        """Creates a default plugin path that won't work. Forcing the user to specify one... bad idea or great idea?"""
        return "plz."

    def get_property(self, json_property):
        """Returns the name field from the user.json file"""
        json_file = open('user.json')
        json_obj = json.load(json_file)
        return json_obj["user"][json_property]

    def set_property(self, attr, value):
        """Sets the ['user'][attr] to [value]
        i.e.
            set_json_attr('name', 'kevin')
            would set the name field to kevin"""
        json_file = open('user.json')
        json_obj  = json.load(json_file)
        json_obj['user'][attr] = value

        with open('user.json','w') as user_json:
            json.dump(json_obj, user_json)
