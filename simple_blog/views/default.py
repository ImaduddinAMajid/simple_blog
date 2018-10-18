from pyramid.view import view_config


@view_config(route_name='home',
             renderer='simple_blog:templates/index.jinja2')
def index_page(request):
    return {}
