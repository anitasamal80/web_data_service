from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm


#for Authenticated view
from django.contrib.auth.decorators import login_required
import pandas as pd

#for plotly
from plotly.offline import plot
import plotly.express as px

from .models import Emp_data


# Create your views here.

def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/charts/') 
    else:
        form = UserCreationForm
    return render(request,"registration/registration.html", {"form" : form})


# View for the Chart Page

@login_required
def chartpage(request):
    emp_data = Emp_data.objects.all()
    projects_data = [
        {
            'Year': x.title,
            'Employee_Rate': x.emp_rate,
        } for x in emp_data
    ]
    
    #create a data frame using pandas
    
    df = pd.DataFrame(projects_data)
    
    
    fig = px.line(
        df, x="Year",  y="Employee_Rate")
    fig.update_yaxes(autorange="reversed")
    
    #Embed the plot in an HTML div tag
    
    gantt_plot = plot(fig, output_type="div")
    context = {'employedata': emp_data, 'plot_div': gantt_plot}
    
    template = loader.get_template('chart_page.html')    
    return HttpResponse(template.render(context,request))
