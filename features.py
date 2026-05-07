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
        with open(self.account_file, "r") as file:
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
        with open(self.account_file, "w") as file:
            json.dump(self.accounts, file, indent=4)
    except OSError as error:
        print(f"[ERROR] Cannot save account data: {error}")

def msg_file_creation(self): 
    if not os.path.exists(self.message_file):
        try:
            with open(self.message_file, "w") as file:
                file.write("Message Log\n")
                file.write("===========\n")
        except OSError as error:
            print (f"[ERROR] Could not make message log: {error}")

def ensure_rqeuired_instructor_account(self):
    if "instructor" not in self.accounts:
        self.account["instructor"] = {
            "password": "123",
            "bio": "instructor's test account"
            "account_created": self.timestamp();
        }
        self.save_accounts()

def timestamp(self):
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# HELPERS
# username exits, logged in, require login, valid usrname, valid password

def username

# ACCOUNT FEATURES
# create acct, login, logout, change pass, delete acct, 


# MESSAGING FEATURES
# send msg, read msg

# ADDITIONAL FEATURES OF OUR CHOICE
# update bio + other feature

# MENU (or move to main?)
# basic terminal menu 