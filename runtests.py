import django, sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    USE_TZ=True,
    INSTALLED_APPS=('django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.admin',
                    'db')
)


django.setup()
from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)

failures = test_runner.run_tests(['db'])
if failures:
    sys.exit(failures)
