from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details' : details })

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() #Blog 클래스를 blog라는 객체에 넣어준다.
    blog.title = request.GET['title'] #blog객체의 title변수에 name=title 폼에서 입력한 내용을 GET으로 받는다.
    blog.body = request.GET['body'] #blog객체의 body변수에 name=body 폼에서 입력한 내용을 GET으로 받는다.
    blog.pub_date = timezone.datetime.now() #현재 시점을 받아오는 함수, django.utils timezone 임포트 후 사용
    blog.save() #쿼리셋 메소드(.save), blog 객체에 넣어준 내용을 DB에 저장해준다. / 객체.delete() 삭제 메소드
    return redirect('/blog/'+str(blog.id)) #url은 항상 문자열 