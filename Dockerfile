FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]