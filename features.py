import json
import os
from datetime import datetime

ACCOUNT_FILE = "account_management.json"
MESSAGE_FILE = "message_log.txt"


class SocialMediaApp:
    def __init__(self, account_file=ACCOUNT_FILE, message_file=MESSAGE_FILE):
        self.account_file = account_file
        self.message_file = message_file
        self.current_user = None
        self.accounts = self.load_accounts()
        self.ensure_rqeuired_instructor_account()
        self.ensure_message_file()

