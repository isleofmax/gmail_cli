from google.oauth2.credentials import Credentials

class StateClient():
    labels: list[dict[str, str]] = [] # the tuple contains the "id" and "name" of the label
    curr_label: int = 0
    next_endpoint: str = ""
    prev_endpoint: str = ""
    creds: Credentials = None
