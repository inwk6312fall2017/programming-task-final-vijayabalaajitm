lass JoeSandbox(object)

    __init__(self, apikey='', apiurl='https://jbxcloud.joesecurity.org/api',
                   accept_tac=False, timeout=None, verify_ssl=True, retries=3)
        Create a JoeSandbox object.

        Parameters:
          apikey:     the api key
          apiurl:     the api url
          accept_tac: Joe Sandbox Cloud requires accepting the Terms and Conditions.
                      https://jbxcloud.joesecurity.org/resources/termsandconditions.pdf
          timeout:    Timeout in seconds for accessing the API. Raises a ConnectionError on timeout.
          verify_ssl: Enable or disable checking SSL certificates.
          retries:    Number of times requests should be retried if they timeout.

    account_info(self)
        username = input(unsername:)
        password = input(password:)
