<h3 style="color:BLUE">DJANGOCMS TESTER</h3>

<span>You can clone this project to test some functionnality of djangocms</span>
<br/>
<span>Example: Test a placehlder you want to add, a package, ...</span>
<br/><br/>
<span>[Page 1]</span>

<h4>A-SET YOUR ENV</h4>

```
python3 -m venv venv
```
```
source venv/bin/activate
```

<h4>B-INSTALL PACKAGES/MODULES</h4>

```
# update pip
pip install --upgrade pip
```
```
# install djangocms and all necessaries packages/modules

pip install -r requirements.txt
```
<h4>C- Create a new project</h4>

```
django-admin startproject project_tuto
```

```
tree -L 2
.
├── README.md
├── project_tuto
│   ├── manage.py
│   └── project_tuto
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── requirements.txt
└── venv

```

<h4>D- Create Database tables</h4>

```
# cd project_tuto

python manage.py migrate
```

```
# And you must see
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
...
...
Applying filer.0017_image__transparent... OK
Applying menus.0001_initial... OK
Applying sessions.0001_initial... OK
Applying sites.0002_alter_domain_unique... OK
```

<h4>E- Create Admin Super User</h4>

```
python manage.py createsuperuser
```

<h4>F-  check your configuration</h4>

```
python manage.py cms check
```

<h4>G-  RUN The Server</h4>

```
python manage.py runserver
```




