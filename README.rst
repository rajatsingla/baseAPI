Run python service

* use python3, "definitely works with 3.12.6"
* pip install -r pip-requirements.txt
* createdb -O dev mydatabase, "can skip if using db_url"
* hug -f service.py


NOTE:
change port in service.py under allow_origins.

