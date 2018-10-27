import json


async def user_exists(pool, user):
    query = """
    select exists(select id from users where id = $1)
    """
    conn = await pool.acquire()

    try:
        id = user.get("id")
        result = await conn.fetchval(query, id)

    finally:
        await pool.release(conn)

    return result


async def insert_user(pool, user):
    query = """
    insert into users(id, first_name, last_name, username, is_active)
    values ($1, $2, $3, $4, $5)
    on conflict (id)
    do update set (first_name, last_name, username, is_active) = ($2, $3, $4, $5)
    """

    conn = await pool.acquire()

    try:
        id = user.get("id")
        first_name = user.get("first_name")
        last_name = user.get("last_name", "")
        username = user.get("username", "")
        is_active = True
        await conn.execute(query, id, first_name, last_name, username, is_active)

    finally:
        await pool.release(conn)


async def deactivate_user(pool, user):
    query = """
    update users
    set is_active = false
    where id=$1
    """

    conn = await pool.acquire()

    try:
        id = user.get("id")
        await conn.execute(query, id)

    finally:
        await pool.release(conn)


async def insert_text(pool, sender, text):
    query = """
    insert into history(sender, text)
    values ($1, $2)
    """

    conn = await pool.acquire()

    try:
        await conn.execute(query, json.dumps(sender), text)

    finally:
        await pool.release(conn)
