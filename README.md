# CustomDjangoSkeleton

* Note: This project is in progress and not all features have been added.


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is a template for a Django project (a simple web portal) with the following custom advanced features:
* Custom user model with a case insensitvie unique username and email.
* Login/Logout.
* Secure password reset.
* Custom decorators for restricting access to individual views.
* Custom error handling and page views.
* Custom html tags.
* Background tasks and Crontab for letting python scripts run in the background both instantly and via a schedule. 
* Python multiprocessing.
* Email and Excel modules for end user data delivery.
	
## Technologies
Required tech knowledge:
* Linux (Production Only)
	Ubuntu
* Django
	django_crontab
	background-tasks
* Python
	Decouple
	Pandas
	Multiprocessing
* Postgresql
	This is the current database used by this program.
* See requirements.txt for more
	Download needed installs: pip3 install -r requirements.txt 
	Update requirements: pip3 freeze > requirements.txt 

	
## Linux Setup 
* Steps are for Production deployment on Linux Server.  For Development deployment on Mac/Windows, some steps may need to be modified.
1. Connect to server: ssh root@IP.Address 

2. Install system libraries: 
	1. Update Ubuntu: sudo apt-get update 
	2. Install python3: sudo apt-get install python3-pip python3-dev 
	3. Install apache2: sudo apt-get install apache2  apache2-dev  
	4. Install mod_wsgi.mod_wsgi: sudo apt-get install libapache2-mod-wsgi-py3 
	5. pip install mod_wsgi   
	6. Install github: sudo apt-get install git-core git-gui git-doc    
	7. Install virtual environment: sudo pip3 install virtualenv 
	8. Install PostgresSQL: sudo apt-get install postgresql postgresql-contrib 
 
3. Set up PostgreSQL  
	1. Switch to postgresql account user: sudo -u postgres psql
	2. Create new database user: createuser typeUserNameHere  
	3. Create password for user: psql -c "ALTER USER typeUserNameHere WITH PASSWORD 'typePasswordHere'" 
	5. Create new database: CREATE DATABASE typeProjectNameHereAllLowerCase;
	6. Change new database owner to new user: ALTER DATABASE typeProjectNameHereAllLowerCase OWNER TO typeUserNameHere;
	7. Exit: exit 
 
4. Set up Django project: 
	1. Move to parent directory of project: cd /path/to/parentDirectory 
	2. Load git hub repository: 
		1. Set git identity:  
			1. git config --global user.name "typeUserNameHere"  
			2. git config --global user.email "typeUserEmailHere"  
		2. Initialize an empty git repository: git init 
		3. Clone repository: git clone typeHttpsClonedGitUrlHere 
	3. Move to project directory: cd typeProjectDirectoryHere 
	4. Create virtual environment: virtualenv venv -p python3 
	5. Activate virtual environment: source venv/bin/activate 
	6. Install requirements: pip3 install -r requirements.txt (this will install Django and all project specific library files) 
	7. Create or Copy environmental file: .env
		Note: See envTemplate.txt for guide and required variables
		1. Create new secret key:  
		2. Switch to production (unless using for development only): DEBUG=False 
		3. Add server IP: ALLOWED_HOSTS=.localhost, typeServerIPHere, typeServerNameHere
		4. Update database user: DBUSER=typeUserNameFromStep3.2Here 
		5. Update database user password: DBPASSWORD=typeUserPasswordFromStep3.4Here 
	8. Create or Copy sh files: processTaskSingleCron.sh, processTasksMultiCron.sh
		 Note: See shTemplate.txt for guide
	9. Migrate django database: 
		1. Create 0001_postgres_extenions.py script and place in UserManagement/migrations
			Note: Copy content from 0001_postgres_extenionsTemplate.txt 
		2. python3 manage.py makemigrations 
		3. python3 manage.py migrate 
	10. Create django superuser: 
		1. python3 manage.py createsuperuser 

5. Set up Apache configuration: 
	1. Create/Edit configuration file: nano etc/apache2/sites-available/typeServerNameHere.conf
																						   
		<VirtualHost *:80>

			ServerAdmin webmaster@localhost

			ServerName CtypeServerNameHere

			ServerAlias www.typeServerNameHere

			DocumentRoot /var/www/html

			TimeOut 20000

			ErrorLog ${APACHE_LOG_DIR}/error.log
			CustomLog ${APACHE_LOG_DIR}/access.log combined

			ProxyRequests On
			ProxyPass /serverconf http://localhost:8000/
			ProxypassReverse /serverconf http://localhost:8000/

			#Root Directory
			<Directory /var/www/html>
				<RequireAny>
					#Company Network allowed
					Require ip typeIpHere
					#Company VPN allowed
					Require ip typeIpHere
					#All others refused
					Require all denied
				</RequireAny>
			</Directory>

			#Django Websites
			################################################
			#typeProjectName Live 
			Alias /media/ /var/www/html/typeProjectName/media/
			Alias /static/ /var/www/html/typeProjectName/static/
			<Directory /var/www/html/typeProjectName>
					#Don't list Directories/Files 
					Options -Indexes
					<RequireAny>
						#Company Network allowed
						Require ip typeIpHere
						#Company VPN allowed
						Require ip typeIpHere
						#All others refused
						Require all denied
					</RequireAny>       
			</Directory>
			WSGIDaemonProcess typeProjectName processes=2 threads=4 python-path=/var/www/html/typeProjectName python-home=/var/www/html/typeProjectName/venv
			WSGIScriptAlias /typeProjectName /var/www/html/typeProjectName/typeProjectName/wsgi.py process-group=typeProjectName
			WSGIApplicationGroup %{GLOBAL}

		</VirtualHost>
		'# vim: syntax=apache ts=4 sw=4 sts=4 sr noet 
	2. Test the configuration file with the command: apachectl configtest
	3. Restart the apache server with the command: service apache2 restart 
	4. Check the status of the apache server with the command: service apache2 status 




# Trouble shooting
error: django.db.utils.OperationalError: could not connect to server: Connection refused
	Postgres didn't close properly:
		On Mac: Library -> Application Support -> Postgres -> Delete postmaster.pid










