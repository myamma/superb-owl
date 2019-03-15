from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from superb_owl.process import recImg
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
	return render(request, 'index.html')

@csrf_exempt
def process(request):
	if (request.method == "POST"):
		myfile = request.FILES['userImg']
		fs = FileSystemStorage(location=settings.IMG_ROOT)
		filename = fs.save(myfile.name, myfile)
		#running recognition
		res = str(recImg())
		return HttpResponse(json.dumps({"status": 1, "result": res}))

