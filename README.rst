cookiecutter-mezzanine
==========================

A cookiecutter_ template for Mezzanine.

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Features
---------

* Mezzanine_ 3.1
* Django 1.6
* South 1.0

.. _Mezzanine: http://mezzanine.jupo.org 


Constraints
------------

- SQLite 3 database	


Usage
------


Database:

CONFIG_SECTION=filathome fab setup_pgsql

```bash

$ mkdir -p ~/www/dev/

$ cd ~/www/dev/

$ git clone https://github.com/unbit-is/fil-home .

$ mkdir -p projects/web/filathome.it

$ cd projects/web/filathome.it

$ virtualenv venv

$ source venv/bin/activate


$ pip install cookiecutter

$ cookiecutter https://github.com/mauriziobit/cookiecutter-mezzanine.git


CREATE DATABASE filathome_db3 WITH OWNER filathome ENCODING 'UTF-8'
CREATE DATABASE volleysport_db2 WITH OWNER volleysport ENCODING 'UTF-8'


(venv)30121@filathome:~/www/dev/projects/www/filathome.it$ cookiecutter https://github.com/mauriziobit/cookiecutter-mezzanine.git
Cloning into 'cookiecutter-mezzanine'...
remote: Counting objects: 71, done.
remote: Compressing objects: 100% (42/42), done.
remote: Total 71 (delta 23), reused 71 (delta 23)
Unpacking objects: 100% (71/71), done.
Checking connectivity... fatto.
project_name (default is "project_name")? project
repo_name (default is "project")? filathome
author_name (default is "Your Name")? Maurizio Branca
email (default is "Your email")? maurizio@unbit.it
description (default is "A short description of the project.")? Filathome web site
year (default is "Current year")? 2014
with_documentation (default is "yes")?
environment (default is "dev")? dev
production_domain (default is "domain.com")? filathome.it
current_domain (default is "dev.domain.com")? dev.filathome.it
execution_mode (default is "dev")? dev
container_id (default is "30116")? 30121

atleti.volleysport.it

$ DJANGO_SETTINGS_MODULE=settings.dev python project/manage.py

```






First, get cookiecutter. Trust me, it's awesome::

$ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/mauriziobit/cookiecutter-mezzanine.git


You'll be prompted for some questions, answer them, then it will create a Mezzanine project for you.

Then you can enter in the new project directory::

	$ cd <repo_name>


Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/dev.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Now run the ``createdb`` command::

	$ python manage.py createdb

And answer to all the question that will be prompted.

The last step is collect all the static files::

	$ python manage.py collectstatic

You can now run the usual Django ``runserver`` command::

    $ python yourapp/manage.py runserver
