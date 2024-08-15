from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, BasketItem


def index(request):
    courses = Course.objects.all()
    if(request.user.is_authenticated):
        basket_items = BasketItem.objects.filter(user=request.user)
        for course in courses:
            for basket_item in basket_items:
                if course.title == basket_item.course.title:
                    course.is_basket_item = True
    return render(request, 'shop/courses.html', {'courses': courses})

def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if(request.user.is_authenticated):
        basket_items = BasketItem.objects.filter(user=request.user)
        for basket_item in basket_items:
                if course.title == basket_item.course.title:
                    course.is_basket_item = True
    return render(request, 'shop/single_course.html', {'course': course})

def personal_info(request):
    return render(request, 'shop/personal_info.html')

def view_basket(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    total_price = sum(basket_item.course.price for basket_item in basket_items)
    return render(request, 'shop/basket.html', {'basket_items': basket_items, 'total_price': total_price})

def add_to_basket(request, course_id):
    course = Course.objects.get(id=course_id)
    basket_item, created = BasketItem.objects.get_or_create(course=course, 
                                                       user=request.user)
    basket_item.quantity += 1
    basket_item.save()
    return redirect('shop:index')

def remove_from_basket(request, item_id):
    basket_item = BasketItem.objects.get(id=item_id)
    basket_item.delete()
    return redirect('shop:view_basket') 



