from django.shortcuts import render,redirect
from django .http import JsonResponse
from django.contrib.auth import  login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from datetime import datetime

# Create your views here.

# -------------------- superuser login ------------------------------------------------------
def login(request):
    return render(request, 'index.html')

def superuser_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            # login(request, user)
            return redirect('dashboard')  # Redirect to your desired URL
        else:
            messages.error(request, 'Invalid username or password for superuser.')
    return render(request, 'superuser_login.html')

@login_required
def superuser_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('superuser_login')

# --------------------------------------------------------------------------------------------

def dashboard(request):
    states_list = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
        'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
        'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
        'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Jammu and Kashmir'
    ]
    state_counts = {state: {'total': 0, 'verified': 0, 'unverified': 0} for state in states_list}

    # Fetch data from the registrations API
    registrations_url = 'http://13.127.81.177:8000/api/registers/'
    data = requests.get(registrations_url).json()
    user_count = len(data)

    # Fetch data from the transactions API
    transactions_url = 'http://13.127.81.177:8000/transactions/'
    response = requests.get(transactions_url)

    if response.status_code == 200:
        data1 = response.json()
        verified_data = [entry for entry in data1 if entry.get('is_paid') == True]
        payment_count = len(verified_data)

    # Update the state counts based on the registrations
    for registration in data:
        college_state = registration.get('college_state')
        if college_state in state_counts:
            state_counts[college_state]['total'] += 1
            if registration.get('verified'):
                state_counts[college_state]['verified'] += 1
            else:
                state_counts[college_state]['unverified'] += 1


# --------------count the total verified ----------------------
    url = 'http://13.127.81.177:8000/api/registers/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    verified_count = 0
    for registration in data:
        if registration.get('verified') == True:
            verified_count += 1
    print(f'Number of verified registrations: {verified_count}')

# -------------- count the total unverified----------------------
    url = 'http://13.127.81.177:8000/api/registers/'
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    unverified_count = 0
    for registration in data:
        if registration.get('verified') == False:
            unverified_count += 1
    print(f'Number of verified registrations: {verified_count}')

    context = {
        'user_count': user_count,
        'payment_count': payment_count,
        'unverified_count': unverified_count,
        'verified_count': verified_count,
        'state_counts': state_counts,
    }
    return render(request, 'dashboard.html', context)

# --------------------------- Dashboard1 ----------------------------------
def dashboard1(request):
    data=requests.get('http://13.127.81.177:8000/api/registers/').json()
    return render(request,'dashboard1.html',{'data':data})

def view_Info1(request,pk):
     print(pk)
     data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
     return render(request,'Profile-1.html',{'data':data})


# ------------------------------ Dashboard2 ----------------------------------
def dashboard2(request):
    url = 'http://13.127.81.177:8000/api/registers/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        verified_data = [entry for entry in data if entry.get('verified') == True]
        context = {'data': verified_data}    
    else:
        context = {'data': [], 'error': 'Failed to retrieve data from the API'}

    return render(request, 'dashboard2.html', context)

def view_Info2(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
    return render(request,'Profile-1.html',{'data':data})



# ------------------------------- Dashboard3 -----------------------------------
def dashboard3(request):
    data=requests.get('http://13.127.81.177:8000/api/registers/').json()
    
    url = 'http://13.127.81.177:8000/transactions/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data1 = response.json()
        verified_data = [entry for entry in data1 if entry.get('is_paid') == True]
        context = {
        'user_count': data,
        'transactions': verified_data
        }
    
    else:
        context = {'data': [], 'error': 'Failed to retrieve data from the API'}

    return render(request,'dashboard3.html',context)

def view_Info3(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
    return render(request,'profile-2.html',{'data':data})

# -------------------------------- Dashboard4 ---------------------------------------
def dashboard4(request):
    url = 'http://13.127.81.177:8000/api/registers/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        verified_data = [entry for entry in data if entry.get('verified') == False]
        context = {'data': verified_data}
        print(context)
        
    else:
        context = {'data': [], 'error': 'Failed to retrieve data from the API'}

    return render(request, 'dashboard4.html', context)

def view_Info4(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
    return render(request,'Profile-1.html',{'data':data})


# ----------------------------- Verification Button ---------------------------------
def accept(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/registers/{pk}/'

    update_data = {
        'verified': True,
    }
    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('view_Info1',pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    
def reject(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/registers/{pk}/'

    update_data = {
        'verified': False,    
    }
    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('view_Info1',pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)






# --------------------------------------internship section--------------------------------------------


def internship(request):
    data=requests.get('http://13.127.81.177:8000/api/internship-applications/').json()
    intern_count=len(data)
    print(data)


    
# --------------count the total verified ----------------------
    url = 'http://13.127.81.177:8000/api/internship-applications/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Select_count = 0
    for internship in data:
        if internship.get('candidate_status') == 'Accept':
            Select_count += 1
    print(f'Number of verified registrations: {Select_count}')

# -------------- count the total unverified----------------------
    url = 'http://13.127.81.177:8000/api/internship-applications/'
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Reject_count = 0
    for internship in data:
        if internship.get('candidate_status') == 'Reject':
            Reject_count += 1
    print(f'Number of verified registrations: {Reject_count}')

 # --------------Count the total Pending ----------------------
    url = 'http://13.127.81.177:8000/api/internship-applications/'
    print(Select_count,Reject_count,intern_count)
    Pending_count= intern_count - (Select_count + Reject_count)
    print(f'Number of Pending Candidate: {Pending_count}')
    
    context={
        'intern_count': intern_count,
        'Select_count': Select_count,
        'Reject_count': Reject_count,
        'Pending_count': Pending_count,
    }
    return render(request,'internship.html',context)


def intern_applied(request):
    internship_response = requests.get('http://13.127.81.177:8000/api/internship-applications/')
    internship_data = internship_response.json()
    internship_field = internship_data[1].get('Internship_profile')

    internship_response = requests.get('http://13.127.81.177:8000/api/internship-applications/')
    
    # Parse the JSON response
    internship_data = internship_response.json()
    
    # Extract the Internship_profile from each internship entry
    internship_profiles = [internship.get('Internship_profile') for internship in internship_data]

    
    registers_response = requests.get('http://13.127.81.177:8000/api/registers/')
    registers_data = registers_response.json()
    
    context = {
        'internship_profiles': internship_profiles,
        'registers_data': registers_data,
    }
    return render(request,'Intern-Applied.html',context)



def intern_info(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/internship-applications/{pk}/').json()
    return render(request,'Intern-Pf-1.html',{'data':data})



def Select_intern(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/internship-applications/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Accept',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('intern_info', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    

def Reject_intern(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/internship-applications/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Reject',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('intern_info', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
# ----------------------------------------------------------------------------------------------------



# ---------------------------------Mantoreship section-------------------------------------------------


def Mentoreship(request):
    data = requests.get('http://13.127.81.177:8000/api/mentorship/').json()
    mentor_count = len(data)

    # --------------Count the total Selected ----------------------
    url = 'http://13.127.81.177:8000/api/mentorship/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    select_count = 0
    for mentoreship in data:
        if mentoreship.get('candidate_status') == 'Select':
            select_count += 1
    print(f'Number of Selected Candidate: {select_count}')


     # --------------Count the total Rejected ----------------------
    url = 'http://13.127.81.177:8000/api/mentorship/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Reject_count = 0
    for mentoreship in data:
        if mentoreship.get('candidate_status') == 'Reject':
            Reject_count += 1
    print(f'Number of Rejected Candidate: {Reject_count}')
    
    context={
        'mentor_count':mentor_count,
        'select_count':select_count,
        'Reject_count':Reject_count,
    }

    return render(request,'Mentoreship.html',context)


def Mentor_dash1(request):
    data=requests.get('http://13.127.81.177:8000/api/mentorship/').json()
    return render(request,'Mentor-dash1.html',{'data':data})

def mentor_info1(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/api/mentorship/{pk}/').json()
    return render(request,'Mentor-pf-1.html',{'data':data})


def Select(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/mentorship/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Select',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('mentor_info1', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    

def Reject(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/mentorship/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Reject',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('mentor_info1', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)



def Mentor_dash2(request):
    url = 'http://13.127.81.177:8000/api/mentorship/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        verified_data = [entry for entry in data if entry.get('candidate_status') == 'Select']
        context = {'data': verified_data}    
    else:
        context = {'data': [], 'error': 'Failed to retrieve data from the API'}

    return render(request, 'Mentor-dash2.html', context)

def mentor_info2(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/api/mentorship/{pk}/').json()
    return render(request,'Mentor-pf-2.html',{'data':data})

# -----------------------------------------------------------------------------------------------------



# ------------------------------------- Corporate training Section ------------------------------------------------

def corporate_training(request):
    data=requests.get('http://13.127.81.177:8000/api/corporatetraining/').json()
    corporate_training_count=len(data)
    print(data)

    # --------------Count the total Selected ----------------------
    url = 'http://13.127.81.177:8000/api/corporatetraining/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    select_count = 0
    for corporate in data:
        if corporate.get('candidate_status') == 'Select':
            select_count += 1
    print(f'Number of Selected Candidate: {select_count}')


     # --------------Count the total Rejected ----------------------
    url = 'http://13.127.81.177:8000/api/corporatetraining/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Reject_count = 0
    for corporate in data:
        if corporate.get('candidate_status') == 'Reject':
            Reject_count += 1
    print(f'Number of Rejected Candidate: {Reject_count}')

     # -------------- Count the Not-Enroll ----------------------
    url = 'http://13.127.81.177:8000/api/corporatetraining/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Notenroll_count = 0
    for corporate in data:
        if corporate.get('payment_status') == 'Not Enroll':
            Notenroll_count += 1
    print(f'Number of Rejected Candidate: {Notenroll_count}')

    context={
        'corporate_training_count':corporate_training_count,
        'select_count':select_count,
        'Reject_count':Reject_count,
        'Notenroll_count':Notenroll_count,
    }
    return render(request,'corporate.html',context)


def corporate_dash1(request):
    data=requests.get('http://13.127.81.177:8000/api/corporatetraining/').json()
    return render(request,'corporate-dash1.html',{'data':data})

def corporate_info1(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/api/corporatetraining/{pk}/').json()
    return render(request,'corporate-pf-1.html',{'data':data})

def corporate_dash2(request):
    url = 'http://13.127.81.177:8000/api/corporatetraining/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        verified_data = [entry for entry in data if entry.get('verified') == True]
        context = {'data': verified_data}    
    else:
        context = {'data': [], 'error': 'Failed to retrieve data from the API'}
    return render(request,'corporate-dash1.html',context)

def corporate_info2(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/api/corporatetraining/{pk}/').json()
    return render(request,'corporate-pf-1.html',{'data':data})

def corporate_dash3(request):
    data=requests.get('http://13.127.81.177:8000/api/corporatetraining/').json()
    return render(request,'corporate-dash1.html',{'data':data})

def corporate_info3(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/api/corporatetraining/{pk}/').json()
    return render(request,'corporate-pf-1.html',{'data':data})

def corporate_dash4(request):
    data=requests.get('http://13.127.81.177:8000/api/corporatetraining/').json()
    return render(request,'corporate-dash1.html',{'data':data})

def corporate_info4(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/api/corporatetraining/{pk}/').json()
    return render(request,'corporate-pf-1.html',{'data':data})



def Corporate_Select(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/corporatetraining/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Select',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('corporate_info1', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    

def Corporate_Reject(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/corporatetraining/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Reject',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('corporate_info1', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)


# ----------------------------------------------------------------------------------------------------------



# -------------------------------------fresher section--------------------------------------------------

def fresher(request):
    data=requests.get('http://13.127.81.177:8000/job-applications/').json()
    fresher_count=len(data)
    print(data)

     # --------------Count the total Selected ----------------------
    url = 'http://13.127.81.177:8000/job-applications/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    select_count = 0
    for fresher in data:
        if fresher.get('candidate_status') == 'Select':
            select_count += 1
    print(f'Number of Selected Candidate: {select_count}')


     # --------------Count the total Rejected ----------------------
    url = 'http://13.127.81.177:8000/job-applications/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Reject_count = 0
    for fresher in data:
        if fresher.get('candidate_status') == 'Reject':
            Reject_count += 1
    print(f'Number of Rejected Candidate: {Reject_count}')

     # -------------- Count the Not-Enroll ----------------------
    url = 'http://13.127.81.177:8000/job-applications/'

    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    Notenroll_count = 0
    for fresher in data:
        if fresher.get('payment_status') == 'Not Enroll':
            Notenroll_count += 1
    print(f'Number of Rejected Candidate: {Notenroll_count}')
    context={
        'fresher_count':fresher_count,
    }
    return render(request,'fresher.html',context)


def fresher_dash1(request):
    data=requests.get('http://13.127.81.177:8000/job-applications/').json()
    return render(request,'fresher-dash1.html',{'data':data})

def fresher_info1(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/job-applications/{pk}/').json()
    return render(request,'fresher-pf-1.html',{'data':data})

def fresher_dash2(request):
    data=requests.get('http://13.127.81.177:8000/job-applications/').json()
    return render(request,'fresher-dash1.html',{'data':data})

def fresher_info2(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/job-applications/{pk}/').json()
    return render(request,'fresher-pf-1.html',{'data':data})

def fresher_dash3(request):
    data=requests.get('http://13.127.81.177:8000/job-applications/').json()
    return render(request,'fresher-dash1.html',{'data':data})

def fresher_info3(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/job-applications/{pk}/').json()
    return render(request,'fresher-pf-1.html',{'data':data})

def fresher_dash4(request):
    data=requests.get('http://13.127.81.177:8000/job-applications/').json()
    return render(request,'fresher-dash1.html',{'data':data})

def fresher_info4(request,pk):
    data=requests.get(f'http://13.127.81.177:8000/job-applications/{pk}/').json()
    return render(request,'fresher-pf-1.html',{'data':data})



def fresher_Select(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/job-applications/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Select',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('fresher_info1', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    

def fresher_Reject(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/job-applications/{pk}/'

    # Update candidate_status with a serializable value
    update_data = {
        'candidate_status': 'Reject',  # Example status value
    }

    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return redirect('fresher_info1', pk)
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)

# -----------------------------------------------------------------------------------------------------