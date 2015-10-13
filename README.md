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

##### Create a default user
Creating a default user saves you some work. It retrieves your name and os for you.
You'll still have to specify your plugin since Python (suprisingly) can't read minds

```
    python reap-get.py --init
```

##### Set your plugin's directory
Once you've set your plugin's directory, reap-get will know all it needs to start
saving you time :D

```
    python reap-get.py --setpath c:/users/your/plugin/path
```

##### View all packages
Viewing all the packages will help illustrate what is up for grab at this moment

```
    python reap-get.py --view 
```
##### Download a package
Once you've found a package that interests you, run the command

```
    python reap-get.py --install synth1
```

and you'll find that reap-get has unzipped it and placed it in your plugins directory

#Web

reap-get isn't just a command line utility. There's a web interface to upload your own packages
(as long as they're licensed appropriately) and other stuff
