import os
from bs4 import BeautifulSoup

# Define the path to the 'inbox' directory
inbox_directory = os.getcwd()

# Iterate over each subfolder within the 'inbox' directory
for folder in os.listdir(inbox_directory):
    folder_path = os.path.join(inbox_directory, folder)
    
    # Check if it's indeed a folder (not a file)
    if os.path.isdir(folder_path):
        # Define the path to the 'message_1.html' file
        html_file_path = os.path.join(folder_path, 'message_1.html')
        
        # Check if the 'message_1.html' file exists
        if os.path.exists(html_file_path):
            # Read the content of the HTML file
            with open(html_file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract relevant data, for example, message text or timestamps
            # (this part depends on the structure of your HTML content)
            messages = []
            for message in soup.find_all('div', class_='_a6-g'):
                messages.append(message.text)
            
            # Print or process the extracted messages
            print(f"Messages from folder '{folder}':")
            for msg in messages:
                print(msg)
                
            print("\n" + "="*50 + "\n")
        else:
            print(f"No 'message_1.html' file found in folder '{folder}'")
