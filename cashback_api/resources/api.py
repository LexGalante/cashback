from flask_restful import Api
from routes.reseller_register_router import ResellerRegisterRouter
from routes.auth_router import AuthRouter
from routes.reseller_router import ResellerRouter
from routes.bonus_router import BonusRouter
from routes.purchase_router import PurchaseRouter
from routes.cashback_router import CashbackRouter

api = Api(prefix="/api/v1")


def configure_api(app):
    """
    Inject routes and another configurations
    """
    # injecting routes
    api.add_resource(AuthRouter, "/auth")
    api.add_resource(ResellerRegisterRouter, "/reseller/register")
    api.add_resource(ResellerRouter, "/reseller",
                                     "/reseller/<int:page>/<int:page_size>",
                                     "/reseller/<string:cpf>")
    api.add_resource(BonusRouter, "/bonus")
    api.add_resource(PurchaseRouter, "/purchase")
    api.add_resource(CashbackRouter, "/cacheback")
    # initialize flask restful
    api.init_app(app)
