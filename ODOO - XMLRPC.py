import functools
import xmlrpc.client
HOST = input("Odoo IP Address (No port number): ")
PORT = int(input("Port number: "))
DB = input("Database: ")
USER = input("Username: ")
PASS = input("Password: ")
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Logged in as %s (uid:%d)" % (USER,uid));

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('openacademy.session','search_read', [], ['name','seats'])
for session in sessions:
    print("Session %s (%s seats)" % (session['name'], session['seats']))
# 3.create a new session
session_id = call('openacademy.session', 'create', {
    'name' : 'XMLRPC Test',
    'course_id' : 2,
    'seats' : 40,
    'duration': 10,
})
# 4. reads the new session
print("Created new session: ");
sessions = call('openacademy.session','search_read', [], ['name','seats'])
print("Session %s (%s seats)" % (sessions[len(sessions)-1]['name'], sessions[len(sessions)-1]['seats']))
