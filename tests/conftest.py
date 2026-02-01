import pytest
from playwright.sync_api import Playwright
import json
from utils.apiutils.login_api import ApiLogin
from utils.apiutils.checkout import CheckandAddress
from utils.apiutils.productadd import AddProductCart

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default = "chrome")

@pytest.fixture()
def browsersetup(playwright:Playwright,request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    
with open("data/credentials.json") as f:
    data = json.load(f)
    cred = data['users']

@pytest.fixture(params = cred, scope="session")
def credential(request):
    return request.param

@pytest.fixture(scope = "session")
def api_session(playwright,credential):
    apilogin  = ApiLogin()
    session = apilogin.loginapi(playwright,credential)
    return session

@pytest.fixture()
def api_context(playwright:Playwright, api_session):
    context = playwright.request.new_context(base_url = "https://demowebshop.tricentis.com",storage_state=api_session)
    yield context
    context.dispose()

@pytest.fixture(scope = "session")
def products():
    with open("data/products.json") as f:
        data = json.load(f)
        return data['products']
    
@pytest.fixture()
def addprodcart(api_context, products):
    addprod = AddProductCart()
    addprod.producttocart(api_context,products)
    return True

    
@pytest.fixture()
def orderId(api_context):

    check = CheckandAddress()

    check.proceed_to_checkout(api_context)
    check.save_billing(api_context)
    check.save_shipping(api_context)
    check.save_shipping_method(api_context)
    check.save_payment_method(api_context)
    check.save_payment_info(api_context)
    check.confirm_order(api_context)
    orderId = check.retrieve_order_number(api_context)
    return orderId
