from bboard.models import Bb
from django.urls import path
from .views import BbCreateView, index,by_rubric,deletebb


urlpatterns = [
    path('<int:rubric_id>/',by_rubric,name='by_rubric'),
    path('',index,name='index'),
    path('add/',BbCreateView.as_view(),name='add'),
    path('delete/<int:id>',deletebb,name='delete'),
]
