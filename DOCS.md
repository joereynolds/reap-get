#JSON

### Structure

The json is formatted like so
```
Package
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
