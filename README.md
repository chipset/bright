# CA Brightside Python Wrappers
These are files provide additional functionality to [CA Brightside](https://www.ca.com/brightside "CA Brightside") specifically for CA Endevor profiles.

The scripts are written using Python 2.5+.  
## Assumptions
You must create a profile for your Endevor instance and it must be active as the default profile.

## Usage
Usage:
python bright-side.py "ENDEVOR INSTANCE" "ENDEVOR ENVIRONMENT" "ENDDEVOR SYSTEM" "ENDEVOR SUBSYSTEM" (OPTIONS)

## Download by CCID
python bright-side.py WEBSALC SIMPLTEST FINANCE ACCTREC -c US146

## Download all Elements in subsystem (wildcards work)
python bright-side.py WEBSALC SIMPLTEST FINANCE * -a

## Download upstream components
To be documented

# Jenkins Folder 
Contains pipeline script examples for calling bright-side.py and CA Brightside
