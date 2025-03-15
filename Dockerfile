FROM python:3.12  # Use the latest available Python version

WORKDIR /app

COPY . .

RUN apt update && apt install -y systemd

RUN pip install -r requirements.txt

CMD ["python", "brute_force.py"]
