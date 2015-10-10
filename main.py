#!/usr/bin/env python
import package_manager
import argparse
import helpers

def run():
    """Runs the whole shebang""" 
   
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', '-i', help='installs a plugin to your plugin path')
    parser.add_argument('--remove', '-r', help='removes the specified plugin')
    parser.add_argument('--view', help="View all packages")
    args = parser.parse_args()
    manager = package_manager.PackageManager()

    if args.install:
        manager.manage_packages(args.install)  

    if args.view :
        manager.show_packages()

if __name__ == '__main__':
    run()
