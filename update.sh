#!/bin/bash
git pull origin main
git add .
git commit -m "Update on $(date)"
git push origin main
