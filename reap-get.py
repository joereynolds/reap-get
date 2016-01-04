#!/usr/bin/env python3

import user
import argparse
import package_manager


def run():
    """Runs the whole shebang""" 
    #this is begging to be in a class   
    parser = argparse.ArgumentParser()
    parser.add_argument('--install', '-i', help='Installs a plugin to your plugin path')
    parser.add_argument('--remove', '-r', help='Removes the specified plugin')
    parser.add_argument('--setname','-sn', help='Sets the username in the configuration file.')
    parser.add_argument('--setpath','-sp', help='Sets the plugin path for all downloaded packages to be moved to')
    parser.add_argument('--view-installed', '-vi', help='Displays installed plugins on the users machine')
    parser.add_argument('--reap', '-rp',action='store_true', help='Installs the packages in reapfile.json')
    parser.add_argument('--setos','-so', help='Sets the operating system in the configuration file.')
    parser.add_argument('--getname','-gn', action='store_true', help='Gets the username in the configuration file.')
    parser.add_argument('--getpath','-gp', action='store_true', help='Gets the plugin path for all downloaded packages to be moved to')
    parser.add_argument('--getos','-go', action='store_true', help='Gets the operating system in the configuration file.')
    parser.add_argument('--getdetails', '-gd',action='store_true', help='Displays your OS, name, and path')
    parser.add_argument('--view',action='store_true', help="View all packages")
    parser.add_argument('--init', action='store_true', help="Creates a blank user.json")
    args = parser.parse_args()
    reap_user = user.User()
    manager = package_manager.PackageManager(reap_user)


    if args.install:
        manager.manage_packages(args.install)  

    if args.reap:
        manager.process_reapfile()

    if args.view:
        manager.show_packages()

    if args.getdetails:
        print(reap_user.name)
        print(reap_user.os)
        print(reap_user.plugin_path)

    if args.remove:
        manager.remove_package(args.remove)

    if args.getname:
        print(reap_user.name)

    if args.getpath:
        print(reap_user.plugin_path)

    if args.getos:
        print(reap_user.os)

    if args.setname:
        reap_user.set_property('name', args.setname)

    if args.setos: 
        reap_user.set_property('os', args.setos)

    if args.setpath:
        reap_user.set_property('plugin-path', args.setpath)

if __name__ == '__main__':
    run()
