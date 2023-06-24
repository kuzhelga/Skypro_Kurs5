import psycopg2


def create_db(params: dict, db_name: str,) -> None:
    """Функция для создания новой БД"""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    try:
        cur = conn.cursor()
        cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
        cur.execute(f'CREATE DATABASE {db_name}')
    finally:
        conn.close()


def execute_sql(params, db_name, queries) -> None:
    """Создает таблицы в базе данных по скрипту в файле queries.sql."""
    with psycopg2.connect(**params, database=db_name) as conn:
        with conn.cursor() as cur:
            with open(queries, 'r') as file:
                sql_command = file.read()
            cur.execute(sql_command)
    conn.close()


def insert_data(params, db_name, employers, vacancies) -> None:
    """Добавляет данные в таблицы 'employers' и 'vacancies'."""
    with psycopg2.connect(**params, database=db_name) as conn:
        with conn.cursor() as cur:
            for emp in employers:
                cur.execute(
                    "INSERT INTO "
                    "employers (company_id, company_name, company_url, company_open_vacancies, vacancies_url) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (emp['company_id'], emp['company_name'], emp['company_url'],
                     emp['company_open_vacancies'], emp['vacancies_url'])
                )

            for vac in vacancies:
                cur.execute(
                    "INSERT INTO "
                    "vacancies (vacancy_id, vacancy_name, company_id, city, salary_from, salary_to, currency, vacancy_url) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (vac['vacancy_id'], vac['vacancy_name'], vac['company_id'], vac['city'],
                     vac['salary_from'], vac['salary_to'], vac['salary_currency'], vac['vacancy_url'])
                )
    conn.close()
