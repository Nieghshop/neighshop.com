import flask  
from flask import *
import requests
from flask import Flask,session,render_template,redirect,request,g,url_for
import os
import os
from twilio.rest import Client
import random
from cryptography.fernet import Fernet



key = Fernet.generate_key()
cipher_suite = Fernet(key)




account_sid = 'AC02d04544f9a7051d87270ee723100387'
auth_token = '22b7c906971e450236481031b0847955'


client = Client(account_sid, auth_token)




app=Flask(__name__)


app.secret_key = os.urandom(24)
def generate_random_string(length):
     digits = "0123456789"
     a= ''.join(random.choice(digits) for i in range(length))
     print(a)
     return a


OTP = []
@app.route('/login', methods=['GET', 'POST'])



def login():
    if request.method == 'POST':
     
       
       
        # Store phone number in session
        session['user'] = request.form['phone_number']
        to_phone_number = "+91" +  str(request.form['phone_number'] )
        print(to_phone_number)
        otp_code = generate_random_string(5)

        message = f'This is otp for neighshop  {otp_code} DO NOT SHARE IT WITH ANYONE'
        from_phone_number = '+12762779220'
        message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
            )
        print(f'Message sent with ID: {message.sid}')
        otp_code=otp_code.encode('utf-8')
       
       
        

        
        
         
        




        # Generate and send OTP to phone number using SMS API
        # ...
        # Redirect user to OTP verification page
        # return redirect(url_for('verify_otp'))

        encrypted_otp = cipher_suite.encrypt(otp_code)
        return redirect(url_for('verify_otp', otp=encrypted_otp))
    
    return render_template('createstore.html')

print(OTP,"otp is this")


@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    # digotp=generate_random_string(5)
    
    encrypted_otp = request.args.get('otp')
    otp = cipher_suite.decrypt(encrypted_otp)
    print("=-----------------------")


    print(str(otp))
    print("=-----------------------")


    if request.method == 'POST':
        # Retrieve OTP from form data
        otpen = request.form['otp']
        otpen = f"b'{otpen}'"
        print("this is new otp" , otpen)

        

       
        # Compare OTP with the one generated earlier
        if str(otp) == str(otpen): # Replace with actual OTP validation code
            # User is authenticated, log them in
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            # Invalid OTP, show error message
            return '''
                <p>Invalid OTP, please try again.</p>
                <form method="post">
                    <label for="otp">Enter your OTP:</label>
                    <input type="text" id="otp" name="otp">
                    <button type="submit">Verify OTP</button>
                </form>
            '''
    # Display OTP verification form
    return '''
        <form method="post">
            <label for="otp">Enter your OTP:</label>
            <input type="text" id="otp" name="otp">
            <button type="submit">Verify OTP</button>
        </form>
    '''

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


@app.route('/')
def home():
    if g.user:
        
        return render_template('home.html',user=session['user'])
    return redirect(url_for('login'))

# @app.route('/')
# def createacc():

#     return render_template('login.html')


@app.route('/create_account',methods=['post','get'])
def render_cracc():
   return  render_template("createacc.html")

@app.route('/create',methods=['post','get'])
def create_user():
    import mysql.connector
    import json
    import random
    import os
    conn=mysql.connector.connect(user='root',password="8307802643",host="localhost",database="akm")
    # conn = mysql.connector.connect(user='ubambexgk0tnotbo',password='yejwFic8aUDHFELoaxfz',host='bdkcuyuzujne58f5ngj4-mysql.services.clever-cloud.com',database='bdkcuyuzujne58f5ngj4')
    cursor=conn.cursor()
    import datetime

   
       
    name=request.form["name"]
    phone=request.form["phone"]
    email=request.form["email"]
    category=request.form["category"]
    file = request.files['image']
   

    try:
        ch1=request.form['ch1']
        ch2=request.form['ch2']

    except:
       ch1=False
    
    img="url_for('static', filename='img/user/user-face.png')"
    verified="no"
    merch="no"
   


   

   
    def generate_random_string(length):
     digits = "0123456789"
     return ''.join(random.choice(digits) for i in range(length))
 
    random_string = generate_random_string(7)
    uid=random_string
    # print(name,phone,email,category,img,uid,verified,merch)
    # print(ch2)
    # print(ch1)
    # print(category)
   
    def check():
       pbl=0
      
       tg=[]
       if len(name)<2:
          tg.append("name")
          pbl +=1
       if len(phone)<10:
          tg.append("phone")
          pbl +=1
       if len(email)<11:
          tg.append("email")
          pbl +=1
       if   not ch1:
          tg.append("agr")
          pbl +=1

       if category=='0':
          tg.append("categ")
          pbl +=1

       if file.filename == '':
          tg.append("imwarn")
          pbl +=1


       userdir = os.path.join(app.static_folder, 'img','user', phone)
       if os.path.exists(userdir):
          tg.append("uswarn")
          pbl +=1
       
    
       
       
    

       
       
    
    # Save the file to a folder on the server
       


      

      
      
       data=""
       cmd=""

       for i in tg:
            print(i)
         
        #  tag=f'{i}'+"{}"

            cmd+=f'#{i}'
            cmd += """{color:red}"""

       data +=cmd
         

    #      cmd +=f''' #
    #    "color:red; " '''
       

      
       
       
       
       
       
       return data , pbl
    
         
         
   
    cmnd ,err=check()
    print(cmnd)
    print(err)
    cmnd1=f"""<style> {cmnd} </style> """
    print(cmnd1)


    

      
    
    # Save the file to the user's subdirectory on the server
   
       
   
    if err==0:
      userdir = os.path.join(app.static_folder, 'img','user', phone)

      os.makedirs(userdir, exist_ok=True)
      filepath = os.path.join(userdir, file.filename)
    
      print(filepath)
      file.save(filepath)
      return render_template("home.html")
    else:
        return render_template("createacc.html",cmd=cmnd1,error='invalid person')
    



   
         


        
    


 


    # sql=f'insert into LOGIN values("{name}","{phone}","{email}","{category}","{ch2}","{verified}","{merch}","{uid}","{img}")'
    # try:
    #  cursor.execute(sql)
    #  conn.close()
    # except mysql.connector.Error as error:
    #    print("Error: {}".format(error))
    #    return(format(error))
    
    # rows=cursor.fetchall()
    ######ERROR MANAGEMENT









if __name__ == '__main__':
   

   
    app.run(debug=True)