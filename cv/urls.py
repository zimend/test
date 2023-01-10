from django.urls import path
from . import views


urlpatterns = [
    #path('bonjour/', views.bonjour),
    #path('users/', views.showProfile),
    path('', views.IndexView.as_view()),
    path('portfolio/<slug:slug>>', views.PortfolioDetailView.as_view(), name="portfolio"),
    # path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
    # path('section/', views.SectionsList.as_view()),
]