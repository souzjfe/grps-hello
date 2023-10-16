all: run_client run_server
run_client:
	poetry run python client.py

run_server:
	poetry run python service.py

build:
	poetry install
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. settings.proto

