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



