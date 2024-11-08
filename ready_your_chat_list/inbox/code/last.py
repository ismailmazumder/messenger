import os
os.chdir("/home/ismail/Downloads/facebook-imismailhan-25_10_2024-VviGhnRP/your_facebook_activity/messages/inbox")
now_path = os.getcwd()
from bs4 import BeautifulSoup
litsdir = os.listdir()
from lxml import  html
import csv

# Function to append data to the CSV file
def append_to_csv(sender, message, csv_filename='sigma.csv'):
    with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write data
        writer.writerow([sender, message])

    print(f"Data appended: {sender}, {message}")
append_to_csv("sender","message")
for path, fol, file in os.walk(now_path):
    for new in file:
        # print(os.path.join(path, new))  # Prints full file path


        # print(os.path.join(path, new))
        
        if ".html" in new:
            html_path =  os.path.join(path, new)
            # print(html_path)
            with open(html_path,'rb') as html_code:
                html_code = html_code.read()
                # print(html_code)
                # soup = BeautifulSoup(html_code,'html.parser')
                
            messages = []
            soup = BeautifulSoup(html_code, 'html.parser')

            # Extract relevant data; adjust the class name based on your HTML structure
            for message in soup.find_all('div', class_='_a6-g'):  # Adjust class as necessary
                # Assuming the sender and message are in different spans or divs
                sender_elem = message.find('div', class_='_2ph_ _a6-h _a6-i')  # Assuming this class corresponds to the sender
                message_elem = message.find('div', class_='_2ph_ _a6-p')  # Assuming this class corresponds to the message
                if sender_elem:
                    # print(sender_elem.text.strip(),message_elem.text.strip())
                    append_to_csv(sender_elem.text.strip(),message_elem.text.strip())
                else:
                    print("Sender element not found")

            
                    
        

        
