# Django-API
Create API for proxy IP address.
Here, "home" is one app directory, in which home.models consist database tabel "IPdata".
home.urls file consist all type of url inputs and according to urlpattern particuler view is returned.
In home.views file all views are included according to view type, different class are created.
In home.serializer file include all different serializer.

Links are:

LocalHost:8000/home/                   -->Returns List of all IP
LocalHost:8000/home/x.x.x.x/           -->Returns Details of Specific IP
LocalHost:8000/home/var_country/       -->Returns All IP where country = var_country
LocalHost:8000/home?country=x          -->Returns All IP where country = x (Same as Above)
LocalHost:8000/admin/                  -->Admin Page
LocalHost:8000/home/create/            -->To Create a New Object
LocalHost:8000/home/x.x.x.x/edit/      -->To Edit Object which have IP Address = x.x.x.x
LocalHost:8000/home/x.x.x.x/delete/    -->To Delete Object which have IP Address = x.x.x.x

NOTE : Last three Links(Edit, Delete, Create) can only access by Admin User.
       Here, IP address is primary key field.
  
