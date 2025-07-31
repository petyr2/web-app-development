# steps for setting up a few things

  # DISCLAIMER
  
  I'll be doing my work on a Linux operating system, so all of my work will be based on Debian-based systems in that case.

  # First

   Create a directory where you shall be performing all of your tasks
   ```bash
mkdir [your_directory]
```
Then `cd` into your directory.
In the directory, create a virtual environment by
```bash
python3 -m venv env
```
Launch the environment 
```bash
source enve/bin/activate
```
Now you are working on a controlled environment.

Install `django` in the environment 
```bash 
pip3 install django # if the command doesn't work, use pipx instead
```

Check whether Django is working through `django-admin`, where this shows different commands to use with Django
Create a project using
```bash
django-admin startproject [name of your project] .<img width="192" height="192" alt="logo-O35E636P" src="https://github.com/user-attachments/assets/ddbc2827-f443-4f99-acaa-27b8957883bf" />

```
On doing `cd`, you will see there are some script and directory create. We shall be using this to create our website

We are going to launch a text editor of your choice, where we shall be writing the code from


The manage.py script acts as our virtual command interface.

We can use the virtual command interface to create the app, which we shall link it to our project which we created earlier. Since the project is independent

To create the app, we shall use:
```bash
django-admin startapp your_app_name
```

To link your app navifgate to the project folder and open settings.py file, navigate to the section with installed_apps and add the app there

<img width="297" height="189" alt="Screenshot From 2025-07-31 01-26-41" src="https://github.com/user-attachments/assets/98d6536f-d678-4ec0-bb53-e215404ef091" />

Since we don't want to write our URL patterns on the project, let's navigate to the folder where we have created the app in, and in the folder, let's create a file and call it urls.py to create we are going to use

```bash
touch urls.py
```

To link the file we have created with our project, we are going to navigate to our project folder in the folder open the urls.py, and  import include in the file, then link our file to our project, as shown below:

<img width="493" height="189" alt="Screenshot From 2025-07-31 01-39-13" src="https://github.com/user-attachments/assets/239d8373-7c5f-41ce-9aea-d5cc0178a0dc" />

# Let's create the models

Models are like the tables in the database

The way to create the models locate the directory where the app was created and run models.py, in there we shall import the models from django.db using 
```bash
from django.db import models
```

Then we create classes for the user and vendor

















































  
