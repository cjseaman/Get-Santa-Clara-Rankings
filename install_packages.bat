@ECHO OFF
ECHO Installing Packages...

python -m pip install --upgrade pip

pip install requests
pip install bs4
pip install selenium
pip install pandas
pip install openpyxl

ECHO Done!

pause