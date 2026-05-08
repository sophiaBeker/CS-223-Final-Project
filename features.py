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
        self.ensure_required_instructor_account()
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
            return {}
        except OSError as error:
            print(f"[ERROR] - Could not read file: {error}")
            return {}

    def save_accounts(self):
        try: 
            with open(self.account_file, "w") as file:
                json.dump(self.accounts, file, indent=4)
        except OSError as error:
            print(f"[ERROR] Cannot save account data: {error}")

    def ensure_message_file(self):
        if not os.path.exists(self.message_file):
            try:
                with open(self.message_file, "w") as file:
                    file.write("Message Log\n")
                    file.write("===========\n")
            except OSError as error:
                print (f"[ERROR] Could not make message log: {error}")

    def ensure_required_instructor_account(self):
        if "instructor" not in self.accounts:
            self.accounts["instructor"] = {
                "password": "123",
                "bio": "instructor's test account",
                "account_created": self.timestamp()
            }
            self.save_accounts()

    def timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    # HELPERS

    # check if user exists
    def username_exists(self, username):
        return username in self.accounts

    # ensure user is logged in
    def is_logged_in(self):
        return self.current_user is not None

    # user cannot use features unless logged in 
    def require_login(self):
        if not self.is_logged_in():
            print("[ERROR] You need to be logged to use this feature.")
            return False
        return True

    # username validation 
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

    # password validation
    def valid_password(self, password):
        if not password: 
            return False, "Password cannot be empty."
        if len(password) < 3:
            return False, "Password must be at least 3 characters long."
        return True, ""

    # ACCOUNT FEATURES

    # have user create their acct (user + pass)
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
            "following": [],
            "created_at": self.timestamp()
        }

        self.save_accounts()
        print(f"Account created successfully for {username}")

    #login to an existing account
    def login(self, username, password):
        """
        Log into an existing account.
        """

        # Check if username exists
        if username not in self.accounts:
            print("[ERROR] Username does not exist.")
            return

        # Check password
        if self.accounts[username]["password"] != password:
            print("[ERROR] Incorrect password.")
            return

        # Set current user
        self.current_user = username

        print(f"[SUCCESS] Logged in as {username}.")

    #logout of the current account
    def logout(self):
        """
        Log out of the current account.
        """

        if not self.current_user:
            print("[ERROR] No user is currently logged in.")
            return

        print(f"[SUCCESS] {self.current_user} has logged out.")

        self.current_user = None

    #change password
    def change_password(self, old_password, new_password):
        """
        Change the password of the currently logged-in user.
        """

        # Must be logged in
        if not self.current_user:
            print("[ERROR] You must be logged in.")
            return

        # Verify old password
        if self.accounts[self.current_user]["password"] != old_password:
            print("[ERROR] Old password is incorrect.")
            return

        # Update password
        self.accounts[self.current_user]["password"] = new_password

        # Save changes
        self.save_accounts()

        print("[SUCCESS] Password updated.")

    #delete account
    def delete_account(self, password):
        """
        Delete the currently logged-in account.
        """

        # Must be logged in
        if not self.current_user:
            print("[ERROR] You must be logged in.")
            return

        # Confirm password
        if self.accounts[self.current_user]["password"] != password:
            print("[ERROR] Incorrect password.")
            return

        username = self.current_user

        # Delete account
        del self.accounts[username]

        # Save changes
        self.save_accounts()

        # Log out user
        self.current_user = None

        print(f"[SUCCESS] Account '{username}' deleted.")


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

    # have user create a bio
    def update_bio(self):
        if not self.require_login():
            return
        
        bio = input("Enter your new bio/status: ").strip()
        if len(bio) > 120:
            print("[ERROR] Bio/status must be 120 characters or fewer.")
            return
        
        self.accounts[self.current_user]["bio"] = bio
        self.save_accounts()
        print("Bio/status updated successfully.")

    # view ALL users on the platform, their bio, and when their acct was created
    def view_users(self):
        print("\n ===== USERS =====")
        for username in sorted(self.accounts):
            bio = self.accounts[username].get("bio", "")
            created_at = self.accounts[username].get("created_at", "unknown date")
            print(f"{username} | Bio: {bio if bio else '(no bio)'} | Account Created: {created_at}")

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
