up:
	docker-compose up --build -d

test: up
	docker-compose exec web python3 /app/manage.py test

migrate: up
	docker-compose exec web python3 /app/manage.py migrate
