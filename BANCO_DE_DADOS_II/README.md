# Build container 
```sh
docker build -t mysql-databe .

ou 

docker build -t name-container .
```

# Run Container

```sh
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_USER=leandro -e MYSQL_PASSWORD=1234 -t mysql-databe

ou 

docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_USER=MainUser -e MYSQL_PASSWORD=MainPassword name-container
```

docker exec -it id-container bash

# Stop Container 
```
docker stop id-container
```

# Remove Container 
```
docker rm id-container
```