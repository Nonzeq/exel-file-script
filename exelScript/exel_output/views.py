import os
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
from .services import main
import shutil
from time import sleep


def home(request):
    if request.method == "POST":
        first_file = request.FILES["First"]
        second_file = request.FILES["Second"]

        exel_file = Uploader(
            first_exel_file=first_file,
            second_exel_file=second_file,
        )
        exel_file.save()
        out = main(first_file,second_file)
        out_file = Uploader(
            out_file=out,
        )
        out_file.save()
        return redirect(to='download_template')
    else:
        try:
            all_files = Uploader.objects.all()
            all_files.delete()
            delete_file()
        except:
            return render(request, template_name='exel_output/index.html')
    # files = Uploader.objects.filter(out_file=out_file)
    # context = {
    #     'files': files
    # }

    return render(request, template_name='exel_output/index.html')


def download_template(request):
    return render(request, template_name='exel_output/download.html')


def exemple(request):
    return render(request, template_name='exel_output/exemple.html')


def download_file(request):
   the_file = 'media/exel/NEW_UPDATE_FILE.xlsx'
   filename = os.path.basename(the_file)
   chunk_size = 8192
   response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                           content_type=mimetypes.guess_type(the_file)[0])
   response['Content-Length'] = os.path.getsize(the_file)
   response['Content-Disposition'] = "attachment; filename=%s" % filename
   return response


def delete_file():

    path = os.path.join(os.path.abspath(os.path.dirname(__file__))[1:1:-1], 'media/exel')
    shutil.rmtree(path)




