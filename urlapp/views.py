from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'I Walk Alone', 'number': 100}
    return render(request,'url_app/index.html',context=context_dict)

def other(request):
    return render(request,'url_app/other.html')

def relative(request):
    return render(request,'url_app/relativeurl.html')

def base(request):
    return render(request,'url_app/base.html')