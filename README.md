# Automation-of-AVR
Configuration files for AVR systems connected to intelligent relays

"Commercian project. In developing"


[Information for test with fixture](https://is20-2019.susu.ru/pollakiyu/2021/05/31/perevod-stati-how-to-provide-test-fixtures-for-django-models-in-pytest/)

P.S.

for  info

add to Makefile:
```html
    # with save coding utf-8
    dampdata:
        python -Xutf8 manage.py dumpdata --exclude auth.permission --exclude contenttypes -o system_avr_db.json
    loaddata:
        python manage.py loaddata --exclude auth.permission --exclude contenttypes systen_avr_db.json
```
