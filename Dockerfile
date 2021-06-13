FROM python:3
ADD . /app
WORKDIR /app

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/script.py"]