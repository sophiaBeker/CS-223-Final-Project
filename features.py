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

def username_exists(self, username):
    return username in self.accounts

def is_logged_in(self):
    return self.current_user is not None

def require_login(self):
    if not self.is_logged_in():
        print("[ERROR] You need to be logged to use this feature.")
        return False
    return True

def valid_username(self, username):
    if not username:
        return False, "Username cannot be empty."
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    if " " in username:
        return False, "Username cannot contain spaces."
    if not username.replace("_", "").isalnum():
        return False, "Username can only contain letters, numbers, and underscores."
    return True, ""

def valid_password(self, password):
    if not password: 
        return False, "Password cannot be empty."
    if len(password) < 3:
        return False, "Password must be at least 3 characters long."
    return True, ""

# ACCOUNT FEATURES
# create acct [fio]
# login, logout, change pass, delete acct [sophia]

def create_account(self):
    username = input("Choose a username: ").strip()
    valid, message = self.valid_username(username)
    if not valid:
        print(f"[ERROR] {message}")
        return
    if self.username_exists(username):
        print("[ERROR] Username already exists.")
        return
    
    password = input ("Choose a password: ").strip()
    valid, message = self.valid_password(password)
    if not valid:
        print(f"[ERROR] {message}")
        return

    self.accounts[username] = {
        "password": password,
        "bio": "", 
        "created_at": self.timestamp(),
    }

    self.save_accounts()
    print(f"Account created successfully for {username}")


# MESSAGING FEATURES
# send msg, read msg

# ADDITIONAL FEATURES OF OUR CHOICE
# update bio [fio] + other feature [sophia]

def update_bio(self):
    if not self.require_login():
        return
    
    bio = input("Enter your new bio/status: ").strip()
    if len(bio) > 120:
        print("[ERROR] Bio/status must be 120 characters or fewer.")
        return
    
    self.accounts[self.current_user]["bio"] = bio
    self.save_accounts()
    print("Bio/status updated successfullly.")

# MENU (or move to main?) 
# basic terminal menu [sophia]