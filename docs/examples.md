
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

##### Using a reapfile
This will install all the packages you've specified in reapfile.json. You can read more about reapfiles [here](reapfile.md)

```
python reap-get.py --reap
```


