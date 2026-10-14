#Import relevant Plaid libraries and modules
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

#Import relevant credential management libraries and modules
from dotenv import load_dotenv
import os

#Load credentials for API pull
load_dotenv(dotenv_path=".env.sandbox")
client_id = os.getenv("CLIENTID")
secret = os.getenv("SECRET")

#Establish configuration used to build Plaid connection
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

#Build low-level client to handle Plaid connection
api_client = plaid.ApiClient(configuration)

#Build high-level client to facilitate coding
client = plaid_api.PlaidApi(api_client)

#Configure request for Plaid link token
request = LinkTokenCreateRequest(
    products=[Products('transactions')],
    client_name="JRM Budget Summary",
    country_codes=[CountryCode('US')],
    language='en',
    user=LinkTokenCreateRequestUser(
        client_user_id="JRM082192"
    )
)

#Execute request for Plaid link token
response = client.link_token_create(request)
link_token = response['link_token']

#Print link token to confirm success
print(link_token)