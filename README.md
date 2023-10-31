# Сервис управления рассылками

Это проект на основе Python Django, который предоставляет функциональность для управления рассылками. Ниже описаны основные задачи, которые были реализованы в данном проекте:

## Основные задачи:

1. Реализован CRUD-механизм для управления рассылками. Это означает, что вы можете добавлять, просматривать, изменять и удалять рассылки.
2. Реализован скрипт рассылки, который может быть запущен как из командной строки, так и по расписанию. Это позволяет автоматизировать процесс рассылки и обеспечить его выполнение в заданное время.
3. Добавлены настройки конфигурации для периодического запуска задачи через crontab. Это позволяет запускать рассылку автоматически в заданное время.
4. Расширена модель пользователя для регистрации по почте и верификации. Теперь пользователи могут зарегистрироваться и подтвердить свою почту для использования сервиса.
5. Добавлен интерфейс для входа, регистрации и подтверждения почтового ящика. Пользователи могут легко создать учетную запись и подтвердить свою почту для использования сервиса.
6. Реализовано ограничение доступа к рассылкам для разных пользователей. Каждый пользователь имеет доступ только к своим рассылкам и не может просматривать или изменять рассылки других пользователей.
7. Реализован интерфейс менеджера, который позволяет пользователям просматривать и управлять своими рассылками. Здесь они могут видеть список своих рассылок, просматривать информацию о каждой рассылке и вносить изменения при необходимости.
8. Создан блог для продвижения сервиса. Здесь пользователи могут читать статьи и новости о функциональности и преимуществах сервиса.

## Технологии

- Python
- Django
- PostgreSQL
- Redis
- Crontab

## Установка и запуск проекта

1. Установите Python и Django, если они не установлены.
2. Склонируйте данный репозиторий на локальную машину.
3. Перейдите в каталог проекта.
4. Создайте и активируйте виртуальное окружение.
5. Установите все зависимости, выполните pip install -r requirements.txt.
6. Создайте базу данных, выполните `python manage.py migrate`.
7. Создайте администратора, выполните `python manage.py csu`.
8. Запустите сервер разработки, выполните `python manage.py runserver`.
9. Перейдите в веб-браузере по адресу http://localhost:8000 и вы увидите главную страницу сервиса.

## Использование проекта

1. После запуска проекта вы сможете просматривать и управлять рассылками через интерфейс менеджера.
2. Чтобы создать новую рассылку, нажмите кнопку "Создать рассылку" и заполните необходимые поля.
3. Чтобы редактировать существующую рассылку, перейдите на страницу этой рассылки и нажмите кнопку "Изменить".
4. Чтобы удалить рассылку, перейдите на страницу этой рассылки и нажмите кнопку "Удалить".
5. Для запуска скрипта рассылки из командной строки, выполните `python manage.py start_mailing_list.py`.
6. Чтобы запустить скрипт рассылки по расписанию, настройте crontab на выполнение команды python manage.py start_mailing_list.py в нужное время.
7. Для запуска Crontab воспользуйтесь командой `python manage.py crontab add`

## Благодарности

Спасибо за использование нашего сервиса управления рассылками! Если у вас есть какие-либо вопросы или предложения, пожалуйста, свяжитесь с нами через блог или обратитесь к администратору.

Желаем успешной работы с нашим сервисом!

## Авторы

ISSAA09

## Связь с авторами

https://github.com/ISSAA09/