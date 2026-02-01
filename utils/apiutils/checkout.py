import re
class CheckandAddress:

    def proceed_to_checkout(self,api_context):

        payload = {
            "CountryId" : 41,
            "StateProvinceId" : 0,
            "ZipPostalCode" : 123456,
            "termsofservice" : "on",
            "checkout" : "checkout" 
        }
        # https://demowebshop.tricentis.com/cart
        response = api_context.post("/cart", form = payload)
        assert response.ok, "Something went wrong"

    def save_billing(self,api_context):
       payload = {
           "BillingNewAddress.Id": "0",
           "BillingNewAddress.FirstName": "Alves",
           "BillingNewAddress.LastName": "Tester",
           "BillingNewAddress.Email": "bharathiselva23@gmail.com",
           "BillingNewAddress.Company": "",
           "BillingNewAddress.CountryId": "41",
           "BillingNewAddress.StateProvinceId": "0",
           "BillingNewAddress.City": "Banglore",
           "BillingNewAddress.Address1": "2nd street",
           "BillingNewAddress.Address2": "",
           "BillingNewAddress.ZipPostalCode": "123456",
           "BillingNewAddress.PhoneNumber": "1234567890",
           "BillingNewAddress.FaxNumber": ""
       }
       # https://demowebshop.tricentis.com/checkout/OpcSaveBilling/
       response = api_context.post("/checkout/OpcSaveBilling/", form = payload)
       assert response.ok

    def save_shipping(self,api_context):

        payload = {
            "shipping_address_id" : "0",
            "ShippingNewAddress.Id" : "0",
            "ShippingNewAddress.FirstName" : "Alves",
            "ShippingNewAddress.LastName" : "Tester",
            "ShippingNewAddress.Email" : "bharathiselva23@gmail.com",
            "ShippingNewAddress.Company" : "",
            "ShippingNewAddress.CountryId" : "41",
            "ShippingNewAddress.StateProvinceId" : "0",
            "ShippingNewAddress.City" : "Banglore",
            "ShippingNewAddress.Address1": "2nd street",
            "ShippingNewAddress.Address2" : "",
            "ShippingNewAddress.ZipPostalCode" : "123456",
            "ShippingNewAddress.PhoneNumber" : "1234567890",
            "ShippingNewAddress.FaxNumber" : "",
            "PickUpInStore" : "false"
        }

        #https://demowebshop.tricentis.com/checkout/OpcSaveShipping/

        response = api_context.post("/checkout/OpcSaveShipping/", form = payload)
        assert response.ok

    def save_shipping_method(self,api_context):

        payload = {
            "shippingoption" : "Ground___Shipping.FixedRate"
        }
        response = api_context.post("/checkout/OpcSaveShippingMethod/", form = payload)
        assert response.ok

    def save_payment_method(self,api_context):

        payload = {
            "paymentmethod": "Payments.CashOnDelivery"
        }

        response = api_context.post("/checkout/OpcSavePaymentMethod/", form = payload)
        assert response.ok

    def save_payment_info(self, api_context):

        response = api_context.post("/checkout/OpcSavePaymentInfo/", form = {})
        assert response.ok

    def confirm_order(self,api_context):

        response = api_context.post("/checkout/OpcConfirmOrder/")
        assert response.ok

    def retrieve_order_number(self, api_context):
        #https://demowebshop.tricentis.com/checkout/completed/
        response = api_context.get("/checkout/completed/")
        assert response.ok
        
        match = re.search(r"Order number:\s(\d+)", response.text())
        orderId = match.group(1)
        return orderId
    



