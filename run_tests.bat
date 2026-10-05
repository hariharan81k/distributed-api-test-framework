@echo off

echo ==============================
echo Running API Test Framework
echo ==============================

python -m pytest -v --html=reports/test-report.html --self-contained-html

echo.
echo ==============================
echo Test execution completed
echo Report: reports/test-report.html
echo ==============================