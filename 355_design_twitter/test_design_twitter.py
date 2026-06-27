import unittest

from design_twitter import Solution


class TestTwitter(unittest.TestCase):
    def setUp(self):
        self.twitter = Solution()

    def test_example(self):
        self.twitter.postTweet(1, 5)
        self.assertEqual(self.twitter.getNewsFeed(1), [5])
        self.twitter.follow(1, 2)
        self.twitter.postTweet(2, 6)
        self.assertEqual(self.twitter.getNewsFeed(1), [6, 5])
        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [5])

    def test_empty_news_feed(self):
        self.assertEqual(self.twitter.getNewsFeed(1), [])

    def test_single_user_multiple_tweets(self):
        self.twitter.postTweet(1, 10)
        self.twitter.postTweet(1, 20)
        self.twitter.postTweet(1, 30)
        self.assertEqual(self.twitter.getNewsFeed(1), [30, 20, 10])

    def test_news_feed_limit_10(self):
        for i in range(15):
            self.twitter.postTweet(1, i)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(len(feed), 10)
        self.assertEqual(feed, [14, 13, 12, 11, 10, 9, 8, 7, 6, 5])

    def test_follow_then_get_feed(self):
        self.twitter.postTweet(2, 100)
        self.assertEqual(self.twitter.getNewsFeed(1), [])
        self.twitter.follow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [100])

    def test_unfollow_removes_tweets_from_feed(self):
        self.twitter.follow(1, 2)
        self.twitter.postTweet(2, 50)
        self.assertEqual(self.twitter.getNewsFeed(1), [50])
        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [])

    def test_unfollow_non_followed_user(self):
        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [])

    def test_follow_multiple_users(self):
        self.twitter.postTweet(2, 10)
        self.twitter.postTweet(3, 20)
        self.twitter.postTweet(4, 30)
        self.twitter.follow(1, 2)
        self.twitter.follow(1, 3)
        self.twitter.follow(1, 4)
        self.assertEqual(self.twitter.getNewsFeed(1), [30, 20, 10])

    def test_own_tweets_always_in_feed(self):
        self.twitter.postTweet(1, 5)
        self.assertEqual(self.twitter.getNewsFeed(1), [5])

    def test_merged_feed_ordering(self):
        self.twitter.postTweet(1, 1)
        self.twitter.postTweet(2, 2)
        self.twitter.postTweet(1, 3)
        self.twitter.postTweet(2, 4)
        self.twitter.follow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [4, 3, 2, 1])

    def test_feed_limit_across_multiple_users(self):
        self.twitter.follow(1, 2)
        for i in range(7):
            self.twitter.postTweet(1, i)
        for i in range(7, 14):
            self.twitter.postTweet(2, i)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(len(feed), 10)
        self.assertEqual(feed, [13, 12, 11, 10, 9, 8, 7, 6, 5, 4])

    def test_follow_self_no_duplicate(self):
        self.twitter.postTweet(1, 42)
        self.twitter.follow(1, 1)
        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [42])

    def test_post_after_follow(self):
        self.twitter.follow(1, 2)
        self.twitter.postTweet(2, 99)
        self.assertEqual(self.twitter.getNewsFeed(1), [99])

    def test_multiple_follow_unfollow_cycles(self):
        self.twitter.follow(1, 2)
        self.twitter.postTweet(2, 10)
        self.assertEqual(self.twitter.getNewsFeed(1), [10])
        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [])
        self.twitter.follow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [10])

    def test_independent_user_feeds(self):
        self.twitter.postTweet(1, 1)
        self.twitter.postTweet(2, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [1])
        self.assertEqual(self.twitter.getNewsFeed(2), [2])

    def test_tweet_id_zero(self):
        self.twitter.postTweet(1, 0)
        self.assertEqual(self.twitter.getNewsFeed(1), [0])

    def test_unfollow_self(self):
        self.twitter.postTweet(1, 5)
        self.twitter.unfollow(1, 1)
        self.assertEqual(self.twitter.getNewsFeed(1), [5])


if __name__ == "__main__":
    unittest.main()
