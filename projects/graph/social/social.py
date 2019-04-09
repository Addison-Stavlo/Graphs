import random
import queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'User{i}')
        # Create friendships
        friendships = []
        for user in self.users:
            # friendship is a 2-way connection, avoid duplicates this way
            for friend in range(user + 1, self.lastID + 1):
                friendships.append((user, friend))
        random.shuffle(friendships)

        # add the randomized friendships, divide by 2 since friendship is 2-ways
        for i in range(numUsers * avgFriendships // 2):
            friendship = friendships[i]
            self.addFriendship(friendship[0],friendship[1])

    def populateGraph_On(self, numUsers, avgFriendships):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
                # Add users
        for i in range(numUsers):
            self.addUser(f'User{i}')
        # Create friendships
        # friendships = []
        i = 0
        while i <= numUsers*avgFriendships // 2:
            user = random.randint(1,numUsers)
            friend = random.randint(1,numUsers)
            if self.addFriendship(user, friend):
                i += 1
        # the above O(n) implementation will break down
        # as avgFrienships approaches numUsers
        # addFriendship will fail very often creating
        # an almost endless loop of addFriendship

    def bf_search(self, starting_vertex, target_vertex):
        # Create and empty queue
        q = queue.Queue()
        q.put([starting_vertex])
        visited = set()
        while q.qsize() > 0:
            path = q.get()
            v = path[len(path)-1]
            if v not in visited:
                visited.add(v)
                if v == target_vertex:
                    return path
                for verts in self.friendships[v]:
                    new_path = path[:]
                    new_path.append(verts)
                    q.put(new_path)
        return []

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.users:
            path_to_friend = self.bf_search(userID, user)
            if len(path_to_friend) > 0:
                visited[user] = path_to_friend

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

# 1. To create 100 users with an average of 10 friends each,
#  how many times would you need to call `addFriendship()`? Why?
#  - 50 times, b/c friendships are a 2-way link

#  2. If you create 1000 users with an average of 5 random friends
#   each, what percentage of other users will be in a particular 
#   user's extended social network? What is the average degree of 
#   separation between a user and those in his/her extended network?
#  - 99% of users will be in each others extended network
#  - with an average of 5 levels of separation
