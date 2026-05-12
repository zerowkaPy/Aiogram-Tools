# PostgreStorage for Aiogram
`PostgreStorage` is a PostgreSQL-based storage backend for aiogram.
By default, aiogram uses `MemoryStorage`, which stores the entire FSM state in RAM. This approach has several major drawbacks, such as data loss after a restart and the inability to share state across multiple bot instances.

`PostgreStorage` solves these issues by storing FSM data in a PostgreSQL database using the asynchronous PostgreSQL driver `asyncpg`.

To start using PostgreStorage in your project, follow these steps:

- Create a table in your database using this script:
```sql
CREATE TABLE IF NOT EXISTS public.states
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id bigint,
    key text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    userdata jsonb,
    CONSTRAINT states_pkey PRIMARY KEY (id),
    CONSTRAINT states_user_id_unique UNIQUE (user_id)
)
```

- Add the postgre_storage.py file to your project directory.
- Add a DATABASE_URL environment variable to your .env file. This variable must contain the connection URL for your PostgreSQL database.

Example format:
```.env
DATABASE_URL=postgres://myuser:mypassword@localhost:5432/mydatabase
```
- If the URL format is still unclear, refer to the official PostgreSQL documentation:
[PostgreSQL Documentation — Connection URIs](https://www.postgresql.org/docs/current/libpq-connect.html?utm_source=chatgpt.com#LIBPQ-CONNSTRING)

- Load the `DATABASE_URL` environment variable inside your `main.py` file
(for example, using the `dotenv` module).

You can also check the `example.py file`, which demonstrates the exact usage of `PostgreStorage`.
Simply follow the same setup in your own project.
