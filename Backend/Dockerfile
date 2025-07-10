FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy dependency definition files from the root context
COPY pyproject.toml poetry.lock /app/

# Install dependencies, excluding development ones for a lean image
RUN poetry install --no-root --no-dev

# Copy the application code into the container
# The source path is relative to the build context (project root)
COPY ./Backend/App /app/App

# Command to run the application using uvicorn
CMD ["poetry", "run", "uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]
