from django.shortcuts import render
from .models import customer_details
from .forms import customer_detailsForm


def create_view(request):
	
	context ={}

	form = customer_detailsForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)

 
def list_view(request):

    context ={}
 
    context["dataset"] = customer_details.objects.all()
         
    return render(request, "list_view.html", context)

def update_view(request):

    context ={}
 
    context["dataset"] = customer_details.objects.all()
         
    return render(request, "update_view.html", context)