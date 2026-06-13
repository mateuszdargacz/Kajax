# Locale Files

Translation catalogs are generated with Django:

```bash
python manage.py makemessages -l pl -l en -l no -l sv -l da -l de
python manage.py compilemessages
```

Polish is the source content language. Other locales can be filled incrementally.
