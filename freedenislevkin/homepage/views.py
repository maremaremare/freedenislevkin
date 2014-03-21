from django.views.generic import TemplateView
from .models import Homepage
from content.models import News_post
from split import chop
# Create your views here.


class HomepageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context

        context = super(HomepageView, self).get_context_data(**kwargs)

        splitted_list = list(chop(3, News_post.objects.all(), truncate=True))

        context['big_list'] = splitted_list

        return context
