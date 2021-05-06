from django.shortcuts import render,redirect,HttpResponse
from .models import employee,department,group,employinfo
# Create your views here.
def index(request):
    return HttpResponse('<h1>hello world</h1>')
def test(request):
    hi='hi,the world is beautiful666'
    test='this is a page for test'
    return render(request,'test.html',{'hi':hi,'test':test})
def list_dep_old(request):
    dep_list=department.objects.all()
    return render(request,'list_dep_old.html',{'dep_list':dep_list})

def add_dep_old(request):
    if request.method=='post':
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
        if dep_name.strip()=='':
            return render(request,'test_orm_old/templates/add_dep_old.html',{'error_info':'部门不能为空！'})
        try:
            p=department.objects.create(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old')
        except Exception as e:
            return render(request,'test_orm_old/add_dep_old.html',{'error_info':'输入部门名称重复或有误!'})
        finally:
            pass
    return render(request,'test_orm_old/add_dep_old.html')

