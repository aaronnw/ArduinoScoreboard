class Team:
    def __init__(self, raw):
        self.id = raw['team']['id']
        self.name = raw['team']['name']
        self.nickname = raw['team']['nickname']
        self.abbreviation = raw['team']['abbreviation']
        self.displayName = raw['team']['displayName']
        self.location = raw['team']['location']
        if 'score' in raw:
            self.score = raw['score']
        else:
            self.score = 0