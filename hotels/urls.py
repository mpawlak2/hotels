from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import show_form

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='hotels/index.html')),
    url(r'^form/$', show_form),
]
