from django.shortcuts import render
from rango.models import Category
# from django.http import HttpResponse


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all of less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def about(request):
    message = {'message': "This tutorial has been put together by ANTI-MUSOR"}
    return render(request, 'rango/about.html', context=message)


