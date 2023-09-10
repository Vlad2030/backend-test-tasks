FROM python:3.11-slim
COPY . /main-worker/
# COPY ../.env /main-worker
WORKDIR /main-worker
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r \
    requirements.txt
RUN pip install \
    'uvicorn[standard]'