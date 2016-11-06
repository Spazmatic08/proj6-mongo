# MongoDB tester secrets
#    A MongoDB instance (mongod process) can have several 'databases',
#    each of which has its own authorized users. Your application runs
#    with a particular user on a particular database. This one is for
#    the suite of nosetests used to test the application itself.
#
db = "testmemo"
db_user = "Test"
db_user_pw = "SirRunsalot"
