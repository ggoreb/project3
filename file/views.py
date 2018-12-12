import os

from django.http import HttpResponse
from django.shortcuts import render

from file.models import Article
from project3 import settings

def show(request, id):
    article = Article.objects.get(id=id)
    file = article.file

    filepath = os.path.join(settings.BASE_DIR, file)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    return response

def read(request, id):
    article = Article.objects.get(id=id)
    return render(
        request,
        'file/read.html',
        { 'article': article }
    )

def write(request):
    if request.method == 'GET':
        return render(
            request,
            'file/write.html'
        )
    else:
        title = request.POST['title']
        file = request.FILES['file']

        try:
            os.mkdir('upload')
        except FileExistsError as e:
            pass
        with open('upload/' + file.name, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        Article.objects.create(title=title, file='upload/' + file.name)


    return HttpResponse('ok')

def download(request):
    filepath = os.path.join(settings.BASE_DIR, 'upload1/Desert.jpg')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    return response



def path1(request):
    return render(
        request, 'file/path1.html')

def path2(request):
    return render(
        request, 'file/path2.html')

def upload3(request):
    if request.method == 'GET':
        return render(
            request,
            'file/upload3.html'
        )
    else:
        files = request.FILES.getlist('my_file')

        try:
            os.mkdir('upload3')
        except FileExistsError as e:
            pass

        for file in files:
            f = open('upload3/' + file.name, 'wb')
            for c in file.chunks():
                f.write(c)
            f.close()

    return HttpResponse('ok')



def upload1(request):
    if request.method == 'GET':
        return render(
            request,
            'file/upload1.html'
        )
    else:
        file = request.FILES['my_file']
        print(file.name)  # 파일명
        try:
            os.mkdir('upload1')
        except FileExistsError as e:
            pass

        with open('upload1/' + file.name, 'wb') as f:
            for c in file.chunks():
                f.write( c )
    return HttpResponse(file.name)









