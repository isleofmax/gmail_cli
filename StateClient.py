from google.oauth2.credentials import Credentials

class StateClient():
    labels: list[dict[str, str]] = [] # the tuple contains the "id" and "name" of the label
    ids: list[str] = []
    curr_label: int = 0
    next_tokens: list[str] = []
    creds: Credentials = None
