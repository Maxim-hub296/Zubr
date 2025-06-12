from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class CustomRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "auth/registration.html"
    success_url = reverse_lazy("shop:products")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"Аккаунт {username} успешно создан! Теперь вы можете войти.")

        # Автоматическая аутентификация после регистрации
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user is not None:
            login(self.request, user)
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field.capitalize()}: {error}")
        return super().form_invalid(form)

class MyLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, f"Добро пожаловать, {self.request.user.username}!")
        return reverse_lazy("shop:products")

    def form_invalid(self, form):
        messages.error(self.request, "Неверное имя пользователя или пароль")
        return super().form_invalid(form)


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("shop:products")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Вы успешно вышли из системы")
        return super().dispatch(request, *args, **kwargs)
