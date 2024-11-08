import os
os.chdir("/home/ismail/Downloads/facebook-imismailhan-25_10_2024-VviGhnRP/your_facebook_activity/messages/inbox")
from bs4 import BeautifulSoup
litsdir = os.listdir()
from lxml import  html
print(litsdir[1])
for new in litsdir:
    fol_path = os.path.join(os.getcwd(),new)
    
    # print(fol_path)
    try:
        html_files = os.listdir(fol_path)
        # print(html_files)
        for new_ in html_files:
            if ".html" in new_:
                html_path = os.path.join(fol_path,new_)
                # print(html_path)
                with open(html_path,'rb') as html_code:
                    html_code = html_code.read()
                    # print(html_code)
                    # soup = BeautifulSoup(html_code,'html.parser')
                    soup = html.fromstring(html_code)
                messages = []
                sender = soup.xpath('/html/body/div/div/div/div/div[2]/div[14]/div[1]')
                message = soup.xpath('/html/body/div/div/div/div/div[2]/div[14]/div[2]/div/div[2]')
                print("love")
                print(fol_path)
                for sender_trans,message_trnas in zip(sender,message):
                    print(sender_trans.text_content().strip(),message_trnas.text_content().strip()) 
                
                # for loveeee in sender:
                #     print(loveeee.text_content().strip()) 
                
                
                

    except Exception as e:
        print("error",e)
    
    # for new_ in html_files:
    #     if "html" in  new_:
    #         final_path = os.path.join(fol_path+new_)
            # soup = BeautifulSoup(final_path,'html.parser')
