## Weblog
#### my first django project

it's a simple weblog project written in django (python)
to use this project please follow these steps:
- create your virtualenv
- change your source into the new virtualenv
- run these following commands in order:
```
git clone https://github.com/red9bit/weblog.git && cd weblog/
pip install -r requirements.txt
touch weblog/db_config.py
```
- add these following variables into weblog/db_config.py file:
```
  NAME = 'YOUR DATABASE NAME'
  USER = 'YOUR DATABASE USER'
  PASSWORD = 'YOUR DATABASE PASSWORD'
```
