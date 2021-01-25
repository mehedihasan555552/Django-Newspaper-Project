from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import LatestPost



class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return LatestPost.objects.all().order_by("-date_posted")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('feed', args=[item.pk])
