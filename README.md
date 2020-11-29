# Onboarding App Backend

This is the backend part of the Onboarding app developed
for the MAD course at Innopolis University.

## Contributing

For running a development server for this project you
should either use the Makefile or run commands defined
in the Makefile manually.

### Using Makefile

Firstly, initialize development environment via the
following command:

```sh
make dev
```

Then, use `docker-compose` for starting and stopping
services.  
For example:

```sh
# To build and start
docker-compose up -d --build

# To stop and remove containers
docker-compose down

# Like previous but also deletes volumes (e.g. database)
docker-compose down -v
```

The webserver will be available at `localhost:8000`.

### Manually

Run the following commands (same as `make dev`):

```sh
cp .env.dev .env
echo "DOCKER_USER=$(id -u):$(id -g)" >> .env
ln -sf docker-compose.dev.yml docker-compose.override.yml
```

Then, you can use `docker-compose` for managing services
(see examples in the previous section).
