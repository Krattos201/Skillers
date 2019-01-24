# Skillers


Download Files
1>demo1.zip
2>djangoproject.zip

Setup and Install
python 3.5 and above required
create virtual environment, if you want using virtaulenv command
install dependent libraries
unzip all folders
go to cd demo1
run server using 'python manage.py runserver 0.0.0.0:8084'
go to cd djangoproject
run server using 'python manage.py runserver'

FILES:-

File views.py contains all the functions which are being executed through the website.
models.py contains the classes used in the web applications.
namer.py contains all the external functions that perform the necessary operations and are imported into views.py for execution
urls.py contains all the urls included in the web application.
trainingdata.yml is generated after the training of the faces and will be used for detection during the face recognition process.
The templates folder contains all the web pages that are displayed during the execution of the procedure.
The demo1 folder contains the demo website which is used to display the initial prototype.

PROCEDURE:-

At first login page of the demo1 folder will run which will direct the user to our portal. Here the new users will have the option to register themselves whereas the existing users can directly proceed for login. During registration the necessary details of the user is asked and hence after the mobile no. verification and generating the dataset for face recognition a user-id is provided. This user-id can be used to login to their respective accounts. After the successful 2 step verification, the user will finally be redirected to the webpage he tried to log into.
