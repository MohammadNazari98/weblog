## Weblog
#### my first django project

##### it's a simple weblog project written in django (python)
###### to use this project please follow these steps:
1. create your virtualenv
2. change your source into the new virtualenv
3. run these following commands in order:
```
git clone https://github.com/red9bit/weblog.git && cd weblog/
pip install -r requirements.txt
touch weblog/local_settings.py
```
4. add these following variables into weblog/local_settings.py file:
```
  DB_NAME = 'YOUR DATABASE NAME'
  DB_USER = 'YOUR DATABASE USER'
  DB_PASSWORD = 'YOUR DATABASE PASSWORD'
```
