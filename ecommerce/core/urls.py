"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import SetPasswordForm
from django.urls import path, reverse_lazy, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns

from views.decorators import login_forbidden

from webapps.customer.forms import PasswordResetForm


# password_reset_form = get_class('customer.forms', 'PasswordResetForm')
password_reset_form = PasswordResetForm
set_password_form = SetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(

    # WEBPAPPS
    path('', include('webapps.urls')),

    # API
    path('api/v1/', include('api.urls')),

    # Password reset - as we're using Django's default view functions,
    # we can't namespace these urls as that prevents
    # the reverse function from working.
    path('password-reset/',
        login_forbidden(
            auth_views.PasswordResetView.as_view(
                form_class=password_reset_form,
                success_url=reverse_lazy('password-reset-done'),
                template_name='registration/password_reset_form.html'
            )
        ),
        name='password-reset'),
    path('password-reset/done/',
        login_forbidden(auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        )),
        name='password-reset-done'),
    path('password-reset/confirm/<str:uidb64>/<str:token>/',
        login_forbidden(
            auth_views.PasswordResetConfirmView.as_view(
                form_class=set_password_form,
                success_url=reverse_lazy('password-reset-complete'),
                template_name='registration/password_reset_confirm.html'
            )
        ),
        name='password-reset-confirm'),
    path('password-reset/complete/',
        login_forbidden(auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        )),
        name='password-reset-complete'),
) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
