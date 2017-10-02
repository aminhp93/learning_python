from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/posts/post_text.txt')
    # title = indexes.CharField(model_attr='title')
    # content = indexes.CharField(model_attr='content')
    # author = indexes.CharField(model_attr='user')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        # print(self.get_model(), 15)
        return self.get_model().objects.all()

