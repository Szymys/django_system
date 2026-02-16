from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.auth.models import User



# DO LOGOWANIA
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# WERYFIKACJA MAILA
from django.contrib.sites.shortcuts import get_current_site
from . token import user_tokenizer_generate
from django.template.loader import render_to_string

from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# WIADOMOSCI DJANGO
from django.contrib import messages
# ********************************************************************************************


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
                user = form.save()

                user.is_active = False
                                
                user.save()

                # WYSYLANIE MAILA Z LINKIEM DO WERYFIKACJI      
                        
                current_site = get_current_site(request)

                subject = 'Weryfikacja konta'

                message = render_to_string('account/registration/email-verification.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': user_tokenizer_generate.make_token(user),
                })

                user.email_user(subject=subject, message=message)

                return redirect('email-verification-sent')
        
        
    context = {'form':form}





    return render(request, 'account/registration/register.html', context=context)




def email_verification(request, uidb64, token):

        # UnikALNY ID UZYTKOWNIKA
        unique_id = force_str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=unique_id)

        # SUKCES WERYFIKACJI
        if user and user_tokenizer_generate.check_token(user, token):

                user.is_active = True

                user.save()

                return redirect('email-verification-success')
        # BŁĄD WERYFIKACJI
        else:

                return redirect('email-verification-failed')



def email_verification_sent(request):

        return render(request, 'account/registration/email-verification-sent.html') 



def email_verification_success(request):

        return render(request, 'account/registration/email-verification-success.html')



def email_verification_failed(request):

        return render(request, 'account/registration/email-verification-failed.html')








# LOGOWANIE
def my_login(request):
      
        form = LoginForm()

        if request.method == 'POST':
            
                form = LoginForm(request, data=request.POST)

                if form.is_valid():

                        username = request.POST.get('username')
                        password = request.POST.get('password')

                        user = authenticate(request, username=username, password=password)

                        if user is not None:
                        
                                auth.login(request, user)

                                messages.success(request, 'Login success!')

                                return redirect("dashboard")
                        
        context = {'form':form}

        return render(request, 'account/my-login.html', context=context)




# PANEL
@login_required(login_url='my-login')
def dashboard(request):
       
       return render(request, 'account/dashboard.html')



# WYLOGOWANIE
def user_logout(request):

        auth.logout(request)

        messages.success(request, 'Logout success!')

        return redirect("store")



# USUWANIE KONTA
@login_required(login_url='my-login')
def delete_account(request):


        user = User.objects.get(id=request.user.id)

        if request.method == 'POST':
               
               user.delete()

               messages.error(request, 'Account deleted successfully!')

               return redirect('store')


        return render(request, 'account/delete-account.html')



# ZARZADZANIE KONTEM
@login_required(login_url='my-login')
def profile_management(request):

        user_form = UpdateUserForm(instance=request.user)
# AKTUALIZACJA MAILA I NICKU
        if request.method == 'POST':

                user_form = UpdateUserForm(request.POST, instance=request.user)

                if user_form.is_valid():

                        user_form.save()

                        messages.success(request, 'Profile updated successfully!')

                        return redirect('dashboard')



        context = {'user_form':user_form}

        return render(request, 'account/profile-management.html', context=context)




# SLEDZENIE ZAMOWIEN
@login_required(login_url='my-login')       # user jest zalogowany na track orders
def track_orders(request):
        pass


# kupowanie widok
@login_required(login_url='my-login')
def manage_shipping(request):
        pass