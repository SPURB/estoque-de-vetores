call activate
set FLASK_APP=server.py
set FLASK_DEBUG=1
set /p host=<host.txt
flask run -h %host%
python server.py