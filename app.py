import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from pymessenger.bot import Bot
import sqlite3
nos=1
app = Flask(__name__)
ACCESS_TOKEN = 'EAACnRSZCx3LUBAGfxVUxkyna6RQBqrOMXZA18ACzFHh1oZBmo3WmOI8J4YRbsUbQmZCz1vAHcqStZAkf38POlGcW7587ibKgEPS4LeC7VLKyemWf2ZCOcZC5AwfCtmwIkPZCbNWVci6ZABZAVUqtFZAWshiZBXrLqgwWM3Smn8iiFLM6cAZDZD'
VERIFY_TOKEN = 'ladkidedo'
bot = Bot(ACCESS_TOKEN)
    


def Creator(tb_name):
    import sqlite3
    conn = sqlite3.connect("Daaa.db")
    cursor = conn.cursor()
    create_table = "CREATE TABLE %s (id INT, name TEXT , price INT)" %tb_name
    try:
        cursor.execute(create_table)
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        return "Table already Created, Or DATABASE is locked "
        
    
def Destructor(tb_name):
    conn = sqlite3.connect("Daa.db")
    cursor = conn.cursor()
    q = "DROP TABLE %s" %tb_name
    cursor.execute(q)
    conn.commit()
    conn.close()
    
def Inserter(database,table_name,obj_values):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    insert_q = "INSERT INTO %s VALUES (?,?,?)" %table_name 
    cursor.execute(insert_q,obj_values)
    conn.commit()
    conn.close
    
def Printer(database,table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    insert_q = "SELECT * FROM %s" %table_name 
    for row in cursor.execute(insert_q):
        print(row)
    conn.commit()
    conn.close

def Printer_specific(database,table_name,obj_values):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    insert_q = "SELECT * FROM %s WHERE id=%s" %(table_name,obj_values[0])
    for row in cursor.execute(insert_q):
        print(row)
    conn.commit()
    conn.close
    
Creator("Prices")
nos=1
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    global nos
                    nos+=1
                    k=message['message'].get('text')
                    #response_sent_text = get_message()
                    send_message(recipient_id,k)
                    til=title(amazon_pricer(k)[1])
                    if til!="Nuffin":
                        price=casher((amazon_pricer(k)[0]),k)
                        k=(nos,til,price)
                        Inserter("Daaa.db","Prices",k)
                    else:
                        return ("Invalid Url : Unable to attain the price ")
                    #price[title(amazon_pricer(k)[1])]=(casher(amazon_pricer(k)[0]))
                    #print(type(casher(amazon_pricer(k))))
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    #Sresponse_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    print(k)
    return ("Success")

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def amazon_pricer(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    try:
        res = requests.get(url,headers = headers,verify=True)
    except requests.exceptions.MissingSchema:
        return (1,1)
    if res.status_code==200:
        soup = BeautifulSoup(res.text,'lxml')
        x= "#result_0 > div > div.a-fixed-left-grid > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(3) > div.a-column.a-span7 > div:nth-child(2) > a"
        y="#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > div:nth-child(1) > a > h2"
        y= y.replace("nth-child","nth-of-type")
        x= x.replace("nth-child","nth-of-type")
        return (soup.select(x),soup.select(y))
    else:
        return "Site nein Diya Dhokha, Ye abhi nahi Hoga"

def title(str1):
    ##result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > div:nth-child(1) > a > h2
    if str1==[] or str1==1:
        return "Nuffin"
    else:
        str1 = str(str1[0])
        name="data-attribute="
        len_name = len(name)
        i = str1.index(name)
        j= str1.index("data-max-rows")
        return str1[i+1+len_name:j-2]
        

def casher(str1,url):
    try1=0
    #use regex for single number price as < will be inclded
    if str1==1:
        return "Nuffin"
    if str1==[]:
        try1+=1
        return casher(amazon_pricer(url),url)
    if try1==2:
        return "None"
    str1 = str(str1[0])
    pricew = "sx-price-whole"
    len_pricew = len(pricew)
    try:
        i = str1.index(pricew)
    except ValueError:
        return "Aroar"
    pricef = "sx-price-fractional"
    len_pricef = len(pricef)
    try:
        j = str1.index(pricef)
    except ValueError:
        return "Aroar"
    k=str(str1[i+len_pricew+2:4+i+len_pricew]+"."+str1[j+len_pricef+2:j+len_pricef+4])
    k = k.replace("<","")
    return k


#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"




if __name__ == "__main__":
    app.run()
