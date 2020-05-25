# Post mortem for Web stack debugging # 3

### By Daniel Rodriguez Castillo

This file contains a brief description about an outage occurred on May 19 until May 20, 2020, it was given to me a docker container that was wrongly configured to be broken, i tracked and found the main causes and restablished the failing services.


## Issue Summary:

the server was running but the response from the server was always a 500 code, the server depends on the Wordpress core so this facilitated the bug search, i used strace to track the services and found low level outages that kills the server response.



## Timeline

from 00:00 to May 20 at 13:15

May 20:
- 10:00 - The service failure was detected
- 11:48 - The collateral cause was found
- 12:36 - The Root and collateral causes was fixed
- 13:15 - An Automized script was uploaded to github

## Root cause

On May 20 i detected a wrong response from the server running at the docker container, a framework was given and i take the tool in the Resources, with strace listening and a curl request at the time i figured out that MySQL, in the next goofy issue while checking the strace i noticed that an stat() system call was trying to get an non-existent file the extension was '.phpp',  so i checked the files to track this call and the issue was in the configuration file it requires a file named 'class-wp-locations.phpp' note the '.phpp'.

## Resolution and recovery

It was necessary to modify the 'wp-settings.php', changing the extension for the required file from '.phpp' to 'php' and save the file, also restart MySQL and apache2 services, then the server was tested with the browser and curl requests, in all cases the route return a success html response 

## Corrective and preventative measures
