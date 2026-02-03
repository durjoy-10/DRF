# DRF

<img width="1133" height="666" alt="image" src="https://github.com/user-attachments/assets/1a9e78a4-9f01-47eb-9811-f3b9a655663e" />
<img width="1133" height="666" alt="image" src="https://github.com/user-attachments/assets/0a676d3b-68de-428a-90ec-d79c8862c4b2" />

### First create virtual enev
```
python -m venv env
```
### activate virtual env
```
source env/bin/activate
```
### Installation
```
pip install django
pip install djangorestframework
```

### create project
```
django-admin startproject project_name .
```

### Run server
```
python manage.py runserver
```

<img width="845" height="176" alt="image" src="https://github.com/user-attachments/assets/73230d52-ce8f-4baf-8050-1991d454e5b9" />


### create an app (web application end point)
```
python manage.py createapp students
```

### Then add it to installed apps in main project 
<img width="683" height="244" alt="image" src="https://github.com/user-attachments/assets/5190b481-6d4f-42d8-b811-73da275e22d8" />

### Now update project folders urls.py for set the urls of the app students 
<img width="661" height="187" alt="image" src="https://github.com/user-attachments/assets/3b7721fc-18e6-4fa1-9c2a-1f91f62f106c" />

### Now in students/urls.py
<img width="661" height="187" alt="image" src="https://github.com/user-attachments/assets/1abe8c81-b9eb-4f51-bbd2-928cb21ebd50" />

### Now view of the students/views.py
<img width="655" height="250" alt="image" src="https://github.com/user-attachments/assets/2266ae00-a8f6-4260-ad7b-ba21a64c6c76" />

### Create an app (api end-point)

```
 python manage.py createapp api
```

### Now update project folders urls.py for set the urls of the api 
<img width="665" height="259" alt="image" src="https://github.com/user-attachments/assets/4e3d97f3-319d-4fc7-b966-580a832a190b" />


### Now in api--> urls.py
<img width="452" height="150" alt="image" src="https://github.com/user-attachments/assets/99118447-07f1-44c7-bfb2-79228dc79f55" />


### Now in api--> views.py
<img width="832" height="337" alt="image" src="https://github.com/user-attachments/assets/46707bad-76d9-42e1-b9e3-5734f0769931" />


## Create model.. 
### create default db table using migrate
```
python manage.py migrate
```

### Create a superuser
```
python manage.py createsuperuser
```

### create a model in student app --> models.py
<img width="832" height="337" alt="image" src="https://github.com/user-attachments/assets/f30690fa-7497-4974-8426-2c2f2342f1dd" />


### after updating or changing models.py we have to run these two comands..
```
python manage.py makemigrations
python manage.py migrate
```

### but now the model is not added in the db --> admin ..
### For that we have to register the model in the app --> students/admin.py
<img width="832" height="171" alt="image" src="https://github.com/user-attachments/assets/dd4e53df-0e10-487e-baac-0f3911c17121" />


### Now create some user in student model/table
<img width="940" height="171" alt="image" src="https://github.com/user-attachments/assets/85e42ff0-b5eb-429e-9ead-3d7a4339de67" />

### now fetch the data using the api...First fetch using manual way without serializer

<img width="968" height="354" alt="image" src="https://github.com/user-attachments/assets/55d89d5d-b5d4-40ef-82f4-6270297e7daa" />

---
## Now using model serializer 
### First create api/serializers.py
<img width="968" height="354" alt="image" src="https://github.com/user-attachments/assets/d7496a1a-908c-4b9b-b24a-b6cd232e2885" />

### now use the serializers for get request in the api/views.py
<img width="971" height="455" alt="image" src="https://github.com/user-attachments/assets/f7884ba0-cf8b-4595-8a0e-7f560de9a388" />


### now storing data using serializer using POST method..Updating api/views.py
<img width="807" height="281" alt="image" src="https://github.com/user-attachments/assets/423b1b06-104e-43b5-bec7-81d27134ab17" />

----------

## Get a single object primary key based operation
### First update api/urls.py
<img width="807" height="281" alt="image" src="https://github.com/user-attachments/assets/f8cecfbf-533c-4f12-bd07-dd416b566481" />

### Now create the view studentdetailView in api/view.py for get a particular student 
<img width="807" height="281" alt="image" src="https://github.com/user-attachments/assets/0c5277ee-51d0-41dd-b403-7cae26acc5e9" />

----------

----------
## Update operation on student (PUT Request) in the same view studentdetailView
<img width="808" height="353" alt="image" src="https://github.com/user-attachments/assets/0cf46605-b1c8-49ae-ad3c-efe378046245" />

---------

## Delete operation (delete a student using delete method) in the same view studentdetailView
<img width="761" height="424" alt="image" src="https://github.com/user-attachments/assets/8023412c-cdd0-4234-9e80-422f3a4d471a" />

------------
------------
------------
------------
## Class based view
### For learning class based view first i am creating an app name employee
```
python manage.py startapp employees
```

### then register the app in the project/settings.py
<img width="480" height="270" alt="image" src="https://github.com/user-attachments/assets/71cf7bca-d11b-4181-925d-5d558ab08e83" />

### Now update employees/models.py for creating a new table(model) named Employee
<img width="696" height="377" alt="image" src="https://github.com/user-attachments/assets/84ce435d-1bf9-4176-b555-f92f1548f205" />

### Now register the model in employees/admin.py
<img width="533" height="196" alt="image" src="https://github.com/user-attachments/assets/cf5eb628-6179-4ac7-a017-50376d1c1741" />

### Now i have to use migrate command for updating models.py
```
python manage.py makemigrations
python manage.py migrate
```
### Running the server now i am showing another table in /admin/ named Employee
```
python manage.py runserver
```
<img width="964" height="416" alt="image" src="https://github.com/user-attachments/assets/03a3e170-b88c-4f0b-a937-d117efb3c47a" />


### Now create another serializer for the Employee model.. For that i have to update api/serializers.py

<img width="964" height="416" alt="image" src="https://github.com/user-attachments/assets/7ac16ca4-c088-4ae3-8976-5575ecc5aaa7" />

### Now update the api/urls.py for employee and here i linked a class based in the urls.py 
<img width="964" height="416" alt="image" src="https://github.com/user-attachments/assets/f693747a-d19c-4f4d-9ae0-3a918f251b6f" />

### Update api/views.py for creating the class based view named employees_class_view ..Here i make get and post request in one class ..Here don't need the decorator

<img width="964" height="445" alt="image" src="https://github.com/user-attachments/assets/bd17b983-9ff8-4aea-84b1-807940ac320d" />

### Getting single object using pk ..Getting an employee, update an employee , delete an employee
### Let's create an url patterns for this..
<img width="964" height="445" alt="image" src="https://github.com/user-attachments/assets/8a185152-9b79-4a6c-87b8-713e38ac4fea" />

### Now update the code of api/urls.py for get a particular employee using employee_detail_view (class) 
<img width="964" height="445" alt="image" src="https://github.com/user-attachments/assets/dc0ea7e8-8a91-41f5-b633-56ac540ca9c7" />

### Now implement put request for update a particular employee ..For that update the api/views.py

<img width="964" height="445" alt="image" src="https://github.com/user-attachments/assets/e3711971-a1d0-4a58-ab42-a12fd06a4ab5" />

### Now implement delete request for delete a particular employee ..For that update the api/views.py

<img width="964" height="445" alt="image" src="https://github.com/user-attachments/assets/0f0ec21a-ebb7-49ba-85fe-f7abb453aa2f" />

------------
---------------
------------
-----------
## Mixins Overview
---
### Mixins are reusable code classes in oop that provide specific functionalities..In django rest framework, mixins are used to add common functionality to views.
### 1. Create   2.Read    3.Update    4.Delete
### 5 types of mixins for performing crud operation in simple --> ListModelMixin, CreateModelMixin, RetriewModelMixin, UpdateModelMixin, DestroyModelMixin
<img width="1008" height="568" alt="image" src="https://github.com/user-attachments/assets/cca798cc-3fe2-42e6-9ce6-ca7e0d3314b7" />

<img width="1139" height="568" alt="image" src="https://github.com/user-attachments/assets/9089e698-7be6-454d-848c-d886351776a4" />


### LIST & Create Mixins for retrive data from db & create new data in db
----
#### First update api/urls.py for creating new view for genrics class based view
<img width="1115" height="149" alt="image" src="https://github.com/user-attachments/assets/966f581c-8dee-4f05-a0cb-5f2dd3fda05f" />


#### Now update api/views.py for LIST & Create Mixins for retrive data from db & create new data in db
<img width="1115" height="281" alt="image" src="https://github.com/user-attachments/assets/6357f080-2d8d-49d8-9e94-ef47e6d4b630" />

###### It gives an html format for post request by GenericAPIView 

#### Now create another view named GenericStudentDetailView for get a particular employee, create update a particular employee , delete a particular employee
###### get a particular employee using RetrieveModelMixin
<img width="1115" height="438" alt="image" src="https://github.com/user-attachments/assets/50e3c00e-092b-4621-b37b-92b32cffe65a" />

###### Now update and delete a particular empoyee using UpdateModelMixin and DestroyModelMixin
<img width="1115" height="312" alt="image" src="https://github.com/user-attachments/assets/93149ffa-1492-4f1d-9e70-86feeb8d054c" />

---------
----------
----------
----------
## Generics Overview 
<img width="1144" height="639" alt="image" src="https://github.com/user-attachments/assets/12f0abc7-8811-4ee9-b2ce-f8c14aaa8410" />

### Now first understand about generics.listapiview, generics.createapiview and genericslistcreateapiview
#### Create 2 new urls in api/urls for performing the operation using generics 
<img width="1415" height="420" alt="image" src="https://github.com/user-attachments/assets/4df8af51-f1ea-404e-9614-fb5cbe1ee530" />

#### Now update api/views.py ..creating a class named GenericEmployeesListCreateView which retrive data from db using generics.ListAPIView
<img width="1635" height="904" alt="image" src="https://github.com/user-attachments/assets/4361c10b-8349-4ff2-9b99-a0e741fff2b2" />

#### Update the class named GenericEmployeesListCreateView for fetch the data and perform also post request to db..
<img width="1635" height="904" alt="image" src="https://github.com/user-attachments/assets/e8e2acef-0230-407b-a7f3-f5a85ab18f68" />

#### Now create another class named GenericEmployeesDetailView for fetch a particular employee(RetrieveAPIView), update a particular employee(UpdateAPIView), delete a particular employee(DestroyAPIView)
###### Here RetrieveAPIView helps ro get single record using lookup_field 
###### UpdateAPIView helps to update record using lookup_field
###### DestroyAPIView helps to delete record using lookup_field
<img width="1819" height="904" alt="image" src="https://github.com/user-attachments/assets/4e9536db-7ee9-4bcb-9a4f-06c87d6cc029" />


----------------
----------------
----------------
----------------
## Viewsets Overview
-------

<img width="1154" height="547" alt="image" src="https://github.com/user-attachments/assets/caded57c-bbd9-4d50-8dc6-61a823ba4651" />

### List and Create Data using Viewset
-----
###### First i am updating the api/urls.py and create new url for viewset functionalities..
<img width="1154" height="547" alt="image" src="https://github.com/user-attachments/assets/97d4e0ba-cfbc-4bcb-a1cd-bec760302582" />

##### Now create the class named viewset-employees in api/views.py
###### Fetch the data from db and performing post request for creating a new employee
<img width="1154" height="547" alt="image" src="https://github.com/user-attachments/assets/68c8c6f2-c68d-41a1-b565-af675a12e0d1" />

###### Fetch a particular employee, Update a particular employee & Delete a particular employee using viewset..Here don't need to create another url for particular employee because  router automatically handles that in api/urls.py

<img width="1154" height="547" alt="image" src="https://github.com/user-attachments/assets/4eb21494-1eae-4f3c-9085-2d8b25cae1ba" />

--------------
-------------
------------
## ModelViewSet --> It automatically perform all the pk and non-pk activities in few lines of cviewset-employees/ode..
-----------
###### For that first create a new url ..update api/urls.py
<img width="1154" height="222" alt="image" src="https://github.com/user-attachments/assets/c243d05d-5486-4c08-98dd-e7ebdfd33c01" />

###### Now create a new class in api/views.py for implement ModelViewSet which automatically provides implementations for list, create, retrieve, update, and destroy actions.
<img width="1154" height="222" alt="image" src="https://github.com/user-attachments/assets/262729b1-59cf-4b6d-a7ff-67fc1573e266" />

--------------
------------
------------
--------------
## Nested Serializer 
----------
#### Why nested serializer is used ??
```
Nested serializers in Django Rest Framework (DRF) are primarily used to represent relationships between different data models in a single, unified data structure, typically a JSON or XML
```
#### Let's understand nested serializer step by step..For this purpose i created a new app name blogs
```
python manage.py startapp blogs
```
#### Now register the app in the main project file/settings.py
<img width="1154" height="436" alt="image" src="https://github.com/user-attachments/assets/d9a12882-44ae-4307-afed-685d8ae8f307" />

#### Now update the blogs/models.py for creating 2 class named Blog,Comment...Here in Comment class "on_delete=models.CASCADE" is used for if the blog is deleted the the comment of this comment class is also deleted...
<img width="923" height="365" alt="image" src="https://github.com/user-attachments/assets/c8f9ae61-5e52-4236-9196-1a325a91cb62" />

#### Registering the models Blog and Comment in blogs/admin.py 
<img width="655" height="269" alt="image" src="https://github.com/user-attachments/assets/c7986ee1-9e22-42d3-b87e-915d9f77d751" />

#### Now i have to run makemigration and migrate command for create the table named Blog and Comment in admin database

```
python manage.py makemigrate
python manage.py migrate
```
<img width="645" height="133" alt="image" src="https://github.com/user-attachments/assets/13f32608-f86c-4b5b-bfbd-96858c37e427" />


#### Making nested serializer for here one blog id there have multiple comments
<img width="923" height="336" alt="image" src="https://github.com/user-attachments/assets/f8df320b-1607-4da5-8482-29e9c4ef42f9" />

#### Now update api/urls.py for create another url and view for blog and comment where nested serializer is implemented ..and here i use model viewset for creating the api
<img width="1014" height="365" alt="image" src="https://github.com/user-attachments/assets/407aa77d-abf1-42ab-b88a-7a383c697e89" />

#### Update api/views.py for BlogViewSet and CommentViewSet which is implemented by ModelViewSet
<img width="1014" height="290" alt="image" src="https://github.com/user-attachments/assets/582407db-b607-41fd-aa52-f191482b2c80" />

#### Now show the view in the browser running the server
#### in comment :
<img width="1014" height="770" alt="image" src="https://github.com/user-attachments/assets/c4a4489d-53fb-4814-b89f-6075788f3e18" />

#### In blog: Here Nested serialization is implemented
<img width="1014" height="770" alt="image" src="https://github.com/user-attachments/assets/2e319bac-cec3-4f03-8bc0-92e4df7db5ac" />

-----------------
-------------
---------------
----------------
## Primary Key based operation on Blog Comment Model using generics retrive, update ,destrory view
----------------

##### First of all configure the api/urls.py 
<img width="1347" height="351" alt="image" src="https://github.com/user-attachments/assets/3145076c-b81c-477f-b5c9-1ecf26528717" />

#### Now create the views named BlogDetailView and CommentDetailView which can fetch, update and delete a particular blog and a particular comments...updating api/views.py

<img width="1347" height="351" alt="image" src="https://github.com/user-attachments/assets/03e37733-d63d-4883-b8b3-b862cfb160dc" />


<img width="1347" height="967" alt="image" src="https://github.com/user-attachments/assets/50757d6d-5ac5-4ddb-baea-832010b55fda" />


<img width="1347" height="967" alt="image" src="https://github.com/user-attachments/assets/18664df7-eb5b-4765-8ec3-791988bf4b14" />

----------------------------
--------------------------
----------------------------
-----------------------------

## Pagination Overview 
-----------
<img width="1245" height="543" alt="image" src="https://github.com/user-attachments/assets/1b0218a1-ff19-4e2a-b9a3-5dc9c814a02b" />

##### Example : 
<img width="1245" height="380" alt="image" src="https://github.com/user-attachments/assets/05d1254a-8935-4206-98ea-6be1309ae3c7" />

--------------------
### First Implement Global Pagination 
-----------
#### Global pagination is automatically use in the genrics and viewset views...
#### Now Configure the project file/settings.py for setting Global Pagination ...django_rest_main/settings.py
<img width="1225" height="466" alt="image" src="https://github.com/user-attachments/assets/e6509810-2b2a-4f89-93c4-6acfc2aee680" />

<img width="1225" height="950" alt="image" src="https://github.com/user-attachments/assets/1ccf7c9a-4eca-444c-b972-aeaed78429b3" />

------------------
### Implement Custom Pagination
--------------------

#### Let's make custom pagination for EmployeeModelViewSet class...api/views.py
<img width="1243" height="206" alt="image" src="https://github.com/user-attachments/assets/3a90a645-f6a0-459a-8f9f-f987b20c60ad" />

#### Now create a file api/paginations.py for making custom pagination for EmployeeModelViewSet class.. The paginations.py also can create in the django_rest_main folder
<img width="1057" height="395" alt="image" src="https://github.com/user-attachments/assets/d9e0313e-b955-4c36-ac15-41c476072b11" />

#### Now First see EmployeeModelViewSet class views which use global pagination
<img width="1057" height="950" alt="image" src="https://github.com/user-attachments/assets/c07028fc-9052-4cc3-9f01-f7a8d8a294bc" />

#### Use this custom pagination to this EmployeeModelViewSet class views...update api/views.py
<img width="1057" height="234" alt="image" src="https://github.com/user-attachments/assets/3f0e2233-eed3-4c54-9f1e-79f34f0e6e43" />

#### Now see EmployeeModelViewSet class views which use custom pagination
<img width="1180" height="808" alt="image" src="https://github.com/user-attachments/assets/92bc0a30-da2e-46c2-a29d-d47b4746939e" />

-------------------
-----------------
----------------
------------------
## Filtering
------------

#### Install django filter
```
pip install django-filter
```
#### Now register the the django-filter in projectFile/settings.py in installed_apps section
<img width="619" height="372" alt="image" src="https://github.com/user-attachments/assets/688947fd-fc99-4bfa-bf7b-588e3f1d326e" />

#### Here we work on 3 use case 
<img width="852" height="455" alt="image" src="https://github.com/user-attachments/assets/7bf43a24-7bec-4a8d-80cd-dc780c95cd71" />

------
#### First understand the use case 1: Filter Employee by position
#### Global filter like pagination..Update project_file/settings.py
<img width="1179" height="341" alt="image" src="https://github.com/user-attachments/assets/e2abfc33-9cde-4d36-ae96-7b5920e27d64" />

#### Now set the filter in EmployeeModelViewSet class views..update api/views.py
<img width="1183" height="235" alt="image" src="https://github.com/user-attachments/assets/0377ff91-8a8a-47b8-a4af-0c1c5e6e8aff" />

#### Here have a problem this globar filter is case sensitive..
<img width="1272" height="547" alt="image" src="https://github.com/user-attachments/assets/1c4779ba-5151-4b63-a618-8df19810cac5" />

#### Now implement custom filter Employee by position which wouldn't be case sensitive
#### create employees/filters.py ..It also can create in api
<img width="1255" height="243" alt="image" src="https://github.com/user-attachments/assets/2a62d0bb-a61e-4d25-a953-9ec5ea0cae27" />

#### Now set this filter functionalities to the EmployeeModelViewSet class views ..update api/views.py
<img width="1255" height="243" alt="image" src="https://github.com/user-attachments/assets/e508c60d-0d38-4e03-bc52-b3cfb97b6823" />

#### Now the filter by position is case insensitive ...
<img width="1223" height="560" alt="image" src="https://github.com/user-attachments/assets/a3c3eb2b-291e-46ee-bd07-e19a2d6f3d61" />

---------
#### Use case 2: add another filteration by first_name of the employee..Here I just simply add filteration code in employees/filters.py
<img width="1223" height="296" alt="image" src="https://github.com/user-attachments/assets/afcc0312-a1bb-4df1-8d62-24d84a0768b5" />

#### Now check the filteration 
<img width="1223" height="652" alt="image" src="https://github.com/user-attachments/assets/a2e654cc-d2a9-4dc0-9195-970e0d03d543" />
<img width="1223" height="652" alt="image" src="https://github.com/user-attachments/assets/cecd151b-decc-465e-b349-158029a6733b" />
#### Here I can use any one filter or 2 filters at a time like and operation 

------
#### Use case 3: Filter Employee by emp_id range ..But I can't directly use rangefilter because it only works for integer number but my emp_id is charfeild..I can use rangefilter directly for id which is integer..
#### For use range filteration by emp_id(char_feild) i have to use advanced method.. For that updating employees/filters.py
<img width="1223" height="534" alt="image" src="https://github.com/user-attachments/assets/1c360b48-2b81-40a8-85b2-296e3332a37b" />

#### Now check the range filteraion by emp_id which is charfeild
<img width="1223" height="898" alt="image" src="https://github.com/user-attachments/assets/c3ce6880-230d-49ca-8ee5-5d512f245c59" />

-------------
-------------
-------------
---------------
## Search Filters
-----------
#### Search by any word in blog title in blog app ..And it is case insensitive
#### For that I have to simply update the BlogViewSet class view in api/views.py
<img width="1223" height="137" alt="image" src="https://github.com/user-attachments/assets/96028652-0da2-4302-bac7-c7ffe7eebd39" />


#### Check the filteration
<img width="1249" height="987" alt="image" src="https://github.com/user-attachments/assets/6e1c5cc5-09aa-4bdc-8cc7-133cb9e34097" />
#### Now change the search in url to q ..Update django_rest_main/settings.py
<img width="1249" height="266" alt="image" src="https://github.com/user-attachments/assets/e2d0bcd5-910d-44f0-8d57-0bbb030c5401" />
#### Check: change 'search' to 'q'
<img width="643" height="48" alt="image" src="https://github.com/user-attachments/assets/303b8b9e-caf9-4e9d-bed1-aea516e0dfa5" />

#### Also search by any word in content in blog ..
#### Simply added content to search_feilds..
<img width="809" height="129" alt="image" src="https://github.com/user-attachments/assets/efe7e8d0-708e-42e8-98bd-ea5a8b2cdb10" />
#### Check :
<img width="1277" height="714" alt="image" src="https://github.com/user-attachments/assets/18a207f8-bdd0-4400-98ab-2692e277e225" />

#### We can also use search filer by the first word of a feild ..Let's try by the title and content feild..Here i have to simply give ^title and ^content to the search_feilds which in the BlogViewSet class view
<img width="876" height="112" alt="image" src="https://github.com/user-attachments/assets/8600161f-b931-42db-9561-ccfc1ecfa49c" />


#### Check:
<img width="1245" height="823" alt="image" src="https://github.com/user-attachments/assets/0aa4f0bb-58ee-4955-87d8-d4d7847d6ad5" />

------------

## Ordering Filters
--------
#### simply added OrderingFilter to filter_backends and ordering_feilds=['created_at'] in BlogViewSet class view in api/views.py

<img width="1245" height="243" alt="image" src="https://github.com/user-attachments/assets/4492015f-72c5-4fc8-aac6-61017a6f3213" />

#### Check:
<img width="1345" height="893" alt="image" src="https://github.com/user-attachments/assets/366d7341-2dc6-4804-af74-643fc234518d" />

----------------
---------------
----------------
----------------

