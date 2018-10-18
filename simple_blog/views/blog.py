from pyramid.view import view_config

@view_config(route_name='blog',
renderer='simple_blog:templates/view_blog.jinja2')
def blog_view(request):
	return{}

@view_config(route_name='blog_action', match_param='action=create',
renderer='simple_blog:templates/create_blog.jinja2')
def blog_create(request):
	return{}

@view_config(route_name='blog_action', match_param='action=edit',
renderer='simple_blog:templates/edit_blog.jinja2')
def blog_edit(request):
	return{}
