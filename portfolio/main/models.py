from django.db import models

#tag model.
class Tag(models.Model):
	name = models.CharField(max_length=100, unique=True)

	#def_str_(self)
	#	return self.name


#project models.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	tags = models.ManyToManyField(Tag, related_name="projects")
	link = models.URLField(max_length=200, blank=True)

	#def_str_(self)
	#return self.title
		

#image model.
class ProjectImage(models.Model):
	project = models.ForeignKey(
		Project, related_name="images", on_delete=models.CASCADE
		)
	image = models.ImageField(upload_to="project_images/")

	#def_str_(self)
	#return f"{self.project.title} Image"