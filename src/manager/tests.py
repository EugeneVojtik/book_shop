from django.contrib.auth.models import User
from django.db.models import Exists
from django.test import TestCase
from django.urls import reverse
from slugify import slugify

from manager.models import Book, Comment


class TestMyApp(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Test_name')
        self.user1 = User.objects.create_user('test_name2')


    def test_add_book(self):
        self.client.force_login(self.user)
        url = reverse('add_book')
        data = {
            'title': 'test_title',
            'description': 'test_description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302, msg='is not redirected')
        self.assertTrue(Book.objects.exists(), msg='book is not created')
        book = Book.objects.first()
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.description, data['description'])
        self.assertEqual(book.slug, slugify(data['title']))
        self.assertEqual(book.authors.first(), self.user)
        self.client.logout()
        data2 = {
            'title2': 'test_title',
            'description2': 'test_description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302, msg='is not redirected')
        self.assertEqual(Book.objects.count(), 1, msg='Second book have not been created')

    def test_update_book(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title='test_title43')
        self.book1.authors.add(self.user)
        self.book1.save()

        self.book2 = Book.objects.create(title='test_titler')
        self.assertEqual(Book.objects.count(), 2)

        data = {
            'title': 'test_title4444',
            'description': 'test_description44444'
        }
        url = reverse('update_book', kwargs=dict(slug=self.book1.slug))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'], msg='Book 1 is not refreshed')
        self.assertEqual(self.book1.description, data['description'], )
        self.assertEqual(self.book1.authors.first(), self.user)
        self.client.logout()

        url = reverse('update_book', kwargs=dict(slug=self.book2.slug))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.book2.refresh_from_db()
        self.assertNotEqual(self.book2.title, data['title'], msg='Its equal')

    def test_rate_book(self):
        self.book1 = Book.objects.create(title='test_title43')

        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title='test_title1')
        url = reverse('add_rate', kwargs=dict(slug=self.book1.slug, rate=3))
        self.client.get(url)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.rating,3)
        self.client.force_login(self.user1)
        url = reverse('add_rate', kwargs=dict(slug=self.book1.slug, rate=4))
        self.client.get(url)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.rating, 3.5, msg='Rating is not correct')

        self.book2 = Book.objects.create(title='test_book_2')
        self.book2.refresh_from_db()
        self.client.force_login(self.user)
        url = reverse('add_rate', kwargs=dict(slug=self.book2.slug, rate=2))
        self.client.get(url)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.rating, 2)
        self.client.force_login(self.user1)
        url = reverse('add_rate', kwargs=dict(slug=self.book2.slug, rate=5))
        self.client.get(url)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.rating, 3.5)

        # url = reverse('add_rate', kwargs=dict(slug=self.book2.slug, rate=3))
        # self.client.get(url)
        # self.book2.refresh_from_db()
        # self.assertEqual(self.book2.rating, 2.5)
    def test_delete_book(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title='test_title_1')
        self.book1.authors.add(self.user)
        self.book2 = Book.objects.create(title='test_title_2')
        self.book1.refresh_from_db()
        url = reverse('delete_book', kwargs=dict(slug=self.book1.slug))
        response = self.client.get(url)

        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.status_code, 302)

        url = reverse('delete_book', kwargs=dict(slug=self.book2.slug))
        response = self.client.get(url)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Exists(Book.objects.get(slug=self.book2.slug)))
        print(Book.objects.get(slug=self.book2.slug))

        self.book2.authors.add(self.user)

        url = reverse('delete_book', kwargs=dict(slug=self.book2.slug))
        response = self.client.get(url)
        self.assertEqual(Book.objects.count(), 0)
        print('book 2 has been successfully deleted')
        self.assertEqual(response.status_code, 302)

    def test_add_comment(self):
        self.book1 = Book.objects.create(title='test_title_1')
        self.client.force_login(self.user)
        url = reverse('add_comment', kwargs=dict(slug=self.book1.slug))
        data = {
            'text': "comment text comment text"
        }
        response = self.client.post(url, data)
        self.book1.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.first()
        self.assertEqual(comment.text, data['text'])
        self.assertEqual(Comment.objects.count(), 1)

    def test_book_detail(self):
        self.client.force_login(self.user)

        self.book1 = Book.objects.create(title='Test_title_1')
        self.book1.refresh_from_db()

        url = reverse('book_detail', kwargs=dict(slug=self.book1.slug))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_main_page(self):
        url = reverse('the-main-page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_comment_like(self):
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title='test_title_1')
        self.book1.refresh_from_db()
        url = reverse('add_comment', kwargs=dict(slug=self.book1.slug))
        data = {
            'text': "comment text comment text"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.first()
        comment.refresh_from_db()
        self.assertEqual(Comment.objects.count(), 1)
        self.book1.refresh_from_db()
        url = reverse('add_comment_like_location', kwargs=dict(id=comment.id, location='book_detail'))
        response = self.client.get(url)
        comment.refresh_from_db()
        self.assertEqual(comment.likes, 1)














