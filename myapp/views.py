from django.shortcuts import render,redirect,HttpResponse
from .models import employee,department,group,employinfo
import os
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
    if request.method=='POST':
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
        if dep_name.strip()=='':
            return render(request,'add_dep_old.html',{'error_info':'部门不能为空！'})
        try:
            p=department.objects.create(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old')
        except Exception as e:
            return render(request,'add_dep_old.html',{'error_info':'输入部门名称重复或有误!'})
        finally:
            pass
    return render(request,'add_dep_old.html')

def edit_dep_old(request,dep_id):
    dep_object = department.objects.get(id=dep_id)
    if request.method=='POST':
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
        if dep_name.strip()=='':
            return render(request,'edit_dep_old.html',{'error_info':'部门不能为空！'})
        try:
            p=department.objects.filter(id=dep_id).update(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old')
        except Exception as e:
            return render(request,'edit_dep_old.html',{'error_info':'输入部门名称重复或有误!'})
        finally:
            pass
    return render(request,'edit_dep_old.html',{'department':dep_object})

def del_dep_old(request,dep_id):
    department.objects.filter(id=dep_id).delete()
    return redirect('/test_orm_old/list_dep_old')

def list_group_old(request):
    group_list=group.objects.all()
    return render(request,'list_group_old.html',{'group_list':group_list})

def add_group_old(request):
    if request.method=='POST':
        group_name_a=request.POST.get('group_name')
        group_script_a=request.POST.get('group_script')
        if group_name_a.strip()=='':
            render(request,'add_dep_old.html',{'error_info':'团体不能为空'})
        try:
            g=group.objects.create(group_name=group_name_a,group_script=group_script_a)
            return redirect('/test_orm_old/list_group_old')
        except Exception as e:
            return render(request,'add_group_old.html',{'error_info':"部门为空或者"})
        finally:
            pass
    return render(request,'add_group_old.html')

def edit_group_old(request,group_id):
    group_object=group.objects.get(id=group_id)
    if request.method=='POST':
        group_name=request.POST.get('group_name')
        group_script=request.POST.get('group_script')
        if group_name.strip()=='':
            render(request,'edit_group_old.html',{'error_info':"团体不能为空"})
        try:
            g=group.objects.filter(id=group_id).update(group_name=group_name,group_script=group_script)
            return redirect('/test_orm_old/list_group_old')
        except Exception as e:
            return render(request,'list_group_old.html',{'error_info':"输入部门重复或者有误"})
        finally:
            pass
    return render(request,'edit_group_old.html',{'group_object':group_object})

def del_group_old(request,group_id):
    g=group.objects.filter(id=group_id).delete()
    return redirect('/test_orm_old/list_group_old')

def list_employinfo_old(request):
    employinfo_list=employinfo.objects.all()
    return render(request,"list_employinfo_old.html",{'employinfo_list':employinfo_list})

def add_employinfo_old(request):
    if request.method=="POST":
        employinfo_phone=request.POST.get('employinfo_phone')
        employinfo_address=request.POST.get('emplolyinfo_address')
        if employinfo_phone.strip()=="":
            return render(request,"add_employinfo_old.html",{'errorinfo':'电话号码不能为空'})
        try:
            g=employinfo.objects.create(phtone=employinfo_phone,address=employinfo_address)
            redirect('/test_orm_old/list_employinfo_old')
        except Exception as e:
            return render(request,'add_employinfo_old.html',{'errorinfo':'输入信息错误或者重复'})
        finally:
            pass
    return render(request,'add_employinfo_old.html')

def edit_employinfo_old(request,info_id):
    if request.method=='POST':
        employinfo_phone=request.POST.get('employinfo_phone')
        employinfo_address=request.POST.get('employinfo_address')
        if employinfo_phone.strip()=='':
            return render(request,'edit_employinfo_old.html',{'error_info':"手机不能为空"})
        try:
            employinfo.objects.filter(id=info_id).update(phone=employinfo_phone,address=employinfo_address)
            return redirect('/test_orm_old/list_employinfo_old')
        except Exception as e:
            return render(request,'edit_employinfo_odl.html',{'error_info':"输入重复或者错误"})
    return render(request,"edit_employinfo_html")

def del_employinfo_old(request,info_id):
    employinfo.objects.filter(id=info_id).delete()
    return render(request,'list_employinfo_old.html')
