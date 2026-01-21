import os
import django
import sys
from pathlib import Path

# ensure project root is on sys.path so 'reservations' package can be imported
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reservations.settings')
django.setup()

from django.test import Client
c = Client()

try:
    r1 = c.get('/catalogue/artist/')
    print('INDEX', r1.status_code)

    r2 = c.get('/catalogue/artist/create')
    print('CREATE_GET', r2.status_code)

    r3 = c.post('/catalogue/artist/create', {'firstname': 'Test', 'lastname': 'User'})
    print('CREATE_POST', r3.status_code)

    rlist = c.get('/catalogue/artist/')
    html = rlist.content.decode('utf-8')
    # estimate rows by counting <tr> occurrences (simple heuristic)
    print('LIST_TR_COUNT', html.count('<tr'))

    rshow = c.get('/catalogue/artist/1')
    print('SHOW_1', rshow.status_code)

    # Test validation: empty fields
    r_bad = c.post('/catalogue/artist/create', {'firstname': '', 'lastname': ''})
    # POST with invalid data should return 200 and render form with errors (no redirect)
    print('CREATE_POST_EMPTY', r_bad.status_code)

except Exception as e:
    print('ERROR', repr(e))
    sys.exit(1)
