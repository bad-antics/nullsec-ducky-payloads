FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -e .
ENTRYPOINT ["python","-m","nullsec_ducky_payloads"]
