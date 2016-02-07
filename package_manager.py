#!/usr/bin/env python3

import distutils.dir_util
import urllib.request
import urllib.error
import zipfile
import shutil
import json
import os

import package_reader
import tabby


class PackageManager():
    """
    @archiveExtensions = A list of all valid extensions to check through. If the file ends in one of these
                         an attempt is made to unzip the file
    """

    archiveExtensions = ('zip')
    vstExtensions = ('exe','dll')

    def __init__(self, user):
        self.user = user
        self.reader = package_reader.JSONReader()

    def manage_packages(self, package_name: str):
        """A wrapper that downloads, extracts and moves the
        file"""
        #Check to see if we have the package in our db
        if not self.reader.get_sources(package_name):
            print('No package with the name "' + package_name +'" found.')
            return
        print('Downloading', package_name)
        self.download(package_name)
        print('Unzipping', package_name)
        print('Moving', package_name,'to ',self.user.plugin_path)
        self.unzip(package_name)
        self.user.add_package(package_name)

    def show_packages(self, package_type=''):
        """Prints all packages of a given type (all if not specified).
        Output is also formatted"""
        if package_type:
            for package in self.reader.get_type(package_type):
                print(package)
        else:        
            tabby.tabby_print(
                self.reader.get_packages(),
                self.reader.get_properties('type'),
                self.reader.get_properties('os'),
                self.reader.get_properties('nicesize'),
                headings=['PACKAGE', 'TYPE', 'OS', 'SIZE']
            )

    def show_installed_packages(self):
        tabby.tabby_print(
            self.reader.get_installed_packages(),
            headings=['PACKAGE']
	)

    def remove_package(self, package_name):
        """Removes an installed package from the users
        plugin_path. Note that this implementation will 
        probably need to be changed when we are managing
        different versions of the same package"""
        filepath = self.user.plugin_path + '/' + package_name
        os.remove(filepath)
        print("removed file" + filepath)

    def process_reapfile(self):
        """Installs the packages from a user's reapfile"""
        with open('reapfile.json') as reapfile:
            data = json.load(reapfile)

        for package in data['packages']:
            self.manage_packages(package['name'])

    def download(self, package_name: str):
        """Downloads @package_name from packages.json"""
        for url in self.reader.get_sources(package_name):
            try:
                urllib.request.urlretrieve(url, package_name)
                break
            except urllib.error.URLError:
                print('Unable to download from source, trying other sources')
            except ValueError: 
                print('Invalid package URL. Please report to package creator') #Give a link to the website when we have one

    def unzip(self, downloaded_file):
        """Creates a directory for the downloaded file, unzips it into that directory and removes
        the leftover file that was downloaded"""

        #For some reason, the except clause always gets
        #executed and not the try so we end up with directories
        #ending in _reap-get instead of just the normal file name
        try :
            directory_name = downloaded_file
            os.mkdir(directory_name)
        except FileExistsError : 
            directory_name = downloaded_file + '_reap_get'
            os.mkdir(downloaded_file + '_reap_get')
        
        unzipper = zipfile.ZipFile(downloaded_file)
        unzipper.extractall(directory_name)
        unzipper.close()
        self.move(directory_name)

        #try and remove both the files   
        os.remove(downloaded_file)
        shutil.rmtree(downloaded_file + '_reap_get')

    def move(self, old_directory):
        """Moves the extracted file(s)
        to the user's plugin path"""
        distutils.dir_util.copy_tree(old_directory, self.user.plugin_path +'\\' + old_directory)


