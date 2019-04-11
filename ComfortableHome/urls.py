from django.contrib.auth import views
from django.urls import include, path
from common.views import handler404, handler500

app_name = 'ComfortableHome'

urlpatterns = [
    path('', include('common.urls', namespace="common")),
    path('', include('django.contrib.auth.urls')),
    path('staff/', include('accounts.urls', namespace="accounts")),
    path('homeowners/', include('leads.urls', namespace="leads")),
    path('contacts/', include('contacts.urls', namespace="contacts")),
    path('polls/', include('opportunity.urls', namespace="opportunities")),
    path('requests/', include('cases.urls', namespace="cases")),
    path('news/', include('news.urls', namespace='news')),
    path('emails/', include('emails.urls', namespace="emails")),
    # path('planner/', include('planner.urls', namespace="planner")),
    path('logout/', views.LogoutView, {'next_page': '/login/'}, name="logout"),
]

handler404 = handler404
handler500 = handler500
