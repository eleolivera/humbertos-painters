from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views, forms


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('djcrm.urls', namespace='djcrm_app')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^leads/', include('leads.urls', namespace='leads')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^oppurtunities/', include('oppurtunity.urls', namespace='oppurtunities')),
    url(r'^cases/', include('cases.urls', namespace='cases')),
    url(r'^emails/', include('emails.urls', namespace='emails')),
    url(r'^planner/', include('planner.urls', namespace='planner')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': forms.AuthenticationForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}, name='logout'),

]