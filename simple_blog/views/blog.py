from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from ..models.blog_record import BlogRecord
from ..services.blog_record import BlogRecordService
from ..forms import BlogCreateForm, BlogUpdateForm

@view_config(route_name='blog',
renderer='simple_blog:templates/view_blog.jinja2')
def blog_view(request):
	blog_id = int(request.matchdict.get('id',1))
	entry = BlogRecordService.by_id(blog_id, request)
	if not entry:
		return HTTPNotFound
	return {'entry': entry}

@view_config(route_name='blog_action', match_param='action=create',
renderer='simple_blog:templates/create_blog.jinja2')
def blog_create(request):
	entry = BlogRecord()
	form  = BlogCreateForm(request.POST)
	if request.method == 'POST' and form.validate():
		form.populate_obj(entry)
		request.dbsession.add(entry)
		return HTTPFound(location=request.route_url('home'))
	return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='blog_action', match_param='action=edit',
renderer='simple_blog:templates/edit_blog.jinja2')
def blog_edit(request):
	return{}
