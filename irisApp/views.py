from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

def predictor(request):
    return render(request, 'main.html')


def formInfo(request):
    sepal_length = request.GET['sepal-length']
    sepal_width = request.GET['sepal-width']
    petal_length = request.GET['petal-length']
    petal_width= request.GET['petal-width']
    y_pred =  model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    if y_pred[0] == 0:
        y_pred = 'setso'
    elif y_pred[0] == 1:
        y_pred = 'vesticolor'
    else:
        y_pred = 'virginca'

    return render(request, 'result.html' , {'result': y_pred})