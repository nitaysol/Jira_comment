import sys
from jira import JIRA
import getpass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\03	3[4m'

def check_input_parm ():
	if not (len(sys.argv) == 3):
		print "Wrong syntax - Please insert 2 parameters | 1-MAN-ticket 2-comment"
		exit(1)

def insert_auth():
	print "Please insert username & password"
	user_name = raw_input('User Name:')
	password = getpass.getpass('Password:')
	return user_name, password

def connect_jira_and_comment(man_ticket, comment, user_name, password):
	options = {
    'server': 'https://jira.com'
	}
	try:
		jira = JIRA(options, basic_auth=(user_name, password))
		jira.add_comment(man_ticket, comment)
	except:
		print bcolors.FAIL + 'Wrong info Username / Password / MAN-ticket'
		exit(1)


#checking that it got 2 parameters
check_input_parm()
#put the parameters on variables
man_ticket = sys.argv[1]
comment = sys.argv[2]
user_name, password = insert_auth()
connect_jira_and_comment(man_ticket, comment, user_name, password)
print bcolors.OKGREEN + "Comment added"