from django.urls import path, include
from .models import CategoryResource, CourseResource
from tastypie.api import Api


api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
