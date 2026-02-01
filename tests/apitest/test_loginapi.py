from playwright.sync_api import Playwright
from utils.apiutils.login_api import ApiLogin

def test_loginapi(api_session):
    assert api_session is not None