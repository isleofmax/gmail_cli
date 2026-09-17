import base64
import datetime as dt
import email
from Command import Command
from email import policy
from googleapiclient.discovery import Resource
from StateClient import StateClient


class ListCommand(Command):
    def get_messages(self, state: StateClient, service: Resource, results: Resource) -> None:
        if results["resultSizeEstimate"] == 0:
            return

        state.message_ids = []
        index = 0
        for message in results["messages"]:
            # Append the message ID to the list of ID's in the state class
            state.message_ids.append(message["id"])

            # Get the e-mail in raw format
            msg_detail = service.users().messages().get(userId="me", id=message["id"], format="raw").execute()

            # Decode from Base64 in bytes
            msg_bytes = base64.urlsafe_b64decode(msg_detail["raw"].encode("ASCII"))

            # Decode from bytes in mime format
            mime_msg = email.message_from_bytes(msg_bytes, policy=policy.default)

            # Get the from, subject, and date property of the e-mail
            msg_from = mime_msg["from"]
            msg_subject = mime_msg["subject"]
            msg_date = mime_msg["date"]

            # Print the subject of the e-mail with date and from properties
            index += 1
            utc_date = dt.datetime.strptime(msg_date,"%a, %d %b %Y %H:%M:%S %z")
            date_now = utc_date.astimezone()
            date_str = f"{date_now.day:02}/{date_now.month:02}/{date_now.year:4} {date_now.hour:02}:{date_now.minute:02}"
            if "UNREAD" in msg_detail["labelIds"]:
                green_color = "\033[32m"
                reset_color = "\033[0m"
                print(f"{green_color}Message {index:2}: Date {date_str} From {msg_from}")
                print(f"            Subject: {msg_subject[:150]}{reset_color}")
            else:
                print(f"Message {index:2}: Date {date_str} From {msg_from}")
                print(f"            Subject: {msg_subject[:150]}")
            print()


