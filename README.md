#reap-get

Reap-get is a package manager for VST plugins.
It handles downloading, unzipping and moving the file to your plugin directory all for you. I built this out of my hate for installing plugins. Truly the worst task known to man.

Reap-get (obviously) comes with a database of packages. 
Follow the instructions below for a brief guide on getting up to speed with it

# Usage

###Clone me

```
    git clone https://github.com/joereynolds/reap-get.git
    cd reap-get
```

### Use me 

run as administrator in Windows...sigh

##### Set your plugin's directory
```
    python reap-get.py --setpath c:/users/your/plugin/path
```

##### View all packages
```
    python reap-get.py --view 
```
##### Download a package
```
    python reap-get.py --install synth1
```


