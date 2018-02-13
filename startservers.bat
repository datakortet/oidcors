@echo off

call sethost dserver
echo start python dserver\manage.py runserver dserver:7000
start python dserver\manage.py runserver dserver:7000

call sethost oidcserver
echo start python oidcserver\manage.py runserver oidcserver:8000
start python oidcserver\manage.py runserver oidcserver:8000

call sethost clientserver
echo start python clientserver\manage.py runserver clientserver:9000
start python clientserver\manage.py runserver clientserver:9000

start http://dserver:7000
start http://oidcserver:8000
start http://clientserver:9000
