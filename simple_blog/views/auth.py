from pyramid.view import view_config

@view_config(route_name='auth', match_param='action=in', renderer='string', method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string', method='POST')
def sign_in_out(request):
	return{}
