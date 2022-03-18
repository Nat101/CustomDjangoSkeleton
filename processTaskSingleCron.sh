
#!/bin/sh

#This shell script checks to see if the subprocess "process_tasks --queue SingleProcess" is running.
#If not running, execute

if [ ! $(pgrep -f "process_tasks --queue SingleProcess") ]; then

        cd /Users/nataliecarlson/Desktop/Natalie/DjangoProjects/CustomDjangoSkeleton
        /Users/nataliecarlson/Desktop/Natalie/DjangoProjects/CustomDjangoSkeleton/venv/bin/typePythonVersionHere(ie: python3.8) /Users/nataliecarlson/Desktop/Natalie/DjangoProjects/CustomDjangoSkeleton/CustomDjangoSkeleton/manage.py process_tasks --queue SingleProcess
        exit 1

else
        exit 1
fi
exit 1