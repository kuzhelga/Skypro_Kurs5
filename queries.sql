DROP TABLE IF EXISTS employers;

DROP TABLE IF EXISTS vacancies;

CREATE TABLE employers (
    company_id int PRIMARY KEY,
    company_name character varying(200) NOT NULL,
    company_url character varying(200),
    company_open_vacancies int,
    vacancies_url character varying(200)
    );

CREATE TABLE vacancies (
    vacancy_id int PRIMARY KEY,
    vacancy_name character varying(200) NOT NULL,
    company_id int REFERENCES employers(company_id),
    city character varying(100) NOT NULL,
    salary_from integer,
    salary_to integer,
    currency character varying(20) NOT NULL,
    vacancy_url character varying(200) NOT NULL
);
