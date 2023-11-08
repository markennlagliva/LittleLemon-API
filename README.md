# LittleLemon-App
Back-End Developer Capstone
✅ Django REST API

# Dependencies <br>
- pipenv <br>
- django <br>
- mysqlclient <br>
- django-livereload-server <br>
- djangorestframework <br>

# API endpoints

Available API endpoints -> protected api's. Needed a valid credentials before viewing. <br>

'menu/' -> Show the List of available Menus <br>
'menu/<int:pk>/' -> Retrieve a specific Menu <br>
<br>
Obtaining Authentication Tokens <br>
restaurant: <br>
'api-token-auth/' <br> 
<br>
little-lemon api: <br>
'api/api-token-auth/' <br>
<br>
Note: Registered users only can Obtain Tokens <br>
<br>
'restaurant/booking/tables' -> show all the booked tables <br>
<br>
LittleLemonAPI <br>
'api/menu-items/' -> show all the available Menus <br>
'api/menu-items/<int:pk>' -> show single resource available Item <br>
'api/message/' -> Test Protection of API <br> 
<br> 
Tools used for testing API's <br>
-> Browsable API provided by django-rest-framework package <br>
-> Insomia <br>


