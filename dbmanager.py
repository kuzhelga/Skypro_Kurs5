import psycopg2


class DBManager:
    """Класс для работы с данными в БД"""
    def __init__(self, params, db_name):
        self.params = params
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        with psycopg2.connect(**self.params, database=self.db_name) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT company_name, company_open_vacancies FROM employers')
                data = cur.fetchall()
        conn.close()
        for row in data:
            print(row)

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, вакансии и зарплаты, ссылки на вакансию"""
        with psycopg2.connect(**self.params, database=self.db_name) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT vacancy_name, company_name, salary_from, salary_to, vacancy_url '
                    'FROM employers JOIN vacancies USING(company_id)'
                )
                data = cur.fetchall()
        conn.close()
        for row in data:
            print(row)

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        with psycopg2.connect(**self.params, database=self.db_name) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT ROUND((AVG(salary_from) + AVG(salary_to)) / 2) as avarage_salary FROM vacancies;'
                )
                data = cur.fetchall()
        conn.close()
        print(data)

    def get_vacancies_with_higher_salary(self):
        """Получает список вакансий, у которых зарплата выше средней по всем вакансиям"""
        with psycopg2.connect(**self.params, database=self.db_name) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT vacancy_name, salary_from, salary_to FROM vacancies '
                    'WHERE salary_from > (SELECT ROUND((AVG(salary_from) + AVG(salary_to)) / 2) as avarage_salary '
                    '                     FROM vacancies) '
                    'ORDER BY salary_from, salary_to DESC;'
                )
                data = cur.fetchall()
        conn.close()
        for row in data:
            print(row)

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся слова (keyword)"""
        with psycopg2.connect(**self.params, database=self.db_name) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT vacancy_name FROM vacancies '
                )
                data = cur.fetchall()
        conn.close()
        for row in data:
            if keyword in row[0]:
                print(row)
