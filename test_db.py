"""
Automated nose test suite for the mongodb memo application.
"""
import sys

from flask_main import get_memos

# We need to be able to modify a mongo database to test this
# properly, so we create one and start it with our test user.

from pymongo import MongoClient
import secrets.admin_secrets
import secrets.test_secrets

MONGO_ADMIN_URL = "mongodb://{}:{}@{}:{}/admin".format(
    secrets.admin_secrets.admin_user,
    secrets.admin_secrets.admin_pw,
    secrets.admin_secrets.host, 
    secrets.admin_secrets.port)

MONGO_TESTER_URL = "mongodb://{}:{}@localhost:{}/{}".format(
    secrets.test_secrets.db_user,
    secrets.test_secrets.db_user_pw,
    secrets.admin_secrets.port, 
    secrets.test_secrets.db)

# Set up the test database with the administrator account
try: 
    dbadmin = MongoClient(MONGO_ADMIN_URL)
    admin = getattr(dbadmin, secrets.test_secrets.db)
    admin.add_user(secrets.test_secrets.db_user,
                password=secrets.test_secrets.db_user_pw)

except:
    print("Failure creating database")
    sys.exit(1)

# Get the test database running
dbtester = MongoClient(MONGO_TESTER_URL)
db = getattr(dbtester, secrets.test_secrets.db)
collection = db.dated



###
# Tests
###


# FIXME: These tests still, for some reason, use the client's database -
# despite the fact that db has been set to the tester database instead.
def test_empty():
    print("Contents: {}".format(get_memos()))
    assert not get_memos()





# Drop the testing database
try: 
    admin.remove_user(secrets.test_secrets.db_user)
    print("Dropped database users for {}".format(secrets.test_secrets.db))
    admin.command( {"dropDatabase": 1 } )
    print("Dropped database {}".format(secrets.test_secrets.db))
except Exception as err:
    print("Failed")
    print(err)
