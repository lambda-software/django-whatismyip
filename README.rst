=================
django-whatismyip
=================

Features
--------
* Very basic Whatismyip application for django.
* Application show the remote ip address of the client in plain-text, 
perfect to be used as remote ip checker for any application or script 
to update DNS records.

Installation
------------
To install it, run the following command inside this directory:

    python setup.py install

Or if you'd prefer you can simply place the included "whatismyip"
directory somewhere on your Python path, or symlink to it from
somewhere on your Python path.

Once you have django-whatismyip in your path, you should add it to

your ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'whatismyip',
        ...
    )

And in the urls.py, you should add this line:
	 urlpatterns = patterns('',
	 	...
	 	url(r'^whatismyip$', include(whatismyip.urls)),
		...
	 )


Use
---
Simply point your browser to /whatismyip directory of your project.

Note
----
This application has been develop using Python 2.7 and Django 1.4,
maybe can run in older version but is not tested. 
You can obtain Python from http://www.python.org/ and
Django from http://www.djangoproject.com/.