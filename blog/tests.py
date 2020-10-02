# Client is a dummy web browser for simulating GET and POST requests
from django.test import TestCase, Client
# Get a reference to the active user
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testuser',
        )

        # Sample blog post
        self.post = Post.objects.create(
            title = 'A good title',
            body = 'A nice content',
            author = self.user,
        )

    # test the blog post string representation
    def test_string_representation(self):
        post = Post(title ='A simple title')
        self.assertEqual(str(post), post.title)

    # Test the blog content
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'A nice content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A nice content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        # Ensure an incorrectpage return a 404
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
        
