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

    archiveExtensions = {'zip'}
    vstExtensions = {'exe','dll'}


    def manage_packages(self, package_name):
        """A wrapper that downloads, extracts and moves the
        file"""
        print('Downloading', package_name)
        self.download(package_name)
        print('Unzipping', package_name)
        self.unzip(package_name)
        print('Moving', package_name,'to [your plugin path]')
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
                print('Invalid package URL. Please report to package creator') #Give a link to the website when we have one

    def unzip(self, downloaded_file):
        """Creates a directory for the downloaded file, unzips it into that directory and removes
        the leftover file that was downloaded"""
        try :
            directory_name = downloaded_file
            os.mkdir(directory_name)
        except FileExistsError : 
            directory_name = downloaded_file + '_reap_get'
            os.mkdir(downloaded_file + '_reap_get')
        
        unzipper = zipfile.ZipFile(downloaded_file)
        unzipper.extractall(directory_name)
        unzipper.close()
        os.remove(downloaded_file)


    def move(self):
        """Moves the extracted file(s)
        to the user's plugin path"""
        #try :
        #    shutil.copytree()


