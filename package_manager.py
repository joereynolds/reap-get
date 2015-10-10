import urllib.request
import urllib.error
import zipfile
import helpers
import shutil
import os

class PackageManager():
    """
    @archiveExtensions = A list of all valid extensions to check through. If the file ends in one of these
                         an attempt is made to unzip the file
    """

    archiveExtensions = {'zip','rar'}
    vstExtensions = {'exe','dll'}


    def manage_packages(self, package_name):
        """A wrapper that downloads, extracts and moves the
        file"""
        print('Retrieving', package_name)
        self.download(package_name)
        #self.unzip(package_name))
        #self.move(self, package_name)

    def show_packages(self):
        for package in helpers.JSONHelper.get_packages(): 
            print(package)

    def download(self, package_name):
        """downloads a file from @url"""
        for url in helpers.JSONHelper.get_sources(package_name):
            try :
                urllib.request.urlretrieve(url, package_name)
                break

            except urllib.error.URLError:
                print('Unable to download from source, trying other sources')

            except ValueError : 
                print('Unknown url type, whoever submitted this is a douche.')

    def unzip(self, downloaded_file):
        """unzips a file"""
        unzipper = zipfile.ZipFile(downloaded_file)
        unzipper.extractall()

    def move(self):
        """Moves the downloaded & extracted file
        to the user's plugin path"""
        pass
        #try :
        #    shutil.copytree()


