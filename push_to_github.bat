@echo off
title Push DHANYARAKSHAK to GitHub
echo ======================================================================
echo DHANYARAKSHAK: Push to GitHub
echo Authors: Snehal Patil (25101A2002) ^& Grishma Patil (25101A2003)
echo ======================================================================
echo.

echo Checking repository status...
git status
echo.

echo Pushing code to GitHub (https://github.com/Snehal297/dhanyarakshak)...
git push -u origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ======================================================================
    echo [!] Push failed.
    echo If the error says "Repository not found":
    echo 1. Go to https://github.com/new
    echo 2. Name your repository: dhanyarakshak
    echo 3. Choose Public or Private, and leave "Add a README" UNCHECKED
    echo 4. Click "Create repository"
    echo 5. Run this file again!
    echo ======================================================================
) else (
    echo.
    echo ======================================================================
    echo [SUCCESS] Code pushed successfully to GitHub!
    echo View it at: https://github.com/Snehal297/dhanyarakshak
    echo ======================================================================
)
echo.
pause
