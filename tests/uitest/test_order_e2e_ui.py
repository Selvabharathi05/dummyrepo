from utils.uiutils.uilogin import UILogin
from utils.uiutils.uiorderdetail import OrderDetail
from utils.uiutils.uivalidateorder import ValidateOrder
from utils.uiutils.uiorders import Orders

def test_validare_order(page,credential,orderId,products):

    UILogin(page).loginto(credential)
    Orders(page).navigate_to_orders()
    OrderDetail(page).navigate_to_orderdetails(orderId)
    ValidateOrder(page).validate_order(products)
