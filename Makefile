.PHONY: clean
clean: 
	@rm -rf env/

.PHONY: install
install: 
	@echo "Create env/ directory"
	@mkdir -p env/
	@echo "Setup python virtual environment"
	@pyvenv env/
	@echo "Installing dependencies"
	@./env/bin/pip install -e .
	@echo "You can start the app by running make run command"

.PHONY: db
db:
	@echo "Create and Populate sample Database"
	@env/bin/initialize_simple_blog_db development.ini

.PHONY: run
run: 
	@echo "Starting the Application"
	@./env/bin/pserve --reload development.ini
