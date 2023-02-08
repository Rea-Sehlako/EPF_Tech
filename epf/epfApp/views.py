from django.shortcuts import render, redirect
from .forms import CustomerForm
import pandas as pd
import matplotlib.pyplot as plt
from .models import Customer


# function that validates and saves the form, should proceed to manipulate data into graph
def home(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plot_graph')
    else:
        form = CustomerForm()
    return render(request, 'home.html', {'form': form})


def plot_graph(request):
    # if request.method == "POST":
    # Retrieve the uploaded Excel file
    customer = Customer.objects.last()
    excel_file = customer.excel_file.path

    # Read the data from the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Plot the graph using matplotlib
    plt.ylabel("Monetary")
    plt.plot(df["Expenses"], label="Expenses", marker='o')
    plt.xlabel("Months")
    plt.plot(df["Income"], label="Income", marker='o')
    plt.grid()
    plt.legend()

    # Save the graph as an image file
    # see how its displayed on templates "temporal_graph.html"
    plt.savefig("static/images/graphs.png")

    # Render the template with the graph data
    return render(request, "temporal_graph.html")

    # If the request method is not "POST", display the HTML form
    # return render(request, "temporal_graph.html")
