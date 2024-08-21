APP = restapi


flake:
	@flake8 . --exclude venv/
	@pytest -v --disable-warnings

compose:
	@docker compose build
	@docker compose up 

freeze:
	@pip freeze >> requirements.txt

railway:
	@ if [ -z "$$TOKEN_GIT" ]; then \
		echo "A API DO TOKEN NÃO FOI DEFINIDA"; \
		exit 1; \
	fi
	@railway api login --token $$TOKEN_GIT
	@railway link -p ab7747a8-1fe6-4a3c-bd0c-cdb74998818f
	@railway up
