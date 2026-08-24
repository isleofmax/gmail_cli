from google.oauth2.credentials import Credentials

class StateClient():
    labels: list[dict[str, str]] = [] # the tuple contains the "id" and "name" of the label
    curr_label: int = 0
    next_token: str = ""
    prev_token: str = ""
    curr_token: str = ""
    first_next_token: str = ""
    creds: Credentials = None
