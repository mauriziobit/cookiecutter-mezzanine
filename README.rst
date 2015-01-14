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

- PostgreSQL 9.3 database


Usage
------

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

* `pip`
* `virtualenv`

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
