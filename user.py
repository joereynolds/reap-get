import json
import sys
import os

class User():

    def __init__(self):
        self.conf_file = self.load_user_file()
        self.plugin_path = self.get_plugin_path()
        self.name = self.get_name()
        self.os = self.get_os()

    def load_user_file(self):
        try : 
            open('user.json')
        except FileNotFoundError : 
            print('User configuration file not found. Creating default.')
            self.create_default_json()

    def create_default_json(self):
        """Creates a 'default' user if the user hasn't done any configuration yet"""
        default_user = {"user" : 
                           {
                               "name" : os.environ['COMPUTERNAME'],
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

    def get_name(self):
        """Returns the name field from the user.json file"""
        pass
 
    def get_os(self):
        """Returns the os field from the user.json file"""
        pass

    def get_plugin_path(self):
        """Returns the plugin-path field from the user.json file"""
        pass


    #Setting attributes is very similar. Can be refactored into one function probably
    def set_name(self, name):
        """Sets the name in the user.json file"""

        user = {"user" : 
                           {
                               "name" : name,
                               "os" : self.os,
                               "plugin-path" : self.plugin_path
                           }
                       }

        with open('user.json','w') as user_json:
            json.dump(user, user_json)

    def set_os(self, os):
        """Sets the os in the user.json file"""
 
        user = {"user" : 
                           {
                               "name" : self.name,
                               "os" : os,
                               "plugin-path" : self.plugin_path
                           }
                       }

        with open('user.json','w') as user_json:
            json.dump(user, user_json)

    def set_plugin_path(self, path):
        """Sets the plugin-path in the user.json file"""
 
        user = {"user" : 
                           {
                               "name" : self.name,
                               "os" : self.os,
                               "plugin-path" : plugin_path
                           }
                       }

        with open('user.json','w') as user_json:
            json.dump(user, user_json)


