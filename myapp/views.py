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
        employinfo_phone=request.POST.get('phone')
        employinfo_address=request.POST.get('address')
        if employinfo_phone.strip()=='':
            return render(request,"add_employinfo_old.html",{'error_info':'电话号码不能为空'})
        try:
            g=employinfo.objects.create(phtone=employinfo_phone,address=employinfo_address)
            return redirect('/test_orm_old/list_employinfo_old')
        except Exception as e:
            return render(request,'add_employinfo_old.html',{'error_info':"输入有误"})
        finally:
            pass
    return render(request,'add_employinfo_old.html')

def edit_employinfo_old(request,info_id):
    employinfo_object=employinfo.objects.get(id=info_id)
    if request.method=='POST':
        employinfo_phone=request.POST.get('phtone')
        employinfo_address=request.POST.get('address')
        if employinfo_phone.strip()=='':
            return render(request,'edit_employinfo_old.html',{'error_info':"手机不能为空"})
        try:
            employinfo.objects.filter(id=info_id).update(phone=employinfo_phone,address=employinfo_address)
            return redirect('/test_orm_old/list_employinfo_old')
        except Exception as e:
            return render(request,'edit_employinfo_old.html',{'error_info':"输入有误"})
    return render(request,"edit_employinfo_old.html",{"employinfo":employinfo_object})

def del_employinfo_old(request,info_id):
    employinfo.objects.filter(id=info_id).delete()
    return redirect('/test_orm_old/list_employinfo_old')

def list_employee_old(request):
    employee_list=employee.objects.all()
    return render(request,'list_employee_old.html',{'employee_list':employee_list})

def del_employee_old(request,emp_id):
    employee.objects.filter(id=emp_id).delete()
    return  redirect('/test_orm_old/list_employee_old')
def add_employee_old(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        dep=request.POST.get('dep')
        info=request.POST.get('info')
        salary=request.POST.get('salary')
        groups=request.POST.getlist('group')
        new_emp=employee.objects.create(name=name,email=email,salary=salary,dep_id=dep,info_id=info)
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_employee_old/')
    dep_list=department.objects.all()
    group_list=group.objects.all()
    info_list=employinfo.objects.all()
    return render(request,'add_employee_old.html',{'dep_list':dep_list,'group_list':group_list,'info_list':info_list})

def edit_employee_old(request,emp_id):
    emp_list=employee.objects.get(id=emp_id)
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        dep=request.POST.get('dep')
        info=request.POST.get('info')
        salary=request.POST.get('salary')
        groups=request.PSOT.get('group')
        new_emp=employee.objects.create(name=name,email=email,salary=salary,dep_id=dep,info_id=info)
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_employee_old/')
    dep_list=department.objects.all()
    group_list=group.objects.all()
    info_list=employinfo.objects.all()
    return render(request,'edit_employee_old.html',{'emp':emp_list,'dep_list':dep_list,'group_list':group_list,'info_list':info_list})

def test_foreign(request):
    emp=employee.objects.get(id=2)
    dep_name=emp.dep.dep_name
    dep_obj=department.objects.get(id=2)
    emp_list=dep_obj.employee_set.all()
    emp_names=[emp.name for emp in emp_list]
    return HttpResponse('1.正向关联：员工名称：{0}，所在部门名称：{1}<br> 2.反向查找：部门名称：{2}，部门员工：{3}'.format(emp.name,dep_name,dep_obj.dep_name,emp_names))