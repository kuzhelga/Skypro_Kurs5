import requests


def get_employers(url, area):
    """Функция возвращает список работодателей у которых более 3 открытых вакансий"""
    employers = []

    for page in range(10):
        params = {'area': area, 'page': page, 'per_page': 100}
        response = requests.get(url, params).json()

        for employer in response['items']:
            if employer['open_vacancies'] > 3:
                employers.append({
                    'company_id': employer['id'],
                    'company_name': employer['name'],
                    'company_url': employer['alternate_url'],
                    'company_open_vacancies': employer['open_vacancies'],
                    'vacancies_url': employer['vacancies_url']
                })
    return employers


def get_vacancies(data):
    """Функция возвращает список вакансий по отдельному работодателю"""
    vacancies = []
    for employer in data:
        response = requests.get(employer['vacancies_url']).json()
        for company in response['items']:
            if company['salary'] is not None:
                vacancies.append({
                    'vacancy_id': company['id'],
                    'company_id': company['employer']['id'],
                    'vacancy_name': company['name'],
                    'city': company['area']['name'],
                    'salary_from': company['salary']['from'],
                    'salary_to': company['salary']['to'],
                    'salary_currency': company['salary']['currency'],
                    'vacancy_url': company['alternate_url']
                })
    return vacancies
