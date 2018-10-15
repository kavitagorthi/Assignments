from django.contrib.syndication.views import Feed
from django.contrib.comments import Comment
from django.core.urlresolvers import reverse


class DreamrealCommentsFeed(Feed):
    title = "Dreamreal's comments"
    link = "/drcomments/"
    description = "Updates on new comments on Dreamreal entry."

    def items(self):
        return Comment.objects.all().order_by("-submit_date")[:5]

    def item_title(self, item):
        return item.user_name

    def item_description(self, item):
        return item.comment

    def item_link(self, item):
        return reverse('comment', kwargs={'object_pk': item.pk})