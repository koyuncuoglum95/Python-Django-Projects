from django.shortcuts import render

from first_app.models import AccessRecord


# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'help/index.html', context=date_dict)