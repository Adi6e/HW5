FROM python:3.12

RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /sbin/nologin appuser

WORKDIR /app

COPY main.py ./

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "main.py"]