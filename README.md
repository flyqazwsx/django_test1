## 指令
- django-admin startproject todolist

- python manage.py runserver

- 新增 app

    - python manage.py startapp user
- settings.py[INSTALLED_APPS]

    - 'user.apps.UserConfig'
- 進行資料庫同步

python manage.py migrate
後台新增超級管理者

    - python manage.py createsuperuser
    - 127.0.0.1:8000/admin
- 語言跟時間變更(settings.py)

    - LANGUAGE_CODE = 'zh-Hant'
    - TIME_ZONE = 'Asia/Taipei'