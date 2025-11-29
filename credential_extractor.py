import requests
from bs4 import BeautifulSoup

def extract_credentials(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all input fields
        inputs = soup.find_all('input')
        
        credentials = []
        
        for input_field in inputs:
            # Check if input field has type 'text' or 'password'
            if input_field.get('type') in ['text', 'password']:
                # Extract username and password values
                username = input_field.get('name')
                password = input_field.get('name')
                
                if username and password:
                    credentials.append((username, password))
        
        return credentials
    
    except Exception as e:
        print(f"Error extracting credentials: {e}")
        return []

# Example usage
url = 'http://78.142.47.33/fileadmin/'
credentials = extract_credentials(url)

if credentials:
    for username, password in credentials:
        print(f"Username: {username}, Password: {password}")
else:
    print("No credentials found.")
