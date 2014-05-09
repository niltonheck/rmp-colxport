##Sync/Export RunMyProcess Collection

We use this command-line tool to create a local copy of a RunMyProcess collection for purposes like: reduction of risks (during maintenances), realize local tests throughout Mongo Database, among others reasons.

To use this tool you need to have an local [MongoDB](http://uol.com.br) installed and configured locally. Also, you'll need **pyMongo**  package installed in your python path. [See here how install pyMongo](http://api.mongodb.org/python/current/installation.html).

### Usage

It's pretty simples to use this tool.
Notice: All the parameters used below are **required**.

```Bash
python colxport.py
  -u example@domain.com
  -p ******
  -c 123456789234
  -cl mycollection
  -lh 127.0.0.1
  -ldb runmyprocess
  -lc acoes
```


### Help

More information about the **required** and optional arguments can be found using the -h (--help) argument. Here's an example of the help output:

```Bash
usage: colxport [-h] -u USERNAME -p PASSWORD -c CUSTOMERID -cl COLLECTION [-m MODE]
          -lh LOCAL_HOST -ldb LOCAL_DATABASE -lc LOCAL_COLLECTION

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --user USERNAME
                        e-mail of the runmyprocess account with privilegies
  -p PASSWORD, --pass PASSWORD
                        password of the runmyprocess account with privilegies
  -c CUSTOMERID, --customer CUSTOMERID
                        identifier of the customer (visible at the application
                        url)
  -cl COLLECTION, --collection COLLECTION
                        name of the collection you wish to copy from the
                        runmyprocess IDE
  -m MODE, --mode MODE  mode of the environment desired, available options
                        are: LIVE (default) or TEST
  -lh LOCAL_HOST, --host LOCAL_HOST
                        address of the local host database, usually it is
                        127.0.0.1 or localhost
  -ldb LOCAL_DATABASE, --local-database LOCAL_DATABASE
                        name of the local database
  -lc LOCAL_COLLECTION, --local-collection LOCAL_COLLECTION
                        name of the collection you wish to be populated
```
