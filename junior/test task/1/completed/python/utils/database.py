DATABASE_LINK: str ="postgresql+asyncpg://{}:{}@{}:{}/{}"


def url(
        user: str,
        password: str,
        hostname: str,
        port: int = 5432,
        database: str = None,
) -> str:
    return DATABASE_LINK.format(user, password,
                                hostname, port, database)