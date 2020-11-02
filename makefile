
# Venv Helper ------------------------------------------------------------------

venv: clean-venv
	$(info * initializing venv)
	@python3 -m venv venv
	$(info * installing dev requirements)
	@./venv/bin/pip install -qU pip
	@./venv/bin/pip install -qr requirements-dev.txt