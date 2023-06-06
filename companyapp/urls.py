from django.urls import path,include
from.import views


urlpatterns = [
   path('',views.company_Details, name='company_Details'),
   path('companydata/',views.companydata,name='companydata'),
   path('view_company_details/',views.view_company_details,name='view_company_details'),
   path('editcompany/<int:id>/',views.editcompany,name='editcompany'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>/',views.delete,name='delete'),
   ]