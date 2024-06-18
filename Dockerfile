FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /backend/ /app/backend/

CMD ["uvicorn", "backend.app:main.app", "--reload"]