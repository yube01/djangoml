from django.shortcuts import render
from joblib import load
from rest_framework.decorators import api_view #new
from rest_framework.response import Response    #new

model = load('./savedModels/model.joblib')

@api_view(['GET','POST'])
def predictor(request):

    if request.method == 'POST':
        
        sepal_length = request.data['sepal_length']
        sepal_width = request.data['sepal_width']
        petal_length = request.data['petal_length']
        petal_width = request.data['petal_width']


        # sepal_length = request.POST.get('sepal_length')
        # sepal_width = request.POST.get('sepal_width')
        # petal_length = request.POST.get('petal_length')
        # petal_width= request.POST.get('petal_length')
        
        # print( sepal_length)
        # print(request.data)
        y_pred =  model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred[0] == 0:
            y_pred = 'setso'
        elif y_pred[0] == 1:
            y_pred = 'vesticolor'
        else:
            y_pred = 'virginca'
        
        return Response({'result':y_pred})
        # return render(request, 'main.html' , {'result': y_pred})

    return Response({'message':"This is the main page to show and add the datas!"})
    # return render(request, 'main.html')


