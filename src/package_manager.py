#/usr/bin/env python3

import distutils.dir_util
import urllib.request
import urllib.error
import zipfile
import shutil
import json
import os

import package_repository
import config
import tabby


class PackageManager():

    def __init__(self, user):
        self.user = user
        self.reader = package_repository.PackageRepository()

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
            for package in self.reader.filter_where('type', package_type):
                print(package)
        else:
            tabby.tabby_print(
                self.reader.get_properties('name'),
                self.reader.get_properties('type'),
                self.reader.get_properties('os'),
                self.reader.get_properties('nicesize'),
                headings=['PACKAGE', 'TYPE', 'OS', 'SIZE']
            )

    def show_installed_packages(self):
        try:
            tabby.tabby_print(
                self.reader.get_installed_packages(),
                headings=['PACKAGE']
        )
        except ValueError:
            print('You have no packages installed')

    def remove_package(self, package_name: str):
        """Removes an installed package from the users
        plugin_path. Note that this implementation will
        probably need to be changed when we are managing
        different versions of the same package

	command : reap-get --remove package_name
	"""
        filepath_name = 'vst-' + package_name
        filepath = self.user.plugin_path + '/' + filepath_name

        self.remove_package_from_filesystem(filepath)
        self.remove_package_from_json(package_name)

    def remove_package_from_json(self, package_name: str):
        """Removes the plugin entry from the user's json file."""
        for element in self.user.conf_file['user']['packages']:
            if element['name'] == package_name:
                del element['name']

        print(self.user.conf_file['user']['packages'])

    def remove_package_from_filesystem(self, filepath: str):
        """Removes the packages from the machine
        filename : the path to our file i.e. d:/programs/reaper/fx/vst-synth1"""
        try:
            shutil.rmtree(filepath)
        except FileNotFoundError:
            print("reap-get couldn't find the file " + filepath)
        else:
            print("removed file " + filepath)

    def process_reapfile(self):
        """Installs the packages from a user's reapfile"""
        with open(config.reapfile_file) as reapfile:
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

        directory_name = 'vst-' + downloaded_file
        os.mkdir(directory_name)

        self.extract(downloaded_file, directory_name)
        self.move(directory_name)

        #remove temporary files
        os.remove(downloaded_file)
        shutil.rmtree(directory_name)

    def move(self, old_directory):
        """Moves the extracted file(s)
        to the user's plugin path"""
        distutils.dir_util.copy_tree(old_directory, self.user.plugin_path +'\\' + old_directory)

    def extract(self, filename, directory_name):
        """extracts filename and places it into directory_name"""
        unzipper = zipfile.ZipFile(filename)
        unzipper.extractall(directory_name)
        unzipper.close()


