from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout

class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, self.template_name)
            

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if username != '' or password != '':
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/home')
                else:
                    error_message = "Account has been disabled !!!"
            else:
                error_message = "Invalid credentials !!!"
        else:
            error_message = "Username/Password required !!!"

        return render_to_response(self.template_name, {'error_message' : error_message})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')