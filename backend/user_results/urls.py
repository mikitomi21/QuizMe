from django.urls import path
from .views import ResultDetailView, ResultCreateView, ResultListView, UserResultDetailView

urlpatterns = [
    path("", ResultListView.as_view(), name="result-list"),
    path("<int:pk>", ResultDetailView.as_view(), name="result-detail"),
    # path("", ResultCreateView.as_view(), name='result-create'),
    path("user/<int:pk>", UserResultDetailView.as_view(), name="result-user"),
]
