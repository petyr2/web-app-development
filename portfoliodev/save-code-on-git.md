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

Your entire portfolio/ project is now saved online. 🎉

# Next Time You Make Changes

Whenever you edit code inside webdevelopment/portfolio, run:

```
git add .
git commit -m "Update portfolio"
git push
```

That keeps your GitHub repo up-to-date.
