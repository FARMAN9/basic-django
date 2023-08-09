from django.shortcuts import *
from django.http import *

# Create your views here.
def homepageX(resquest):
    return HttpResponse("homeX")
def adddataX(resquest):
    return HttpResponse("insertX")
def updatedataX(resquest):
    return HttpResponse("updataX")
def finddataX(resquest):
    return HttpResponse("viewdataX")
def deletedataX(resquest):
    return HttpResponse("deletedX")