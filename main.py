from dbmanager import DBManager
from dbase import *
from employers import *
from configpars import *


def main():
    url = 'https://api.hh.ru/employers'
    db_name = 'head_hunter'
    queries = 'queries.sql'
    params = config()
    print('Ожидайте создания базы вакансий...')
    employers = get_employers(url)  # получение списка компаний
    vacancies = get_vacancies(employers)  # получение списка вакансий по компаниям

    create_db(params, db_name)  # создание базы данных
    execute_sql(params, db_name, queries)  # создание таблиц в базе данных
    insert_data(params, db_name, employers, vacancies)  # добавление данных в таблицы

    db = DBManager(params, db_name)
    print('База данных вакансий с сайта Head Hunter создана. Выберите опцию:')

    while True:
        command = input(
            "1 - Показать все компании и количество вакансий у каждой компании\n"
            "2 - Показать все вакансии (название комп, вакансии, ЗП, ссылки на вакансию)\n"
            "3 - Показать среднюю зарплату по вакансиям\n"
            "4 - Показать все вакансии, у которых зарплата выше средней\n"
            "5 - Показать все вакансии, в названии которого содержится переданное слово\n"
            "q - Выход \n"
        )

        if command.lower() == 'q' or 'й':
            break
        elif command == '1':
            db.get_companies_and_vacancies_count()
        elif command == '2':
            db.get_all_vacancies()
        elif command == '3':
            db.get_avg_salary()
        elif command == '4':
            db.get_vacancies_with_higher_salary()
        elif command == '5':
            keyword = input('Введите слово для поиска: \n')
            db.get_vacancies_with_keyword(keyword)


if __name__ == '__main__':
    main()
