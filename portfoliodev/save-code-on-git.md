# Step-by-Step: Save portfolio to GitHub

# 1. Go into your project folder

Open terminal in Kali:

```
cd ~portfolio
```

# 2. Initialize Git inside that folder
```
git init
```

This tells Git: “Track this folder as a project.”

# 3. Add your project files to Git

```
git add .
git commit -m "First commit - Portfolio project"
```

The . means all files in this folder.

The -m is your commit message (you can write anything).

# 4. Create a GitHub repository

Log in to GitHub
.

Click New repository.

Name it portfolio (or whatever you want).

Leave Initialize with README unchecked.

Click Create repository.

# 5. Link your local project to GitHub

Copy the repo link from GitHub (HTTPS). Example:

```
https://github.com/yourusername/portfolio.git
```

Now connect it:

```
git branch -M main
git remote add origin https://github.com/yourusername/portfolio.git
```

# 6. Push your code to GitHub

```
git push -u origin main
```

or

If you want to keep what’s already on GitHub (like a README), just pull first:

```
git pull origin main --rebase
git push origin main
```

git pull --rebase brings down changes from GitHub and applies your commits on top.

Then git push will succeed.

Your entire portfolio/ project is now saved online. 

# Next Time You Make Changes

Whenever you edit code inside webdevelopment/portfolio, run:

```
git add .
git commit -m "Update portfolio"
git push
```

That keeps your GitHub repo up-to-date.

If you wipe your system, don’t worry. Just clone it back:

```
git clone https://github.com/yourusername/portfolio.git
cd portfolio
pip install -r requirements.txt
python manage.py runserver
```
# ADDITIONAL INFO

# If you just want to reuse the existing remote

Check what remote is set:

```
git remote -v
```

You should see something like:

```
origin  https://github.com/petyr2/web-app-development.git (fetch)
origin  https://github.com/petyr2/web-app-development.git (push)
```

If it already points to the correct GitHub repo, you don’t need to add it again.

You can skip git remote add origin ... and just push with:

```
git push -u origin main
```
# If the remote is wrong and you want to replace it

Remove the existing one:

```
git remote remove origin
```

Then add the correct one:

```
git remote add origin https://github.com/petyr2/web-app-development.git
```

And push:

```
git push -u origin main
```

# ON THE LOGIN SECTION

GitHub no longer allows using your account password for git push. Instead, you must use either:

A Personal Access Token (PAT) (recommended for HTTPS URLs), or SSH keys (recommended if you use the same machine often).

Use a GitHub Personal Access Token (HTTPS method)

Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic).

Or click here when logged in: Generate token
.

Click Generate new token → choose Classic.

Set a name (e.g., Kali Git).

Expiration: pick a long one (e.g., 90 days or “no expiration”).

Select scopes: at minimum repo.

Copy the token (GitHub will only show it once).
