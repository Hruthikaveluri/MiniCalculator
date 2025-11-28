FROM python:3.10-slim

WORKDIR /app

COPY . .

ENV PYTHONPATH="/app"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["coverage", "run", "-m", "pytest"]
