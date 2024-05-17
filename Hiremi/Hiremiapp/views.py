from django.shortcuts import render,redirect
from django .http import JsonResponse
from django.contrib.auth import  login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests

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
    data = requests.get('http://13.127.81.177:8000/api/registers/').json()
    user_count = len(data)
    print(data)

    data1 = requests.get('http://13.127.81.177:8000/transactions/').json()
    payment_count = len(data1)
    print(data1)

    # verified_users_endpoint = 'http://13.127.81.177:8000/api/registers/?verified=true'
    verified_users_endpoint = 'http://13.127.81.177:8000/api/registers/?verified=true'
    
    try:
        verified_users_response = requests.get(verified_users_endpoint)
        verified_users_response.raise_for_status()  # Raises an HTTPError if the response was an HTTP error
        verified_users = verified_users_response.json()
        verified_count = len(verified_users)
    except requests.RequestException as e:
        # Handle the case where the request to the API fails
        print(f"Error fetching verified users: {e}")
        verified_count = None



    unverified_users_endpoint = 'http://13.127.81.177:8000/api/registers/?verified=false'
    
    try:
        unverified_users_response = requests.get(unverified_users_endpoint)
        unverified_users_response.raise_for_status()  # Raises an HTTPError if the response was an HTTP error
        unverified_users = unverified_users_response.json()
        unverified_count = len(unverified_users)
    except requests.RequestException as e:
        # Handle the case where the request to the API fails
        print(f"Error fetching unverified users: {e}")
        unverified_count = None    
        

    context = {
        'user_count': user_count,
        'payment_count': payment_count,
        'verified_count': verified_count,
        'unverified_count': unverified_count,
    }
    return render(request, 'dashboard.html', context)


def dashboard1(request):
    data=requests.get('http://13.127.81.177:8000/api/registers/').json()
    return render(request,'dashboard1.html',{'data':data})


def view_Info(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
    return render(request,'profile-1.html',{'data':data})


# -------------------------------------------------------------------------------------------------------

def dashboard3(request):
    data=requests.get('http://13.127.81.177:8000/api/registers/').json()

    data1 = requests.get('http://13.127.81.177:8000/transactions/').json()
    context = {
        'user_count': data,
        'transctions': data1
    }
   
    return render(request,'dashboard3.html',context)


def view_Info1(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
    return render(request,'profile-2.html',{'data':data})




def accept(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/registers/{pk}/'

    update_data = {
        'verified': True,
    }
    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return JsonResponse({'message': 'User verification status updated successfully'})
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    

def reject(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/registers/{pk}/'

    update_data = {
        'verified': False, 
    }
    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return JsonResponse({'message': 'User verification status updated successfully'})
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)




def count_verified_accounts(request):
    # Endpoint to get all verified users
    verified_users_endpoint = 'http://13.127.81.177:8000/api/registers/?verified=true'
    response = requests.get(verified_users_endpoint)
    
    if response.status_code == 200:
        verified_users = response.json()
        verified_count = len(verified_users)
        return render(request, 'dashboard.html', {'verified_count': verified_count})
    else:
        return JsonResponse({'error': 'Failed to retrieve verified users count'}, status=response.status_code)





# --------------------------------------internship section--------------------------------------------


def internship(request):
    data=requests.get('http://13.127.81.177:8000/api/internship/').json()
    intern_count=len(data)
    print(data)
    return render(request,'internship.html',{'intern_count':intern_count})

def intern_applied(request):
    data=requests.get('http://13.127.81.177:8000/api/registers/').json()
    return render(request,'Intern-Applied.html',{'data':data})

def intern_info(request,pk):
    print(pk)
    data=requests.get(f'http://13.127.81.177:8000/api/registers/{pk}/').json()
    return render(request,'Intern-Pf-1.html',{'data':data})



def select(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/registers/{pk}/'

    update_data = {
        'candidate_status':select
    }
    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return JsonResponse({'message': 'User candidate status updated successfully'})
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)
    

def reject(request, pk):
    update_endpoint = f'http://13.127.81.177:8000/api/registers/{pk}/'

    update_data = {
        'candidate_status':reject 
    }
    response = requests.patch(update_endpoint, json=update_data)
    if response.status_code == 200:
        return JsonResponse({'message': 'User verification status updated successfully'})
    else:
        return JsonResponse({'error': 'Failed to update user verification status'}, status=response.status_code)

# ----------------------------------------------------------------------------------------------------

# ---------------------------------Mantoreship section-------------------------------------------------




# def dashboard3(request):
#      # Fetch data from the APIs
#     users = requests.get('http://13.127.81.177:8000/api/registers/').json()
#     transactions = requests.get('http://13.127.81.177:8000/transactions/').json()

#     # Create a combined data structure
#     combined_data = []
#     for transaction in transactions:
#         # Find the corresponding user for each transaction
#         user = next((user for user in users if user['id'] == transaction['user_id']), None)
#         if user:
#             combined_data.append({
#                 'transaction_id': transaction['id'],
#                 'amount': transaction['amount'],
#                 'date': transaction['date'],
#                 'username': user['username'],
#                 'email': user['email']
#             })

#     # Pass the combined data to the template
#     context = {
#         'combined_data': combined_data
#     }
#     return render(request, 'dashboard3.html', context)

