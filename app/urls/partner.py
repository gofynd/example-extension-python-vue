from sanic import Blueprint

from app.views.partner import PartnerData


# Create your blueprints here
partner_bp = Blueprint("partner_blueprint", url_prefix="/")

# Register routes into blueprints
partner_bp.add_route(PartnerData.as_view(), "/theme_list")



# Blueprint Group
bps = [
    partner_bp
]
partner_bp = Blueprint.group(*bps, url_prefix="/adm")

