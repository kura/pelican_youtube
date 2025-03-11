.PHONY: install uninstall build pypi clean

uv:
	@if ! which uv >/dev/null; then pip install uv; fi

install: uv
	uv pip install .

uninstall: uv
	uv pip uninstall -y pelican-youtube

build: uv
	uv build

pypi: build
	uv publish

clean: uv
	uvx pyclean . --debris
