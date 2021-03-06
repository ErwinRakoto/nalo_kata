# Nalo : Ice Cream APP

### Purpose :
Automatic ice delivery  

### Configuration :
Automatic configuration :  

Go to source root of the application : ~/nalo  

run :  
``` source bin/prepare_dev.sh ```

If it fails :  
 - install python3 (and pip3)
 - run:
``` 
$ python3 -m virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

Then makemigrations to load database:  
``` 
$ python manage.py makemigrations
$ python manage.py migrate
```

Finally Start localMod :  

``` 
$ python manage.py runserver  
```

Fill the database : 
[LOAD DATA IN BASE](http://localhost:8000/cron/cron/init-ice_bowl/)  

### Tests 

```
$ python manage.py test  
```

# Annexes USE :
First :
[LOAD DATA IN BASE](http://localhost:8000/cron/cron/init-ice_bowl/)  

See :
[LIST ICE BOWLS](http://localhost:8000/api/v1/icebowl/list_bowl/)  

The user can make a command as follow. In Fact Front will return glace_id and asked ice scoop number

Example of URL to make a command :
http://localhost:8000/api/v1/icebowl/ice_command/?glace_id=2&nb_boule=1  
We can try to see the out of stock situation :
http://localhost:8000/api/v1/icebowl/ice_command/?glace_id=2&nb_boule=45 

Then the waiter can see the command 
EXAMPLE of URL to get an order command :
http://localhost:8000/api/v1/icebowl/list_command/?num_commande=####
Change the number #### with order_number

if you lost order_command just follow this link :
[All COMMANDS](http://localhost:8000/api/v1/icebowl/list_command/)  

