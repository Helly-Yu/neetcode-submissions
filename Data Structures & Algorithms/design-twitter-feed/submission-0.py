class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(list)  # userId -> list of (time, tweetId)
        self.following = collections.defaultdict(set) # userId -> set of followeeIds
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # get all the followees and its self
        user_ids = self.following[userId] | {userId}
        res = []
        max_heap = []

        for u_id in user_ids:
            if u_id in self.tweets:
                index = len(self.tweets[u_id]) - 1 # get the newest tweet
                time, tweet_id = self.tweets[u_id][index]
                heapq.heappush(max_heap, (-time, tweet_id, u_id, index-1))
        
        while max_heap and len(res)<10:
            time, tweet_id, u_id, next_index = heapq.heappop(max_heap)
            res.append(tweet_id)
            # 如果该用户还有更旧的推文，继续入堆
            if next_index >= 0:
                n_time, n_tweet_id = self.tweets[u_id][next_index]
                heapq.heappush(max_heap, (-n_time, n_tweet_id, u_id, next_index - 1))
        return res
  

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
