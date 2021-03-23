# Django Backend (Boilerplate)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A boilerplate built with Django, Postgres, Nginx, etc.


# .env
Before anything, you should make your own environment variables.
To do that firstly, run the command line below on your terminal:
```shell script
cat .env.EXAMPLE > .env
```
now its build a `.env` file fill the gaps based on your project.


# Code Style
We use black for our code-style!

It's already written in requirements you just need to run commandline below.
```shell script
black .
```


# Run via Docker Compose locally for Development
To run the project for development purpose run the commandline below:
```shell script
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```
You also can make a alias for this command.


# Deploy via Docker Swarm
To run the project with docker swarm, you need to initialize docker swarm and add some secrets, then deploy the project.

### Initialize docker swarm 
```shell script
docker swarm init
```
> [Docker Swarm Document](https://docs.docker.com/engine/reference/commandline/stack/)

### Add secret
```shell script
echo "YOUR_SECRET" | docker secret create secret-name -
```
> [Docker Secret Document](https://docs.docker.com/engine/reference/commandline/secret/)

> The secrets you need to add is listed here.

| Secret name       | Description
|--------------     |---------------
| db-name           | Name of the database
| db-user           | user of the database
| db-pass           | password of the database
| access-key        | storage's access key
| secret-key        | storage's secret key 
| nginx.crt         | The Nginx's certificate
| nginx.key         | The Nginx's private key
| dhparam.pem       | <TODO>

> Run the command line below to make nginx ssl
> ```shell script
> sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx.key -out nginx.crt
> sudo openssl dhparam -out dhparam.pem 2048
> ```
> [Make SSL certificate for Nginx](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-on-centos-7)

### Deploy Swarm
```shell script
docker stack deploy --orchestrator swarm -c docker-compose.yml -c docker-compose.swarm.yml <project_name>
```
> [Docker Stack Document](https://docs.docker.com/engine/reference/commandline/stack/)

### Manage your services
```shell script
docker service ls
```
> [Docker Service Document](https://docs.docker.com/engine/reference/commandline/service/)

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md).

Thanks to all the people who already contributed!

<a href="https://github.com/alireza8n/django-backend/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=alireza8n/django-backend" />
</a>
