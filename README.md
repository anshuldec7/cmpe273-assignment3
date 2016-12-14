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
