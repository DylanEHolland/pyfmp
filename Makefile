activate:
	. env/bin/activate;

all:
	@-echo proper push-release 

clean: proper
	@-sh clean.sh;
	@-rm -rf env;

proper:
	@-rm -rf dist MANIFEST;

push-release: proper
	@-python setup.py sdist;
	@-twine upload dist/*;

setup: clean
	@-python3 -m venv env;
	@-. env/bin/activate && pip install -r requirements.txt;