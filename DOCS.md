#JSON

## User

The user.json file is to store any metadata about the user that reap-get needs.

The json is formatted like so
```
Users Name
    OS
    Plugin Path

```

##### User name

This is configurable in reap-get with the command

```
put command here
```

##### OS

This is used in reap-get to get the correct version of the plugin. Some plugins are only compatible with a certain OS. Supplying this information helps the user get the correct plugin. If no OS is specified it falls back to Windows (Not yet implemented)

##### Plugin Path

Without this specified reap-get is pretty much pointless. The plugin-path needs to be supplied so that reap-get can move the downloaded VST into the users plugin-path. If no path is specified, reap-get will shout at you.

## Packages 
### Structure

The json is formatted like so
```
Package Name
    Package Verbose Name/Description
    Package Sources
```
##### Package Name

Package Name is the name you supply to the console and reap-get will download the package
i.e.
```
reap-get -i synth1
```

Here, synth1 is our Package Name.

##### Package Verbose Name/Description

Exactly what it says on the tin. This is used when a user wishes to inspect the package before blindly downloading a package. It also shows in verbose mode (adding a '-v' flag to reap-get)

##### Package Sources

An array of possible sources to download this file from. If the first url fails, it trys the next one and the next one, and the next one... and the next one... AND THE NEXT ONE.
