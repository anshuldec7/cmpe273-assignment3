# cmpe273-assignment3
##Steps for execution
 - Create Different Application servers (I have created three separate directories to create Separate Docker Images)
    -  cd /Users/\<username>/cmpe273-assignment3/server5001/
    -  docker build -t server1:latest .
    -  cd /Users/\<username>/cmpe273-assignment3/server5002/
    -  docker build -t server2:latest .
    -  cd /Users/\<username>/cmpe273-assignment3/server5003/
    -  docker build -t server3:latest .
 - Make separate path/directories for MySQL docker images
    -  mkdir /Users/\<username>/mysqlDocker1
    -  mkdir /Users/\<username>/mysqlDocker2
    -  mkdir /Users/\<username>/mysqlDocker3
 - Create/Run MySQL docker images fetched from the Docker Hub
    -  docker run --detach -p 3301:3306 --name=db1 --env="MYSQL_ROOT_PASSWORD=\<myapssword>" -v /Users/\<username>/mysqlDocker1:/var/lib/mysql mysql
    -  docker run --detach -p 3302:3306 --name=db2 --env="MYSQL_ROOT_PASSWORD=\<myapssword>" -v /Users/\<username>/mysqlDocker2:/var/lib/mysql mysql
    -  docker run --detach -p 3303:3306 --name=db3 --env="MYSQL_ROOT_PASSWORD=\<myapssword>" -v /Users/\<username>/mysqlDocker3:/var/lib/mysql mysql
 - Excecuting & Linking Application to the MySQL DB instances
    -  docker run -detach --name servertest1 --link db1:mysql -p 5001:5001  server1
    -  docker run -detach --name servertest2 --link db2:mysql -p 5002:5002  server2
    -  docker run -detach --name servertest3 --link db3:mysql -p 5003:5003  server3
 - Now the app servers are up and running execute httpclient.py to test the desired output.

localhost:5002
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 61, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5003
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 62, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5001
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 63, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5001
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 64, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5001
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 65, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5003
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 66, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5002
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 67, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5002
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 68, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5001
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 69, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

localhost:5002
/v1/expenses
{
  "category": "training", 
  "decision_date": "", 
  "description": "iPhone for training", 
  "email": "foo1@bar.com", 
  "estimated_costs": "6760", 
  "id": 70, 
  "link": "http://www.apple.com/shop/buy-ipad/ipad-pro", 
  "name": "Foo Bar", 
  "status": "Pending", 
  "submit_date": "09-08-2016"
}

