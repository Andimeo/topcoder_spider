domain = 'topcoder.com'
index_url = 'http://community.topcoder.com/'
class Login:
	login_url = 'http://community.topcoder.com/tc?module=Login'
	formdata = {'username':'Andimeo', 'password':'19885245201314'}
	formname = 'frmLogin'
	
match_list_url = 'http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=%d'
problem_list_url = 'http://community.topcoder.com/tc?module=ProblemArchive&sr=0&er=10000'
problem_content_path = 'problems'
problem_detail_url = 'http://community.topcoder.com/tc?module=ProblemDetail&rd=%s&pm=%s'
problem_solution_url = 'http://community.topcoder.com/stat?c=problem_solution&cr=%s&rd=%s&pm=%s'
code_path = 'codes'
