#Use an official Python runtime as a parent image

FROM python:3.11-slim

#Set the working directory in the container

WORKDIR /app

#Install poetry, we use poetry for robust dependency management.

RUN pip install poetry

#Copy only the dependency files to leverage Docker cache

COPY poetry.lock pyproject.toml /app/

#Install dependencies
# --no-root: do not install the project itself, only dependencies
# --no-dev: exclude development dependencies for a smaller production image

RUN poetry install --no-root --no-dev

#Copy the application code into the container

COPY ./backend/app /app/backend/app

#Expose the port the app runs on

EXPOSE 8000

#Command to run the application using uvicorn (lightning-fast ASGI server)

CMD ["poetry", "run", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

