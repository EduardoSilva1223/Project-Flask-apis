APP = restapi


flake:
	@flake8 . --exclude venv/

compose:
	@docker compose build
	@docker compose up 

freeze:
	@pip freeze >> requirements.txt