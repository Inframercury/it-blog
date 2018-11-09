from django.test import TestCase
from .models import Post

# Create your tests here.

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        Post.objects.create(title='First Post', content="Some Content")
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'posts/post_list.html')