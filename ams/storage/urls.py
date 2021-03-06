import tornado.web
import settings
from ams.storage import views

storage_router = tornado.web.Application([
        	(settings.ENDPOINTS["storage"], views.StorageHandler)
        ], debug=settings.DEBUG)