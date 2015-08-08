# Scripts for managing docker tasks
This is a collection of scripts that I use in my job for managing
docker containers. These scripts are:

* ds (docker start): Starting a existing docker container.
* dr (docker run): Create a docker container from specified image. Type 'dr --help' for more options.
* dc (docker commit): Commit changes in the container back to image.

## Configuration file
The configuration file (docker.ini) is in INI-like format; you can
put your volume mappings and author information in the file. The
sample is as following:

    [volumes]
    map0src = <Your host absolute directory path>
    map0dst = <Your target absolute directory path>
    map1src = <Your anthoer host absolute directory path>
    map1dst = <Your anthoer target absolute directory path>
    
    [author]
    name = <Your name>
    email = <Your email>

## License
These scripts are licensed under GNU General Public License (GPL),
version 2 or above.
