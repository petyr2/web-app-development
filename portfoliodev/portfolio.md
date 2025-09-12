# I'll be using Python + JavaScript and Django to develop my portfolio.

First, the installation of Django and Pillow is required, where Pillow will assist in displaying images within the project.

Installation, we shall use `pip` for Windows and `pip3` for Linux or Mac

In Linux, if it refuses to install, we can use `pipx` or create a virtual environment using:

```
python3 -m venv myenv                              
source myenv/bin/activate
```

From there, we will create Django project using:

```
django-admin startproject portfolio
                  #or
python3 -m django-admin startproject portfolio
```

Then `cd` into the project, in our case is the `portfolio`, when in the project we shall create the main app using:

```
python3 manage.py startapp main
```

Now we can open a text editor and modify the code. I will use Sublime Text.

Navigate into to portfolio directory, then open the `settings.py` file and edit by adding `import os`

`import os stands for import operating system.`

Then move on to the section where it says `installed_apps` 

We shall add our app, in my case, it is `main`, to link it with Django.

At the bottom of the settings.py file, we are going to write some settings that will help us to add some images later on the app we are going to use 

```python
MEDIA_URL = "/media/"    #This is the directory where we're going to store different media files
MEDIA_ROOT = os.path.join(BASE_DIR, "mdeia") #where the media folder is actually stored
```
We are now done with setting the setting.py, we are then going to set the  main

What we're going to do is we're going to create some database entries or database models for storing our different projects.

The idea here is rather than hardcoding the projects in, what we'll do is we'll create a database field or a database kind of model, and we will allow ourselves to dynamically add projects, edit them, or modify them later on. 
This way, this can be kind of a living website, and as you create new projects, you can update the site by adding new projects to the database. 

Now, in order to do that, we need to create some models.

Now, in Django, I'm going to go to the models.py file. By the way, we use something called `ORM` is an `object relational mapping`. Now this means that rather than writing all of this custom SQL code or database logic, we simply write some Python code, and then Django will map that Python code to the appropriate database operation.

So what you're going to see here is we're going to define in Python what we want the data that we're going to store for our projects looks like. And then Python will automatically handle adding that to the database, getting it from the database, updating it, doing all of that tough stuff that we don't want to deal with. So what we're going to start by doing is going into `models.py` and we're going to define a class which is known as a Django model as follows:

```python
#tag model.
class Tag(models.Model):
	name = models.CharField(max_lenth=100, unique=True)

	def_str_(self):
		return self.name

		
#project models.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	tags = models.ManyToManyField(Tag, related_name="projects")
	link = models.URLField(max_length=200, blank=True)

	def_str_(self):
		return self.title
```
# simple description of the code above on the tag field

Many to many, meaning this tag can exist on many different projects, and this project can have many different tags. Now, what we do is we specify the model that we want the relationship to be with. And then we have a related name. Now the related name is the field name on this tag that will contain all of the projects. So effectively, what's going to happen is that for each of our projects, we're going to have a linkage to the tag.

And for each of our tags, we're going to have a link to all of the different projects that that tag exists on. That's kind of how many too many field works. These other types of relationships and so on. 

# Lastly, is the image model

```python
#image model.
class ProjectImage(models.Model):
	project = models.ForeignKey(
		project, related_name="image", on_delete=models.CASCADE
		)
	image = models.ImageField(upload_to="project_images/")

	def_str_(self):
		return f"{self.project.title} Image"
```

# What is the image model doing

But since we can have multiple images or no images, we don't know how many we're going to have. We need to make a new model that will store images for our individual project. That way we can have multiple of them linked to the project. Now, the first thing we need to do for each of our images is we need to understand what project they're associated with.

Now, unlike our tags, one project image won't exist for multiple different projects. It's just one project image exists for one project, right? So this project can have multiple images, but this image can only be associated with one project. So in that case, we use the foreign key. Now what this means is that we always have a single project for our individual images.

Now I know I've repeated that like five times. So I'm just trying to be specific here. And what we do is we specify that we're gonna have a foreign key with the project model, and then the related name is the field that will exist on this project that stores all of the different images.

So on my project, I'll be able to access images, and it will give me all of these different image models. Now, what on delete specifies that if this project that we're linked to were to be deleted, we should delete all of the images. That's what the cascade means, okay. Which means delete all of the different images that are associated with the project. If that project is to be deleted.

There's some other options here as well, but this is the one that we're going to use. Lastly, we have the image field. And this is just specifying where we actually want to store the images within our media directory. Then we have the string and we're good to go 

# At this point, we have to register our models manually on the admin page. The way to do this is we navigate to the main directory and then open the `admin.py` file

Now, the admin page or the admin portal is something that's provided by Django to allow us to automatically manage our different models.

So what we're going to do is import our models from the models file that we just created. We're going to say `from .models import Tag, Project, ProjectImage`. And we're going to register them. Now we can just register them like this by default. But since we have some more complex models here, we have some links between tags, projects, etc...

What we're going to do is we're going to write a kind of custom registration. Now, what the custom registration means is that we can specify the different fields that we want to have and how we want to view these different projects. 

Let's start by doing the project.

```python
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("title", "link")
	inlines = []
	search_fields = ("title", "description")
	list_filter = ("tags",)
```

Then we have inlines. Now, what I'm going to do is to find something that will be displayed inline. And the reason why we need this is because we're going to have other models that are associated with this project, and we want to edit them at the same time, rather than editing them separately.  

```python
class ProjectImageInline(admin.TabularInline):
	model = ProjectImage
	extra = 1
```

Now, extra equal to one just specifies how many of these we're going to be displaying in line. In this case, we're going to display one, which means by default we're asking the user to upload one image. But we could be asking them to upload, say, four images or five images if we specified it like that. Okay. Now inside of inline. So we're going to say project image inline. And again, what this is going to do for us is it's now going to display this that we've just defined, which is really a view to be able to upload an image while we are creating these different projects.


Lastly, we're going to define our tag admin, and this is going to be admin dot model admin. This one will be a little bit easier. We're going to say list display. And this is going to be equal to simply name. And then we're going to have our search underscore fields. And this will just be equal to name.
Again, remember that trailing comma. So just how we list it and how we search for it. 

```python
class TagAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name",)
```

We are going to register our field using:

```python
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
```

Now, what we need to do is start actually running the server. We need to make some migrations, which I'll talk about in a second, and then we can sign into the admin panel, and we can see what we actually just coded out. So let's go up to our terminal here.

And what we're going to do is start by applying some migrations. Now whenever we make changes to our different models, what we need to do is we need to make migrations and then we need to apply them. Now, making migrations will create some files inside of Django in this migrations directory, which you can see here, which will specify the changes that need to be applied to the underlying database in order for the changes that we made to actually be applied.

Once that file is created, then we need to apply those migrations by running the secondary command. So pretty much whenever you make any changes, you're going to run both of these commands in sequence if you are affecting your models.

The commands to use are 

```bash
python3 manage.py makemigrations  #After running this, we run

python3 manage.py migrate   #this is to apply the changes
```

After all this, we are going to create a super user by:

```bash
python3 manage.py createsuperuser
```
Then set the user name and password, not a must, you input the email address

Then let's run the server by 
```bash
python3 manage.py runserver
```

We accessed the admin panel of our site, and then we want to customize our site.

In the main directory, we have to create the static and templates directories, where we shall be storing our CSS, JS, and HTML code

Additionally, we create two directories in the static folder: one for CSS and another for JS, as these files do not typically change.

We're going to make a new file inside of main called urls.py, okay. And this is where we're going to place some URLs. to kind of link the different views that we create. And inside of here, we're going to say URL patterns is equal to an empty list. We're going to write in that later. But for now, we'll just put it there so we don't get any errors, okay. So what did we just do?

We created the templates directory, the static directory with CSS and JS. And then we created the urls.py file with URL patterns with an empty list. Make sure you've done that. Now main is set up. And what we can start doing is actually rendering some content into our views. So what we're going to do now is go to views.py. Now, in Django, when we actually want to display a page, we need to create something known as a view.

Now, a view is a function that will be called when we go to a specific route. A route is something like slash or slash home or slash project with Id1. We need to write all of those programmatically. So what we're going to do here is we're going to start by importing our models. 

```python
from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here.
def home(request):
	return render(request, "home.html")

def bio(request):
	return render(request, "bio.html")


def projects(request):
	return render(request, "portfolio.html")


def elevator_pitch(request):
	return render(request, "elevator_pitch.html")


def contacts(request):
	return render(request, "contacts.html")
```

Then we shall create HTML files in the templates directory as follows
```
base.html
home.html
bio.html
portfolio.html
elevator_pitch.html
contacts.html
```









