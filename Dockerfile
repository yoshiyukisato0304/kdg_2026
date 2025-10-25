FROM python:3.14-slim

WORKDIR /project

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "project.asgi:application", "--reload"]
