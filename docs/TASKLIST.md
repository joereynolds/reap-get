# Command line

- [ ] Add regular expressions to arguments (no idea how hard this'll be). i.e. A user can do reap-get -i s* (install all packages beginning with 's')
- [ ] Add support for versions of a package
- [ ] Currently you can't remove a package if you want to
- [ ] --setdaw config option
- [ ] A progress bar whilst packages are downloading would be nice
- [ ] reap-get should only display approved packages, not all packages.

# Web

- [ ] Add the ability to sort by table heading in the package search
- [ ] Users need the ability to specify multiple sources since the functionality is actually already there on Python's side
- [ ] Users should be able to specify the rest of the fields too (os, vst version, etc...)
- [ ] Add a friendly thank you message when a user submits a package. Something along the lines of
- [ ] create a cron that pings the download of plugins location to make sure the plugin hasn't 404d or moved.
```
Thank you for submitting your package, it will be reviewed and approved within 24 hours.
```
 


# Complete

- [x] There's no way to see installed packages
- [x] When a file has been downloaded and moved to the correct plugin path, delete the file from reap-get's directory
- [x] Create methods so the json can work with tabby
- [x] Add an extra option to display more info about a package (size, operating system etc...)
- [x] Add a 'reapfile.json' which is essentially an automated build of all of the plugins you want to install.
      It's a json file consisting of package names which reap-get will then download one-by-one (thanks to /u/DuoThree for the idea)
- [x] Host the packages.json file online
- [x] Get basic user.conf file working. Including directory paths
- [x] Move 'temp_db' into json file
- [x] In the future, when we have the web interface, we'll need to somehow approve packages before they go in the packages file
- [x] Add an --init command that will create a default user.json file for the user
- [x] Add a default value to show all plugins in the packages.json if no arguments are supplied
- [x] Change the package layout to 3-9. Not 4-8. Sidebar is too wide with this layout
