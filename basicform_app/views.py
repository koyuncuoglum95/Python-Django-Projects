from django.shortcuts import render
from basicform_app.forms import Formname, NewUser

# Create your views here.
def index(request):
    return render(request, 'basicformapp/index.html')

def form_name_view(request):
    form = Formname()

    # This is used when creating something like registration or posting message or images like social media
    if request.method == 'POST':

        # The following code requests all input of Formname from forms.py
        form = Formname(request.POST)

        # If there are all input of the form
        if form.is_valid():

            print('VALIDATION SUCCESS!')
            # form.cleaned_data[input name from Formname]
            print("NAME:" + form.cleaned_data['name'])
            print("EMAIL:" + form.cleaned_data['email'])
            print("TEXT:" + form.cleaned_data['text'])

    return render(request, 'basicformapp/form_page.html',{'form': form})


def form_user_view(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID !')

    return render(request,'basicformapp/usersform.html',{'form':form})