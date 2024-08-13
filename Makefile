APP = restapi


flake:
	@flake8 . --exclude venv/
	@pytest -v --disable-warnings

compose:
	@docker compose build
	@docker compose up 

freeze:
	@pip freeze >> requirements.txt
