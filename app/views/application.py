from sanic.views import HTTPMethodView
from sanic.response import json as json_response
from fdk_client.platform.PlatformClient import PlatformClient
import ujson

# Get all applications
class ApplicationData(HTTPMethodView):

    async def get(self, request):
        try:

            platform_client: PlatformClient = request.conn_info.ctx.platform_client
            response = await platform_client.configuration.getApplications(page_size=1000, q=ujson.dumps({"is_active": True}))

            return json_response(response["json"], status=200)
        except Exception as e:
            return json_response({"Error": str(e)}, status=400)

