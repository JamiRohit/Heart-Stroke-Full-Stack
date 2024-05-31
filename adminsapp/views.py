from django.shortcuts import render , redirect
from adminsapp.models import *
from usersapp.models import *
from django.core.paginator import Paginator
from django.contrib import messages
import pandas as pd


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble  import GradientBoostingClassifier
from sklearn.svm  import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble  import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score,f1_score, recall_score, precision_score, auc, roc_auc_score, roc_curve,confusion_matrix

from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import cross_val_score

from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB,MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
# import os

# Create your views here.
def admin_dashboard(request):
    # return render(request,'admin/dashboard.html')
    all_users_count =  UserModels.objects.all().count()
    pending_users_count = UserModels.objects.filter(user_status = 'pending').count()
    rejected_users_count = UserModels.objects.filter(user_status = 'removed').count()
    accepted_users_count = UserModels.objects.filter(user_status = 'accepted').count()
    return render(request,'admin/dashboard.html',{'a' : all_users_count, 'b' : pending_users_count, 'c' : rejected_users_count, 'd' : accepted_users_count})

def admin_pendinguser(request):
    users = UserModels.objects.filter(user_status = 'pending')
    return render(request,'admin/pending.html', {'users':users})    

def admin_manageuser(request):
    a = UserModels.objects.all()
    paginator = Paginator(a, 5) 
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/manage_user.html',{'all':post})    

# Create your views here.


def admin_reject_btn(req,x):
    user = UserModels.objects.get(user_id = x)
    user.user_status = 'rejected'
    user.save()
    messages.warning(req,'Rejected')
    return redirect('admin_pendinguser')
    
    
def admin_accept_btn(req,x):
    user = UserModels.objects.get(user_id = x)
    user.user_status = 'accepted'
    user.save()
    messages.success(req,'accepted')
    return redirect('admin_pendinguser')    

def Change_Status(req, id):
    # user_id = req.session['User_Id']
    user = UserModels.objects.get(user_id = id)
    if user.user_status == 'accepted':
        user.user_status = 'rejected'   
        user.save()
        messages.success(req,'Status Changed Succesfully')
        return redirect('admin_manageuser')
    else:
        user.user_status = 'accepted'
        user.save()
        messages.success(req,'Status Changed Successfully')
        return redirect('admin_manageuser')
    
def Delete_User(req, id):
    UserModels.objects.get(user_id = id).delete()
    messages.info(req,'Deleted')
    return redirect('admin_manageuser')



# def admin_data(req):
#     if req.method == 'POST':
#         file = req.FILES['file']
#         # print(file)
#         file_size = str((file.size)/1024) +' kb'
#         # print(file_size)
#         Upload_dataset_model.objects.create(File_size = file_size, Dataset = file)
#         messages.success(req, 'Your dataset was uploaded..')
#     return render(req, 'admin/upload_data.html')


def admin_data(request):
    return render(request, 'admin/upload_data.html')

def admin_dataset_btn(request): 
    messages.success(request, 'Dataset uploaded successfully')
    return redirect('admin_data')

# Admin view dataset
def admin_viewdata(req):
    dataset = Upload_dataset_model.objects.all()
    paginator = Paginator(dataset, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'admin/view.html', {'data' : dataset, 'user' : post})

def delete_dataset(req, id):
    dataset = Upload_dataset_model.objects.get(User_id = id).delete()
    messages.warning(req, 'Dataset was deleted..!')
    return redirect('admin_viewdata')


def admin_viewdetails(request):
    # df=pd.read_csv('heart.csv')
    data = Upload_dataset_model.objects.last()
    print(data,type(data),'sssss')
    file = str(data.Dataset)
    df = pd.read_csv(f'./media/{file}')
    table = df.to_html(table_id='data_table')
    return render(request,'admin/view_details.html', {'t':table}) 


def admin_reject_btn(req,x):
    user = UserModels.objects.get(user_id = x)
    user.user_status = 'rejected'
    user.save()
    messages.warning(req,'Rejected')
    return redirect('admin_pendinguser')
    
    
def admin_accept_btn(req,x):
    user = UserModels.objects.get(user_id = x)
    user.user_status = 'accepted'
    user.save()
    messages.success(req,'accepted')
    return redirect('admin_pendinguser')    

def Change_Status(req, id):
    # user_id = req.session['User_Id']
    user = UserModels.objects.get(user_id = id)
    if user.user_status == 'accepted':
        user.user_status = 'rejected'   
        user.save()
        messages.success(req,'Status Changed Succesfully')
        return redirect('admin_manageuser')
    else:
        user.user_status = 'accepted'
        user.save()
        messages.success(req,'Status Changed Successfully')
        return redirect('admin_manageuser')
    
def Delete_User(req, id):
    UserModels.objects.get(user_id = id).delete()
    messages.info(req,'Deleted')
    return redirect('admin_manageuser')



def admin_data(req):
    if req.method == 'POST':
        file = req.FILES['file']
        # print(file)
        file_size = str((file.size)/1024) +' kb'
        # print(file_size)
        Upload_dataset_model.objects.create(File_size = file_size, Dataset = file)
        messages.success(req, 'Your dataset was uploaded..')
    return render(req, 'admin/upload_data.html')


# def admin_data(request):
#     return render(request, 'admin/upload_data.html')

def admin_dataset_btn(request): 
    messages.success(request, 'Dataset uploaded successfully')
    return redirect('admin_data')

# Admin view dataset
def admin_viewdata(req):
    dataset = Upload_dataset_model.objects.all()
    paginator = Paginator(dataset, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'admin/view.html', {'data' : dataset, 'user' : post})

def delete_dataset(req, id):
    dataset = Upload_dataset_model.objects.get(User_id = id).delete()
    messages.warning(req, 'Dataset was deleted..!')
    return redirect('admin_viewdata')


def admin_viewdetails(request):
    # df=pd.read_csv('heart.csv')
    data = Upload_dataset_model.objects.last()
    print(data,type(data),'sssss')
    file = str(data.Dataset)
    df = pd.read_csv(f'./media/{file}')
    table = df.to_html(table_id='data_table')
    return render(request,'admin/view_details.html', {'t':table}) 



def algorithm_logistic(request):
    return render(request,'admin/logistic.html')
def logistic_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from sklearn.linear_model import LogisticRegression
    Logistics = LogisticRegression()
    Logistics.fit(X_train, y_train)

    # prediction
    train_prediction= Logistics.predict(X_train)
    test_prediction= Logistics.predict(X_test)
    print('*'*20)

    # evaluation
    # from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,Specificity,Sensitivity
    # accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    # precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    # recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    # f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    # Confusion_matrix = confusion_matrix(y_test, test_prediction)
    # Specificity = round(Confusion_matrix[0, 0] / (Confusion_matrix[0, 0] + Confusion_matrix[0, 1]) * 100, 2)
    # Sensitivity = round(Confusion_matrix[1, 1] / (Confusion_matrix[1, 0] + Confusion_matrix[1, 1]) * 100, 2)
    # # Accuracy_train(accuracy_score(prediction_train,y_train))
    # name = "Logistic Regression Algorithm"
    # Logistic.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name,Specificity=Specificity,Sensitivity=Sensitivity)
    # data = Logistic.objects.last()
    # messages.success(req, 'Algorithm executed Successfully')
    # return render(req, 'admin/logistic.html',{'i': data})
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
    from django.contrib import messages

# Your existing code here
    accuracy = round(accuracy_score(y_test, test_prediction) * 100, 2)
    precession = round(precision_score(y_test, test_prediction, average='macro') * 100, 2)
    recall = round(recall_score(y_test, test_prediction, average='macro') * 100, 2)
    f1 = round(f1_score(y_test, test_prediction, average='macro') * 100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    name = "Logistic Regression Algorithm"
    Logistic.objects.create(Accuracy=accuracy, Precession=precession, F1_Score=f1, Recall=recall, Name=name,
                            Specificity=specificity, Sensitivity=sensitivity)
    data = Logistic.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/logistic.html',{'i': data})




def algorithm_svm(request):
    return render(request,'admin/svm.html')
def svm_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from sklearn.svm import SVC
    svm = SVC()
    svm.fit(X_train, y_train)

    # prediction
    train_prediction= svm.predict(X_train)
    test_prediction= svm.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    name = "svm Algorithm"
    SVM_ALGO.objects.create(Accuracy=accuracy, Precession=precession, F1_Score=f1, Recall=recall, Name=name,
                            Specificity=specificity, Sensitivity=sensitivity)
    # Accuracy_train(accuracy_score(prediction_train,y_train))
    
    
    data = SVM_ALGO.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/svm.html',{'i': data})




def algorithm_decision(request):
    return render(request,'admin/decision.html')
def decision_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from sklearn.tree import DecisionTreeClassifier
    decision = DecisionTreeClassifier()
    decision.fit(X_train, y_train)

    # prediction
    train_prediction= decision.predict(X_train)
    test_prediction= decision.predict(X_test)
    print('*'*28)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    # Accuracy_train(accuracy_score(prediction_train,y_train))
    name = "Decision Tree Algorithm"
    DT_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name,Specificity=specificity, Sensitivity=sensitivity)
    data = DT_ALGO.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/decision.html',{'i': data})


def algorithm_random(request):
    return render(request,'admin/random.html')
def random_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from sklearn.ensemble import RandomForestClassifier
    random = RandomForestClassifier()
    random.fit(X_train, y_train)

    # prediction
    train_prediction= random.predict(X_train)
    test_prediction= random.predict(X_test)
    print('*'*28)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    # Accuracy_train(accuracy_score(prediction_train,y_train))
    name = "Random Forest Algorithm"
    RandomForest.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name, Specificity=specificity, Sensitivity=sensitivity)
    data = RandomForest.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/random.html',{'i': data})

def algorithm_knn(request):
    return render(request,'admin/knn.html')
# KNN_btn
def KNN_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_train=scaler.fit_transform(X_train)
    X_test= scaler.transform(X_test)
    from sklearn.neighbors import KNeighborsClassifier
    KNN = KNeighborsClassifier()
    KNN.fit(X_train, y_train)

    # prediction
    train_prediction= KNN.predict(X_train)
    test_prediction= KNN.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    # Accuracy_train(accuracy_score(prediction_train,y_train))

    name = "KNN Algorithm"
    KNN_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name,Specificity=specificity, Sensitivity=sensitivity)
    data = KNN_ALGO.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/knn.html',{'i': data})




def algorithm_gradient(request):
    return render(request,'admin/gradient.html')
def gradient_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from sklearn.ensemble import GradientBoostingClassifier
    gradient = GradientBoostingClassifier()
    gradient.fit(X_train, y_train)

    # prediction
    train_prediction= gradient.predict(X_train)
    test_prediction= gradient.predict(X_test)
    print('*'*28)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    # Accuracy_train(accuracy_score(prediction_train,y_train))
    name = "Gradient Boost Algorithm"
    ANN_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name,Specificity=specificity, Sensitivity=sensitivity)
    data = ANN_ALGO.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/gradient.html',{'i': data})



def algorithm_ada(request):
    return render(request,'admin/ada.html')
def ada_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from sklearn.ensemble import AdaBoostClassifier
    ada = AdaBoostClassifier()
    ada.fit(X_train, y_train)

    # prediction
    train_prediction= ada.predict(X_train)
    test_prediction= ada.predict(X_test)
    print('*'*28)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    # Accuracy_train(accuracy_score(prediction_train,y_train))
    name = "ADA Boost Algorithm"
    ADA_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name,Specificity=specificity, Sensitivity=sensitivity)
    data = ADA_ALGO.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/ada.html',{'i': data})



def algorithm_xg(request):
    return render(request,'admin/xg.html')
def xg_btn(req):
    dataset = Upload_dataset_model.objects.last()
    # print(dataset.Dataset)
    df=pd.read_csv(dataset.Dataset.path)
    X = df.drop('stroke', axis = 1)
    y = df['stroke']
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1,test_size=0.2)
    # from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(X_train)
    # X_test= scaler.transform(X_test)
    from xgboost import XGBClassifier
    xg = XGBClassifier()
    xg.fit(X_train, y_train)

    # prediction
    train_prediction= xg.predict(X_train)
    test_prediction= xg.predict(X_test)
    print('*'*28)

    # evaluation
    from sklearn.metrics import accuracy_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(y_test,test_prediction,average = 'macro')*100, 2)
    recall = round(recall_score(y_test,test_prediction,average = 'macro')*100, 2)
    f1 = round(f1_score(y_test,test_prediction,average = 'macro')*100, 2)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    specificity = round(conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1]) * 100, 2)
    sensitivity = round(conf_matrix[1, 1] / (conf_matrix[1, 0] + conf_matrix[1, 1]) * 100, 2)
    # Accuracy_train(accuracy_score(prediction_train,y_train))
    name = "XG Boost Algorithm"
    XG_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1,Recall=recall,Name=name,Specificity=specificity, Sensitivity=sensitivity)
    data = XG_ALGO.objects.last()
    messages.success(req, 'Algorithm executed Successfully')
    return render(req, 'admin/xg.html',{'i': data})

def admin_graph(request):
    details = XG_ALGO.objects.last()
    a = details.Accuracy
    deatails1 = ADA_ALGO.objects.last()
    b = deatails1.Accuracy
    details2 = KNN_ALGO.objects.last()
    c = details2.Accuracy
    deatails3 = SVM_ALGO.objects.last()
    d = deatails3.Accuracy
    details4 = DT_ALGO.objects.last()
    e = details4.Accuracy
    details5 = ANN_ALGO.objects.last()
    f = details5.Accuracy
    details6 = Logistic.objects.last()
    g = details6.Accuracy
    details7 = RandomForest.objects.last()
    h = details7.Accuracy
    return render(request, 'admin/graph.html', {'xg':a,'ada':b,'knn':c,'sxm':d,'dt':e,'ann':f,'log':g, 'ran':h})

