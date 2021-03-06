from utils.tornado_components.web import RobustTornadoClient, SignedTornadoClient
from .account_attributes import Balance, Blockchain
from .permissions import Permissions
import settings


class AbstractClass(object):
    pass


class Account(AbstractClass):
    balance = Balance()
    blockchain = Blockchain()
    permissions = Permissions()
    client_storage = SignedTornadoClient(settings.storageurl)

    async def createaccount(self, **params):
        result = await self.client_storage.request(method_name="createaccount",
                                                   **params)
        return result

    async def getaccountdata(self, **params):
        result = await self.client_storage.request(method_name="getaccountdata",
                                                   **params)
        return result

    async def createwallet(self, **params):
        result = await self.client_storage.request(method_name="createwallet",
                                                   **params)
        return result

    async def getnews(self, **params):
        result = await self.client_storage.request(method_name="getnews",
                                                   **params)
        return result

    async def setnews(self, **params):
        result = await self.client_storage.request(method_name="setnews",
                                                   **params)
        return result

    async def getaccountbywallet(self, **params):
        result = await self.client_storage.request(method_name="getaccountbywallet",
                                                   **params)
        return result

    async def updatelevel(self, **params):
        result = await self.client_storage.request(method_name="updatelevel",
                                                   **params)
        return result

    async def insertoffer(self, **params):
        result = await self.client_storage.request(method_name="insertoffer",
                                                   **params)
        return result

    async def getoffer(self, **params):
        result = await self.client_storage.request(method_name="getoffer",
                                                   **params)
        return result

    async def removeoffer(self, **params):
        result = await self.client_storage.request(method_name="removeoffer",
                                                   **params)
        return result

    async def updateoffer(self, **params):
        result = await self.client_storage.request(method_name="updateoffer",
                                                   **params)
        return result

    async def mailedconfirm(self, **params):
        result = await self.client_storage.request(method_name="mailedconfirm",
                                                   **params)
        return result

    async def getoffers(self, **params):
        result = await self.client_storage.request(method_name="getoffers",
                                                   **params)
        return result

    async def getuserscontent(self, **params):
        result = await self.client_storage.request(method_name="getuserscontent",
                                                   **params)
        return result

    async def setuserscontent(self, **params):
        result = await self.client_storage.request(method_name="setuserscontent",
                                                   **params)
        return result

    async def updateuserscontent(self, **params):
        result = await self.client_storage.request(method_name="updateuserscontent",
                                                   **params)
        return result

    async def getallcontent(self):
        result = await self.client_storage.request(method_name="getallcontent")
        return result

    async def getsinglecontent(self, cid):
        result = await self.client_storage.request(method_name="getsinglecontent",
                                                   cid=cid)
        return result

    async def changecontentowner(self, **params):
        result = await self.client_storage.request(method_name="changecontentowner",
                                                   **params)
        return result

    async def setaccessstring(self, **params):
        result = await self.client_storage.request(method_name="setaccessstring",
                                                   **params)
        return result

    
    async def getreviews(self, **params):
        result = self.client_storage.request(method_name="getreviews",
                                             **params)
        return result

    
    async def setreview(self, **params):
        result = self.client_storage.request(method_name="setreview",
                                             **params)
        return result

    
    async def updatereview(self, **params):
        result = self.client_storage.request(method_name="updatereview",
                                             **params)
        return result

    
    async def writedeal(self, **params):
        result = self.client_storage.request(method_name="writedeal",
                                             **params)
        return result

    
    async def getdeals(self, **params):
        result = self.client_storage.request(method_name="getdeals",
                                             **params)
        return result

    
    async def updatedescription(self, **params):
        result = self.client_storage.request(method_name="updatedescription",
                                             **params)
        return result

    
    async def setwriteprice(self, **params):
        result = self.client_storage.request(method_name="setwriteprice",
                                             **params)
        return result

    
    async def setreadprice(self, **params):
        result = self.client_storage.request(method_name="setreadprice",
                                             **params)
        return result

    
    async def changeowner(self, **params):
        result = self.client_storage.request(method_name="changeowner",
                                             **params)
        return result

    
    async def sharecontent(self, **params):
        result = self.client_storage.request(method_name="sharecontent",
                                             **params)
        return result