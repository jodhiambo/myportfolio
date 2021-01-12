from django.shortcuts import render
# from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# def index(request):
#     return HttpResponse("hello")

def home(request):
    
    return render(request, 'mainapp/index.html')



def about(request):

	return render(request, 'mainapp/about.html')



def portfolio_details(request):

	return render(request, 'mainapp/portfolio-details.html')



# def inner_page(request):

# 	return render(request, 'mainapp/inner-page.html')


# def portfolio_details(request):

# 	return render(requet, 'mainapp/portfolio-details.html')