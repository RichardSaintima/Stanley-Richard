from django.shortcuts import render

# Create your views here.
def index(request) :

    context ={}
    return render(request, 'pages/start/index.html',context)


def blog(request) :

    context ={}
    return render(request, 'pages/hobby/blog.html',context)



def proyecto(request) :

    context ={}
    return render(request, 'pages/proyecto/proyecto.html',context)