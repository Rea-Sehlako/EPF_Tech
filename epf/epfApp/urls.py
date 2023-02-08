from django.urls import path
from .views import home, plot_graph

# urls(templates) to the different pages, imported from line 2
urlpatterns = [
    # 1 which is the home page
    path('', home, name='customer_form'),
    # 2nd is when the graph is being displayed
    path('graph/', plot_graph, name='plot_graph')
]
