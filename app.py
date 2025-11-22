from security import sanitize_input, is_strong_password
from utils import log_event

def user_login(username, password):
    log_event("Login attempt")

    # Validate username
    username = sanitize_input(username)

    # Password security check
    if not is_strong_password(password):
        return {"status": "error", "msg": "Weak Password. Use strong password."}

    # Simulated secure logic
    if username == "admin" and password == "Admin@123":
        return {"status": "success", "msg": "Login successful"}
    else:
        return {"status": "error", "msg": "Invalid credentials"}


if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(user_login(user, pwd))
