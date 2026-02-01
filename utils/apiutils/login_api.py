from playwright.sync_api import Playwright
import json
class ApiLogin:

    def loginapi(self,playwright:Playwright,credential):
        email = credential['email']
        password = credential['password']
        api_l = playwright.request.new_context(base_url="https://demowebshop.tricentis.com")
        response = api_l.post("/login", data= {"Email": email, "Password": password})
        assert response.status == 200

        session = api_l.storage_state()

        with open("data/session.json", 'w') as f:
            json.dump(session,f)
        api_l.dispose()
        return session