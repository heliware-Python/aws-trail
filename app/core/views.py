from email.mime import base
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import os
import glob
import json
# Create your views here.


@api_view(['GET'])
def home_view(request):
    if request.method == 'GET':
        base_dir = settings.WORKING_DIR
        print(base_dir)
        a = os.path.join(base_dir,"grids")
        if not os.path.isdir(a):
            os.mkdir(a)

        aaaa = {"name":"nandan","pos":"Python develoer"}
        json_object = json.dumps(aaaa, indent = 4)
  
        # Writing to sample.json
        with open("{}/sample.json".format(a ), "w") as outfile:
            outfile.write(json_object)
        for f in glob.glob("{}/*".format(a)):
            print(f)
        with open("{}/sample.json".format(a )) as f:
            data = json.load(f)
        return Response(data)