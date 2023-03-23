run:
    @docker-compose down
	@docker-compose up

rebuild:
	@docker-compose build

logs:
	@docker-compose logs -f

black:
	black .