from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm


# Create your views here.

#메인페이지
def main(request):
    return render(request, 'crudApp/main.html')

#글쓰기페이지
def new(request):
    return render(request, 'crudApp/new.html')

#글쓰기 함수
def create(request): # 2.Form과 관련된 view를 호출
    if request.method == "POST": # view에서 다시 한번 우리가 POST형식으로 요청받은 method를 확인
        form = PostForm(request.POST) # form이 우리가 Forms.py에 작성해서 받기로 한 정보들을 다 받았는가(유효성 검증 시작)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save() # form의 입력값 유효성 검증 끝
            return redirect('read') # form이 잘 입력되었다고 판단되면(valid 판정) 지정한 url(성공 url)로 이동
    else: # 잘 입력되지 않았을 경우 폼을 다시 입력을 받기
        form = PostForm
        return render(request, 'crudApp/new.html', {'form':form})

#읽기페이지
def read(request):
    posts = Post.objects # Post의 객체들을 posts라는 변수에 담아서
    return render(request, 'crudApp/read.html', {'posts':posts}) # {} : Post의 객체가 담겨있는 posts라는 변수를 html에서는 posts라는 변수로 표현하겠다. 라는 뜻

#디테일페이지
def detail(request, id):
    post = get_object_or_404(Post, id = id) # Post 모델에서 id 값을 post라는 변수에 담아 가져오려 하는데, 만약 id값을 제대로 가져오지 못하면 404에러를 일으킬거야! 라는 함수
    return render(request, 'crudApp/detail.html', {'post':post})

#수정페이지
def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # instance는 우리가 수정 할 글이 어떤 글인지 글의 id를 함수에게 설명해주는 코드
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = PostForm(instance=post)
        return render(request, 'crudApp/edit.html', {'form':form})

#삭제 함수
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete() # delete()는 말 그대로 특정 id값을 가진 데이터를 삭제해주는 함수
    return redirect('read')