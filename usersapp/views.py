from django.shortcuts import render , redirect
from usersapp.models import *
from adminsapp.models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import urllib.request
import urllib.parse
import random
import pandas as pd

import time
import pytz
from datetime import datetime
import pickle
from sklearn.metrics import accuracy_score,classification_report



def user_index(request):
    return render(request,'user/index.html')

def user_about(request):
    return render(request,'user/about.html')

def user_contact(request):
    return render(request,'user/contact.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password,'jjjjjjjjjjjjjjjjjj')
        try : 
            user_data = UserModels.objects.get(email = email)
            print(user_data)
             
            if user_data.password ==  password:
                if user_data.user_status == 'accepted':
                    if user_data.Otp_Status == 'verified':
                       messages.success(request,'login successfull')
                       request.session['user_id'] = user_data.user_id
                       print('login sucessfull')
                       return redirect('user_dashboard')
                    else:
                        return redirect('otp')
                elif user_data.password == password and user_data.user_status == 'rejected':
                    messages.warning(request,"your account is rejected")
                else:
                    messages.info(request,"your account is in pending")
            else:
                messages.error(request, 'Error in Email or Password')
        except:
            print('exce[t]')
            return redirect('user_login')
    return render(request,'user/login.html')

def admin_login(request):
    admin_name = 'admin@gmail.com'
    admin_pwd = 'admin'
    if request.method == 'POST':
        a_name = request.POST.get('email')
        a_pwd = request.POST.get('password')
        print(a_name, a_pwd, 'admin entered details')

        if admin_name == a_name and admin_pwd == a_pwd:
            messages.success(request, 'login successful')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Wrong Email Or Password')
            return redirect('admin_login')   
    return render(request,'user/alogin.html')

def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    # Disable SSL certificate verification
    # context = ssl._create_unverified_context()
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data)
    return f.read()


def user_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('user')
        email = request.POST.get('email')
        contact = request.POST.get ('contact')
        password = request.POST.get('password')
        file = request.FILES['file']
        # file = request.FILES['file']
        print (request)
        print(name,username,email,contact,password,'data')
        otp = str(random.randint(1000, 9999)) 
        print(otp)
        try:
           print('try')
           UserModels.objects.get(email=email,) 
           messages.info(request, 'Mail already Registered')
           return redirect('user_registration') 
        except:
            print('except')
            # mail message
            mail_message = f'Registration Successfully\n Your 4 digit Pin is below\n {otp}'
            print(mail_message)
            send_mail("Student Password", mail_message, settings.EMAIL_HOST_USER,[email])
            # text nessage
            sendSMS(name, otp, contact)
            UserModels.objects.create( otp=otp,email=email ,password=password,name=name,contact=contact, file=file )        
            request.session['email'] = email
            messages.success(request, 'Register SUccessfull...!')
            return redirect('user_otp')
    return render(request,'user/registration.html')


def user_otp (request):
    user_id = request.session['email']
    user_o =UserModels.objects.get(email = user_id)
    print(user_o,'user available')
    print(type(user_o.otp))
    print(user_o. otp,'created otp')
    # print(user_o. otp, 'creaetd otp')
    if request.method == 'POST':
        u_otp = request.POST.get('otp')
        u_otp = int(u_otp)
        print(u_otp, 'enter otp')
        if u_otp == user_o.otp:
            print('if')
            user_o.Otp_Status  = 'verified'
            user_o.save()
            messages.success(request, 'OTP  verified successfully')
            return redirect('user_login')
        else:
            print('else')
            messages.error(request, 'Error in OTP')
            return redirect('user_otp')
    return render(request,'user/otp.html')


def user_dashboard(request):
    return render(request,'user/dashboard.html')
    # prediction_count =  UserModels.objects.all().count()
    # print(prediction_count)
    # user_id = request.session["User_id"]
    # user =  UserModels.objects.get(User_id = user_id)
    
    # if user.Last_Login_Time is None:
    #     IST = pytz.timezone('Asia/Kolkata')
    #     current_time_ist = datetime.now(IST).time()
    #     user.Last_Login_Time = current_time_ist
    #     user.save()
    # return render(request,'user/dashboard.html', {'predictions' : prediction_count, 'la':user})
    
# def user_logout(request):
#     user_id = request.session["User_id"]
#     user = UserModels.objects.get(User_id = user_id) 
#     t = time.localtime()
#     user.Last_Login_Time = t
#     current_time = time.strftime('%H:%M:%S', t)
#     user.Last_Login_Time = current_time
#     current_date = time.strftime('%Y-%m-%d')
#     user.Last_Login_Date = current_date
#     user.save()
#     messages.info(req, 'You are logged out..')
#     # print(user.Last_Login_Time)
#     # print(user.Last_Login_Date)
#     return redirect('user_login')

from sklearn.ensemble import RandomForestClassifier
def user_detect(req):
# predictdiabetes form Function

    if req.method == 'POST':
        gender = req.POST.get('gender')
        age = req.POST.get('age')
        hypertension = req.POST.get('hypertension')
        heart = req.POST.get('heart')
        married = req.POST.get('married')
        work = req.POST.get('work')
        residence = req.POST.get('residence')
        bmi = req.POST.get('bmi')
        glucose = req.POST.get('glucose')
        smoking = req.POST.get('smoking')
        # cholestrol=req.POST.get('cholestrol')
        # bp_h=req.POST.get('bp_h')
        # bp_l=req.POST.get('bp_l')
        # alcohol=req.POST.get('alcohol')
        if gender == 1:
            genders= "male"
        else:
            genders = "female"
        context = {'gender': genders}
        
        bmi = float( bmi)
    
       
        import pickle
        file_path = 'rfc_strok.pkl'  # Path to the saved model file

        with open(file_path, 'rb') as file:
            loaded_model = pickle.load(file)
            res =loaded_model.predict([[gender,age,hypertension,heart,married,work,residence,glucose,bmi,smoking]])
            # res=loaded_model.predict([[25,1,50.125,12.0255,0.15,99.255,45.325]])

            dataset = Upload_dataset_model.objects.last()
            # print(dataset.Dataset)
            df=pd.read_csv(dataset.Dataset.path)

    

            X = df.drop('stroke', axis = 1)
            y = df['stroke']
            from sklearn.model_selection import train_test_split
            X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
        
            from sklearn.tree import DecisionTreeClassifier
            decision = DecisionTreeClassifier()
            decision.fit(X_train, y_train)

            # prediction
            train_prediction= decision.predict(X_train)
            test_prediction= decision.predict(X_test)
                    # prediction
            train_prediction= decision.predict(X_train)
            test_prediction= decision.predict(X_test)
            print('*'*20)

            # evaluation
            from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
            accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
            precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
            recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
            f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
            conf_matrix = confusion_matrix(y_test, test_prediction)
            specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
            sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
            x=0
            if res == 0:
                x = 0
                messages.info(req,"Stroke Is Not Detected")
            else:
                x=1
                messages.info(req,"Stroke Is Detected")
            print(x)
            context = {'accc': accuracy,'pre': precession,'f1':f1,'call':recall,'res':x,'spe':specificity,'sen':sensitivity}
            print(type(res), 'ttttttttttttttttttttttttt')
            print(res)
            
            return render(req, 'user/detect_details.html',context)
    return render(req,'user/detect.html')

def user_detect_details(request):
    return render(request,'user/detect_details.html')

def user_myprofile(request):
    user_id = request.session['user_id']
    example = UserModels.objects.get(user_id = user_id)
    print(example,'user_id')
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        messages.success(request,'updated successful')

        example.name =name
        example.contact =contact
        example.email =email
        example.password =password
        
        if len(request.FILES)!=0:
            file = request.FILES['file']
            example.file = file
            example.name = name
            example.contact = contact
            example.email = email
            example.password = password
            example.save()
        else:
            example.name = name
            example.email = email
            example.password = password
            example.contact = contact
        #    example.file=file
            example.save()     
    return render(request,'user/myprofile.html',{'i':example})



# Create your views here.
