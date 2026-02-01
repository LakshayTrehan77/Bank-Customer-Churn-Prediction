FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir requirements.txt

COPY . . 

EXPOSE 8501

CMD [ "streamlit" , "run" , "app.py" , "--server.address=0.0.0.0" , "--server.port=8501"]

