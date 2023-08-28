class Document:
    def __init__(self, body, title, id, subreddit, url, num_comments, author):
        self.body = str(body)
        self.title = title
        self.id = id
        self.subreddit = subreddit
        self.url = url
        self.num_comments = num_comments
        self.author = author

    def get_text(self):
        text = self.body.replace('\n', ' ')
        return text