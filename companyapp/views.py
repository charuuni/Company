from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def company_Details(request):
    return render(request,'company_Details.html')
def companydata(request):
    if request.method=="POST":
        name=request.POST.get('Companyname')
        description=request.POST.get('Companyaddress')
        contactnumber=request.POST.get('contactnumber')
        companyimage=request.FILES['companyimage']

        data=company(companyname=name,companyaddress=description,contactnumber=contactnumber,companyimage=companyimage)
        data.save()
        return redirect('view_company_details')

def view_company_details(request):
    data=company.objects.all()
    return render(request,'view_company_details.html',{'key':data})
def editcompany(request,id):
    data=company.objects.filter(id=id)
    return render(request,'editcompany.html',{'data':data})
def update(request,id):
    if request.method=='POST':
        company_name=request.POST['Companyname']
        company_address=request.POST['Companyaddress']
        contact_no=request.POST['contactnumber']
        try:
            companyimage=request.FILES['companyimage']
            fs = FileSystemStorage()
            file = fs.save(companyimage.name, companyimage)
        except MultiValueDictKeyError:
            file =company.objects.get(id=id).companyimage

        data=company.objects.filter(id=id).update(companyname=company_name,companyaddress=company_address,contactnumber=contact_no,companyimage=companyimage)
        return redirect('view_company_details')
def delete(request,id):
    data=company.objects.filter(id=id).delete()
    return redirect('view_company_details')
    
