# Pythonning yengil versiyasidan foydalanamiz
FROM python:3.9-slim

# Ishchi katalogni yaratamiz
WORKDIR /app

# Kerakli fayllarni konteynerga nusxalaymiz
COPY requirements.txt requirements.txt
COPY app.py app.py

# Kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Ilova ishlaydigan portni ochamiz
EXPOSE 5000

# Ilovani ishga tushiramiz
CMD ["python", "app.py"]