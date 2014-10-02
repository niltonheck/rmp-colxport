import rmp_colxport.utils as rutils
from rmp_colxport.rmpauth import RMPAuth
import json, requests, base64, cli.app
import xml.etree.cElementTree as et

@cli.app.CommandLineApp
def sync(app):
  # url = 'https://live.runmyprocess.com/config/124158809/project/39799/collection/'

  url = 'https://live.runmyprocess.com/config/11761372963756487/project/58592/collection/?P_mode=TEST'

  r = requests.get(url, auth=RMPAuth('Basic ' + base64.b64encode(app.params.username+':'+app.params.password)))

  tree = et.fromstring(r.text)

  for child in tree.findall('{http://www.w3.org/2005/Atom}entry'):

    # defino a pagina
    cont = True
    page = 0
    conta = 0
    collection = child[0].text

    while cont == True:


      colUrl = 'https://live.runmyprocess.com/' + child[1].attrib['href'] + '/?P_mode=TEST&P_nb=1000&P_first=' + str(page * 1000)
      colR = requests.get(colUrl, auth=RMPAuth('Basic ' + base64.b64encode(app.params.username+':'+app.params.password)))

      if len(colR.json()) > 0:
        for item in colR.json():
          rutils.stablishCon(app.params.database, collection).insert(item)
          conta = conta + 1


      else:
        cont = False

      page = page + 1

    print "Success: " + str(conta) + " record(s) imported to local Mongo Database at " + collection



sync.add_param('-u', '--user', help="e-mail of the runmyprocess account with privilegies", default=False, action="store", dest='username', required=True)
sync.add_param('-p', '--pass', help="password of the runmyprocess account with privilegies", default=False, action="store", dest='password', required=True)
sync.add_param('-d', '--database', help="password of the runmyprocess account with privilegies", default=False, action="store", dest='database', required=True)

if __name__ == "__main__":
  sync.run()
