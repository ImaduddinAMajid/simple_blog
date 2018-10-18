from pyramid.view import view_config
from ..services.blog_record import BlogRecordService

@view_config(route_name='home',
             renderer='simple_blog:templates/index.jinja2')
def index_page(request):
    page = int(request.params.get('page', 1))
    paginator = BlogRecordService.get_paginator(request, page)
    return {'paginator': paginator}
