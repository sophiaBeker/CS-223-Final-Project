from features import SocialMediaApp


def display_menu():
    print("\n===== SOCIAL MEDIA APP =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Logout")
    print("4. Change Password")
    print("5. Delete Account")
    print("6. Send Message")
    print("7. Read Messages")
    print("8. Update Bio")
    print("9. Follow User")
    print("10. Unfollow User")
    print("11. View Following")
    print("12. Exit")


def main():
    app = SocialMediaApp()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        # CREATE ACCOUNT
        if choice == "1":
            app.create_account()

        # LOGIN
        elif choice == "2":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            app.login(username, password)

        # LOGOUT
        elif choice == "3":
            app.logout()

        # CHANGE PASSWORD
        elif choice == "4":
            old_password = input("Old password: ").strip()
            new_password = input("New password: ").strip()
            app.change_password(old_password, new_password)

        # DELETE ACCOUNT
        elif choice == "5":
            password = input("Enter password to confirm deletion: ").strip()
            app.delete_account(password)

        # SEND MESSAGE
        elif choice == "6":
            recipient = input("Recipient username: ").strip()
            message = input("Message: ").strip()
            app.send_message(recipient, message)

        # READ MESSAGES
        elif choice == "7":
            app.read_messages()

        # UPDATE BIO
        elif choice == "8":
            app.update_bio()

        # FOLLOW USER
        elif choice == "9":
            username = input("Enter username to follow: ").strip()
            app.follow_user(username)

        # UNFOLLOW USER
        elif choice == "10":
            username = input("Enter username to unfollow: ").strip()
            app.unfollow_user(username)

        # VIEW FOLLOWING
        elif choice == "11":
            app.view_following()

        # EXIT
        elif choice == "12":
            print("Goodbye!")
            break

        else:
            print("[ERROR] Invalid menu option.")


if __name__ == "__main__":
    main()
