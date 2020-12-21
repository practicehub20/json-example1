from django.shortcuts import render
from app2.utils import getTrainData


def train_search(request):
    name = request.POST.get('t1')
    data = getTrainData(name)
    print(data)
    if type(data) == dict or data == []:
        return render(request, 'content.html', {'error': 'Sorrry... Your Requested Train Is Not Availlable.'})
    else:
        return render(request, 'content.html', {'result': data,'name':name.upper()})