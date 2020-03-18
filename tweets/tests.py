from rest_framework.test import APITestCase
from rest_framework import status


class MainTestCase(APITestCase):
    def registration(self):
        data = {
            "username": "testuser",
            "first_name": "testuser",
            "last_name": "testuser",
            "email": "testuser@gmail.com",
            "password": "testusertestuser",
            "password_confirm": "testusertestuser"
        }
        response = self.client.post("/accounts/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_jwt_test(self):
        self.registration()
        data = {
            "username": "testuser",
            "password": "testusertestuser"
        }
        response = self.client.post("/token/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tweet(self):
        self.registration()

        res_token = self.client.post("/token/", {"username": "testuser", "password": "testusertestuser"}, format='json')
        self.assertEqual(res_token.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in res_token.data)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(res_token.data['access']))

        res_get_tweets = self.client.get("/api/v1/tweets/")
        self.assertEqual(res_get_tweets.status_code, status.HTTP_200_OK)

        res_post_tweets = self.client.post("/api/v1/tweets/", {"body": "first tweet"})
        self.assertEqual(res_post_tweets.status_code, status.HTTP_201_CREATED)

        res_fans = self.client.get("/api/v1/tweets/1/fans/")
        self.assertEqual(res_fans.status_code, status.HTTP_200_OK)

        res_like_tweet = self.client.post("/api/v1/tweets/1/like/")
        self.assertEqual(res_like_tweet.status_code, status.HTTP_200_OK)

        res_unlike_tweet = self.client.post("/api/v1/tweets/1/like/")
        self.assertEqual(res_unlike_tweet.status_code, status.HTTP_200_OK)
