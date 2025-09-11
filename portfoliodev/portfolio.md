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
	desription = models.TextField()
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

So on my project, I'll be able to access images and it will give me all of these different image models. Now what on delete specifies that if this project that we're linked to were to be deleted, we should delete all of the images. That's what the cascade means okay. Which means delete all of the different images that are associated with the project. If that project is to be deleted.

There's some other options here as well, but this is the one that we're going to use. Lastly we have the image field. And this is just specifying where we actually want to store the images within our media directory. Then we have the string and we're good to go 





