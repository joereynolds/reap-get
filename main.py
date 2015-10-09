#!/usr/bin/env python
import file_downloader
import argparse
import helpers

def run():
    """Runs the whole shebang""" 
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', '-i', help='installs a plugin to your plugin path')
    parser.add_argument('--remove', '-r', help='removes the specified plugin')
    args = parser.parse_args()
    downloader = file_downloader.FileDownloader()
    downloader.manage_package(args.install)  

if __name__ == '__main__':
    run()
