FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Bağımlılıklar (önbellek için koddan önce)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Eğitim betiğini kopyala ve modeli build sırasında eğit
COPY train.py .
RUN python train.py

# API kodu
COPY app.py .

RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# Üretim için Flask'ın geliştirme sunucusu yerine gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
