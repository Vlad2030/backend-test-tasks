cores=$(expr $(nproc) + 1)

gunicorn app:app \
    --workers $cores \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind=127.0.0.1:7777 \
    --log-level info \
