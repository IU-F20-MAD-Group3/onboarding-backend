dev:
	[ -f .env ] || { cp .env.dev .env; echo "DOCKER_USER=$$(id -u):$$(id -g)" >> .env; }
	[ -f docker-compose.override.yml ] || ln -sf docker-compose.dev.yml docker-compose.override.yml
	@echo Development environment is ready. You can now use docker-compose as usual
