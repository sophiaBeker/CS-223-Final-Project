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

# FILE MANAGEMENTS
def load_accounts(self):
    if not os.path.exists(self.account_file):
        return {}
    
    try: 
        with open(self.account_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            print("[ERROR] Account file was not formatted correctly.")
            return {}
    except json.JSONDecodeError:
        print("[ERROR] account_management.json was invalid.")
    except OSError as error:
        print("[ERROR] - Could not read file: {error}")
        return {}

def save_accounts(self):
    try: 
        with open(self.account_file, "w", encoding="utf-8") as file:
            json.dump(self.accounts, file, indent=4)
    except OSError as error:
        print(f"[ERROR] Cannot save account data: {error}")