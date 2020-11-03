from time import sleep
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import *
from factory.django import DjangoModelFactory
from factory import SubFactory
from faker import Faker


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    username = Faker().word()
    is_staff = True
    is_superuser = True


class ChatFactory(DjangoModelFactory):
    class Meta:
        model = Chat
    
    name = Faker().word()


class MessageFactory(DjangoModelFactory):
    class Meta:
        model = Message
    
    text = Faker().text()
    from_user = SubFactory(UserFactory)
    chat = SubFactory(ChatFactory)



class AuthTestCase(TestCase):
    def setUp(self):
        # user = User(
        #     username="test",
        #     is_staff=True,
        #     is_superuser=True,
        # )
        
        # user.set_password("django123") 
        # user.save()
        user = UserFactory()


        chat = ChatFactory()
        chat.users.add(user)
        chat.save()

        self.user = user
        self.chat = chat

    #     self.driver = webdriver.Chrome()
        
    
    # def tearDown(self):
    #     self.driver.close()

    def test_authorization_success(self):
        self.assertIn(self.user, User.objects.all())
        self.client.force_login(user=self.user)
        # driver = self.driver
        # driver.get("localhost:8000/admin/")
        # username_input = driver.find_element_by_name("username")
        # username_input.send_keys(self.user.username)
        # password_input = driver.find_element_by_name("password")
        # password_input.send_keys("django123")
        # password_input.send_keys(Keys.RETURN)
        # sleep(5)
        # assert "Site administration" in driver.page_source

        response = self.client.get(reverse("all"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.chat.name)

class MessageTestCase(TestCase):
    
    def test_check_message_success(self):
        message = MessageFactory()
        user = message.from_user
        chat = message.chat

        self.client.force_login(user=user)

        response = self.client.get(reverse("chat", kwargs={"id": chat.id}))
        
        self.assertContains(response, chat.name)

        self.assertContains(response, message.text)


    