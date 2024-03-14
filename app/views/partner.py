from sanic.views import HTTPMethodView
from sanic.response import json as json_response
from fdk_client.partner import PartnerClient

class PartnerData(HTTPMethodView):

    async def get(self, request):
        try:
            partner_client: PartnerClient = request.conn_info.ctx.partner_client
            
            response = await partner_client.theme.getOrganizationThemes()

            return json_response(response["json"], status=200)
        except Exception as e:
            return json_response({"Error": str(e)}, status=400)

