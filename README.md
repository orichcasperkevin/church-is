church-is
# church information system back end
The backend to the church system

## Contributing

Follow these steps to start contributing  
1.Clone the project, `https://github.com/orichcasperkevin/church-is.git`   
2.cd to the project root and create a python virtualenv .NOTE .this project runs on python 3.7, be sure that this is the version you are using.    
3.Activate the virtualenv. run `pip install -r requirements.txt ` to install dependencies  
4.Then copy .env.example to .env and make the necessarily changes to configure your environment. On unix systems `cp .env.example .env`  
5.Migrate to update the database schema `python manage.py migrate`. Make sure to use postgresql because the system depends on postgres specific features.    
6.Create super user to access the admin `python manage.py createsuperuser`    
7.Finally run your development server. `python manage.py runserver`  

In case of questions . open a github issue.
thanks
