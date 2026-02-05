@echo off
echo ========================================
echo Cancer Prediction ML - GitHub Upload
echo ========================================
echo.

REM Configure Git with your information
echo [1/6] Configuring Git...
git config --global user.name "Shravan Niranjan Ajetrao"
git config --global user.email "sna443388@gmail.com"
echo Done!
echo.

REM Initialize Git repository
echo [2/6] Initializing Git repository...
git init
echo Done!
echo.

REM Add all files
echo [3/6] Adding all files...
git add .
echo Done!
echo.

REM Create initial commit
echo [4/6] Creating initial commit...
git commit -m "Initial commit: Cancer Prediction ML Project - Complete professional structure with documentation"
echo Done!
echo.

REM Rename branch to main
echo [5/6] Setting up main branch...
git branch -M main
echo Done!
echo.

REM Add remote repository
echo [6/6] Connecting to GitHub repository...
git remote add origin https://github.com/Shravan44338/Cancer-Prediction-ML.git
echo Done!
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next step: Push to GitHub
echo Run this command:
echo.
echo   git push -u origin main
echo.
echo You will be prompted for your GitHub credentials.
echo.
echo If you have 2FA enabled, use a Personal Access Token instead of password.
echo Create token at: https://github.com/settings/tokens
echo.
pause
