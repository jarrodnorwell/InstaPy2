from .utility import Utility

class Follow:
    def __init__(self, utility: Utility):
        self.utility = utility

        self.min_comments = 10 # only follow if posts comments are >=
        self.max_comments = 1000 # only follow if posts comments are <=
        self.min_followers = 10 # only follow if postees follower count is >=
        self.max_followers = 1000 # only follow if postees follower count is <=

    def usernames(self, iterable: list[str] = []):
        """
        Follows users with the usernames in `iterable`

            Parameters
                iterable (list[str]): list of usernames of users to follow
        """

        total_usernames = len(iterable)
        followed_users = 0
        for index, username in enumerate(iterable=iterable):
            print(f"Following user with username: {username} at index: {index}")

            if self.utility.client.user_follow(user_id=self.utility.client.user_id_from_username(username=username)):
                followed_users += 1
        
        print(f"Followed {followed_users} out of {total_usernames} available usernames")