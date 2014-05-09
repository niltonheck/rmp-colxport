import rmp_colxport.utils as rutils
from rmp_colxport.rmpauth import RMPAuth
import json, requests, base64, cli.app

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

@cli.app.CommandLineApp
def ls(app):
  __page = 0
  __continue = True
  __records = 0

  while __continue == True:

    url = 'https://live.runmyprocess.com/pub/' + app.params.customerid + '/object/' + app.params.collection + '/?P_mode=' + app.params.mode + '&P_nb=1000&P_first=' + str(__page * 1000)

    r = requests.get(url, auth=RMPAuth('Basic ' + base64.b64encode(app.params.username+':'+app.params.password)))

    if r.status_code == 400:
      print 'Error: Unable to access RunMyProcess data, check your customerid and collection name.' + bcolors.FAIL + ' x' + bcolors.ENDC
      exit()
    elif r.status_code == 403:
      print 'Error: Unable to log in RunMyProcess, check your username and password.' + bcolors.FAIL + ' x' + bcolors.ENDC
      exit()
    else:
      if len(r.json()) > 0:
        for item in r.json():
          rutils.stablishCon('runmyprocess', 'acoes').insert(item)
          __records = __records + 1
      else:
        __continue = False

      __page = __page + 1

  print "Success: " + str(__records) + " record(s) imported to local Mongo Database " + bcolors.OKGREEN + u'\u2713' + bcolors.ENDC

ls.add_param('-u', '--user', help="e-mail of the runmyprocess account with privilegies", default=False, action="store", dest='username', required=True)
ls.add_param('-p', '--pass', help="password of the runmyprocess account with privilegies", default=False, action="store", dest='password', required=True)
ls.add_param('-c', '--customer', help="identifier of the customer (visible at the application url)", default=False, action="store", dest='customerid', required=True)
ls.add_param('-cl', '--collection', help="name of the collection you wish to copy from the runmyprocess IDE", default=False, action="store", dest='collection', required=True)
ls.add_param('-m', '--mode', help="mode of the environment desired, available options are: LIVE (default) or TEST", default='LIVE', action="store", dest="mode")
ls.add_param('-lh', '--host', help="address of the local host database, usually it is 127.0.0.1 or localhost", default='LIVE', action="store", dest="local_host", required=True)
ls.add_param('-ldb', '--local-database', help="name of the local database", default=False, action="store", dest="local_database", required=True)
ls.add_param('-lc', '--local-collection', help="name of the collection you wish to be populated", default=False, action="store", dest="local_collection", required=True)

if __name__ == "__main__":
  ls.run()