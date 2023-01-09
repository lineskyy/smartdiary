from django.urls import path
from . import views
app_name = 'cal'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('event_new/', views.event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/$',views.event,name='event_edit'),
    path('calendarr/',views.CalendarView.as_view(),name='calendarr'),
]