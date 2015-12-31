
#Reapfiles

A reapfile is a JSON file consisting of package names for reap-get to install.
This means that moving from machine to machine to do any audio work is significantly easier
as you can just pass the reapfile to reap-get and it will handle the rest for you.

A typical reapfile might look like the following

    {
    "packages": [
            {
            "name": "synth1",
        },
            {
            "name": "asian-dreamz",
        },
            {
            "name": "world-stringz",
            }
        ]
    }

(note that at the moment, all you need to supply is the package name.
This will change when methods to handle versions are introduced.)

Creating a 'reapfile.json' and placing it in the root of reap-get will allow reap-get to do
its magic.
