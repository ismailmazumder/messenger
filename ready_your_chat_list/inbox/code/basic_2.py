import os
import csv
from bs4 import BeautifulSoup

# Define the path to the 'inbox' directory
inbox_directory = os.getcwd()

# Create a list to hold message data
all_messages = []

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
            
            # Extract relevant data; adjust the class name based on your HTML structure
            for message in soup.find_all('div', class_='_a6-g'):  # Adjust class as necessary
                # Assuming the sender and message are in different spans or divs
                sender_elem = message.find('div', class_='_a70e')  # Assuming this class corresponds to the sender
                message_elem = message.find('div', class_='_aoa9')  # Assuming this class corresponds to the message
 # Adjust as necessary
                print(sender_elem,message_elem)
                if sender_elem and message_elem:
                    sender = sender_elem.text.strip()
                    message_text = message_elem.text.strip()
                    print(message_text)
                    all_messages.append((sender, message_text))

        else:
            print(f"No 'message_1.html' file found in folder '{folder}'")

# Save the extracted messages to a CSV file
csv_file_path = 'messages.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Sender', 'Message'])  # Write header
    csv_writer.writerows(all_messages)  # Write all message data

print(f"Messages have been saved to '{csv_file_path}'.")
