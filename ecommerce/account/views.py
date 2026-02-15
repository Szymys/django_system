from django.shortcuts import render, redirect

from .forms import CreateUserForm



# ********************************************************************************************


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
                form.save()

                return redirect('')


                
        
        
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
