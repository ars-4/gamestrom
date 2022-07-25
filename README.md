# gamestrom
This is the open source code to the gamestorm app. Comming soon.

### To Run Locally:
#### RUNTIME: Python 3.10.2
#### Steps:

* Clone the project and `cd` into it


* Create virtual environment:
    * `virtualenv venv` 
    

* Activate Virtual Environment
  * Windows:
    `venv\Scripts\activate.bat`
  * Linux \ MacOS: `source venv\bin\activate`


* Install Requirements:
  * `pip install -r requirements.txt`


* Create Migrations and migrate them to DB:
  * `py manage.py makemigrations`
  * `py manage.py migrate`


* Create superuser:
  * `py manage.py createsuperuser`


* Run the server:
  * `py manage.py runserver`


* Open `http://127.0.0.1:8000/gamestromadmin/`
  * in the db, create 3 Groups initially with the following order:
    * admin
    * expired
    * standard
    * trial


* Create a `Person` object with the current superuser and add him in the `admin` group

#### Congratulations server is running and the endpoint is http://127.0.0.1:8000/

##### since this can run video game on this server an has to do with running video games an licensing please make sure you own the game before running. 
