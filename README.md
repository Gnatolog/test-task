# test-task

## Реализация процесса интеграции сообщений
___
### Цель
Реализация полосы чтения –> загрузки сообщений с почты. Необходимо продумать 
гибкий функционал для импортирования в систему сообщений из “yandex.ru”, “gmail.com”, “mail.ru”.
___
### Задачи

    1. Реализация моделей:
Необходимо реализовать модели, работающие на PostgresSQL для хранения логина и пароля от почты и хранения информации о сообщениях, полученных с почты.
Минимальные поля для модели хранения сообщений:

        1) id
        2) Тема сообщения (наименование)
        3) Дата отправки
        4) Дата получения
        5) Описание или текст сообщения
        6) Поле для хранения списка прикреплённых файлов к письму

    2. Создание страницы списка сообщений:
Сверстайте страницу (дизайн не важен) для отображения списка (желательно в виде таблицы) сообщений. Помимо таблицы должен быть где-то наверху страницы реализован прогресс-бар, где будет сначала надпись “чтение сообщений” а затем “получение сообщений”.
    3. Логика процесса получения:
После внесения логина и пароля в БД необходимо зайти на страницу списка сообщений и должен начаться процесс их получения. Пока последнее добавленное будет искаться на почте, в прогресс-баре мы должны видеть, сколько писем проверено. Как только данное сообщение найдено, полоса загрузки должна начать