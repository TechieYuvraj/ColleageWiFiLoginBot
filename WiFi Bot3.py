import urllib.parse
import urllib.request
import time

def connect_to_wifi(username, password):
    login_url = "http://10.17.0.1:1000/login?051a89e966e12d73"  # Replace with your college WiFi login URL

    while True:
        try:
            response = urllib.request.urlopen(login_url)
            if response.getcode() == 200:
                # Already connected to WiFi
                print("Connected to WiFi!")
            elif response.getcode() == 302:
                # Redirected to login page
                print("Logging in...")
                data = urllib.parse.urlencode({
                    "username": username,
                    "password": password
                }).encode()
                response = urllib.request.urlopen(login_url, data)
                if response.getcode() == 200:
                    print("Successfully logged in!")
                else:
                    print("Failed to log in.")
            else:
                print("Failed to connect to WiFi.")
        except urllib.error.URLError as e:
            print("Error:", e)

        # Wait for 1 hour before checking the connection again
        time.sleep(3600)

# Usage
username = "22gitcse13"
password = "yuvraj789"

connect_to_wifi(username, password)
