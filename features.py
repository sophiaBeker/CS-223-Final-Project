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
def send_message(self, recipient, message):
    """
    Send a message from the current logged-in user to another user.
    """

    # Make sure someone is logged in
    if not self.current_user:
        print("[ERROR] You must be logged in to send messages.")
        return

    # Make sure recipient exists
    if recipient not in self.accounts:
        print("[ERROR] Recipient account does not exist.")
        return

    timestamp = self.timestamp()

    try:
        with open(self.message_file, "a") as file:
            file.write(
                f"{timestamp} | FROM: {self.current_user} | "
                f"TO: {recipient} | MESSAGE: {message}\n"
            )

        print("[SUCCESS] Message sent.")

    except OSError as error:
        print(f"[ERROR] Could not send message: {error}")


def read_messages(self):
    """
    Read all messages sent to the current logged-in user.
    """

    # Make sure someone is logged in
    if not self.current_user:
        print("[ERROR] You must be logged in to read messages.")
        return

    try:
        with open(self.message_file, "r") as file:
            messages = file.readlines()

        print("\n=== YOUR MESSAGES ===")

        found = False

        for msg in messages:
            if f"TO: {self.current_user}" in msg:
                print(msg.strip())
                found = True

        if not found:
            print("No messages found.")

    except OSError as error:
        print(f"[ERROR] Could not read messages: {error}")

# ADDITIONAL FEATURES OF OUR CHOICE
# update bio [fio] + follow/unfollow users [sophia]

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

def follow_user(self, username):
    """
    Follow another user by username.
    """

    # Must be logged in
    if not self.current_user:
        print("[ERROR] You must be logged in.")
        return

    # User cannot follow themselves
    if username == self.current_user:
        print("[ERROR] You cannot follow yourself.")
        return

    # Check if account exists
    if username not in self.accounts:
        print("[ERROR] User does not exist.")
        return

    # Create following list if missing
    if "following" not in self.accounts[self.current_user]:
        self.accounts[self.current_user]["following"] = []

    # Prevent duplicate follows
    if username in self.accounts[self.current_user]["following"]:
        print("[ERROR] You already follow this user.")
        return

    # Add user to following list
    self.accounts[self.current_user]["following"].append(username)

    # Save changes
    self.save_accounts()

    print(f"[SUCCESS] You are now following {username}.")


def unfollow_user(self, username):
    """
    Unfollow another user by username.
    """

    # Must be logged in
    if not self.current_user:
        print("[ERROR] You must be logged in.")
        return

    # Check if following list exists
    if "following" not in self.accounts[self.current_user]:
        print("[ERROR] You are not following anyone.")
        return

    # Check if user is currently followed
    if username not in self.accounts[self.current_user]["following"]:
        print("[ERROR] You are not following this user.")
        return

    # Remove user
    self.accounts[self.current_user]["following"].remove(username)

    # Save changes
    self.save_accounts()

    print(f"[SUCCESS] You unfollowed {username}.")

#HELPER: check followed accounts
def view_following(self):
    """
    View all followed users.
    """

    if not self.current_user:
        print("[ERROR] You must be logged in.")
        return

    following = self.accounts[self.current_user].get("following", [])

    print("\n=== FOLLOWING ===")

    if not following:
        print("You are not following anyone.")
        return

    for user in following:
        print(f"- {user}")

# MENU (or move to main?) 
# basic terminal menu [sophia]