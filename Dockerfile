FROM python:3.9 as builder

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY todo_app /code/todo_app

CMD ["uvicorn", "todo_app.api:app", "--host", "0.0.0.0", "--port", "8000"]