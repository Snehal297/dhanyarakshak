@echo off
title Push DHANYARAKSHAK to GitHub
echo ======================================================================
echo DHANYARAKSHAK: GitHub Repository Setup & Push
echo Author: Snehal Patil (Roll Number: 25101A2002)
echo ======================================================================
echo.

echo Step 1: Logging in to GitHub via GitHub CLI...
echo Follow the prompts on screen to authenticate (Browser or Token).
echo.
"C:\Program Files\GitHub CLI\gh.exe" auth login

echo.
echo Step 2: Creating GitHub repository 'dhanyarakshak' and pushing code...
"C:\Program Files\GitHub CLI\gh.exe" repo create dhanyarakshak --public --source=. --remote=origin --push

echo.
echo ======================================================================
echo Repository created and pushed successfully!
echo ======================================================================
pause
