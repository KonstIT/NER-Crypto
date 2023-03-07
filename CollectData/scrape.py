import urllib.request
import polish
import time



def retrieveDataApi():
    #Collect Data from German language sources ==> Update Link with your own Authcode from cryptopanic.com
    responseDE = urllib.request.urlopen("https://cryptopanic.com/api/v1/posts/?auth_token=INSERT-TOKEN&regions=de")
    print('Time Buffer before next query')
    time.sleep(30)
    #Collect Data from German language sources ==> Update Link with your own Authcode from cryptopanic.com
    responseEN = urllib.request.urlopen("https://cryptopanic.com/api/v1/posts/?auth_token=INSERT-TOKEN&regions=en")

    dataDE = responseDE.read().decode('UTF-8')  
    dataEN =responseEN.read().decode('UTF-8')
    return [dataDE, dataEN]


data = retrieveDataApi()

polish.polishAndStore(data[0])
polish.polishAndStore(data[1])

                        
