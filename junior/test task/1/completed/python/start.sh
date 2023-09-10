cores=$(expr $(nproc) + 1)

if [ -f .env ]; then
    source .env
else
    echo ".env file not fount"
    exit 1
fi

gunicorn app:app \
    --workers $cores \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind=$SERVER_HOST:$SERVER_PORT \
    --log-level $SERVER_LOG_LEVEL \
