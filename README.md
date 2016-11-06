# proj6-mongo
A simple list of dated memos kept in MongoDB database.

## Functionality

The user is able to add dated memos from a separate page. 
Memos displayed in date order. 
The user is able to delete memos. 

## Setting up

Setting up should follow a series of commands after you've forked
and cloned the project:

* bash ./configure
* make run [or make service]

Note that this requires a mongod (a la MongoDB) running in order to
function, with the /secrets directory containing the necessary information
to employ user, tester, and administrator accounts.

Our use of the database is pretty simple, but you should anticipate
that installing MongoDB could take some time.  Since you may not be
able to install the same version of MongoDB on your development
computer and your Pi, it will be especially important to test your
project on the Pi. 

The version of MongoDB available for installing on Raspberry Pi with
apt-get is 2.4.  The version you can find for your development
computer is probably 3.x.  You may even have difficulty finding
documentation for 2.4, as it is considered obsolete.  However,
commands that work for 2.4 still seem to work for 3.x, so you should
write your application and support scripts to use 2.4.   The
difference that may cause you the most headaches is in creating
database user accounts (which are different than the Unix accounts for
users). 

In Python, the pymongo API works with both versions of MongoDB, so
it's only the initial setup where you have to be  
careful to use the right version-specific commands. 

## FIXME

* The automated nosetest suite remains functionally useless - it still tries
to employ the client's account rather than the tester's. The structure of
the application is poorly suited for such tests, but some editing from anyone
savvy with MongoDB and Nose might have better luck. Alternatively, a series of
unittests for the various Flask pages might be more appropriate considering the
number of routes that employ POST.