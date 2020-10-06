from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import Jobserializers
from django.utils import timezone
import datetime
# Create your views here.

def view(request):
    ac=Job.objects.all().exclude(Expiry_Date__lte=timezone.now())
    template=loader.get_template('jobs_view.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))
class JobList(APIView):
    def get(self,request):
        JOB=Job.objects.all().exclude(Expiry_Date__lte=timezone.now())
        serializer=Jobserializers(JOB,many=True)
        return Response(serializer.data)

    def post(self):
        pass