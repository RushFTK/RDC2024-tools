class Team():
    name = ''
    players = []

    def __init__(self, name, players):
        self.name = name
        self.players = players

    def add_player(self, player: object):
        player.pick_order = len(self.players) + 1
        self.players.append(player)
        return len(self.players)

    def find_player_by_id(self, playerID):
        for player in self.players:
            if player.uid == playerID:
                return player
        return None

    def find_player_by_name(self, playerName):
        for player in self.players:
            if player.name == playerName:
                return player
        return None

    # def add_player(self, uid: str | int, name: str, group: str) -> object:
    #     player = Player(uid, name, group, len(self.players) + 1)
    #     self.players.append(player)
    #     return len(self.players)

    def __repr__(self):
        return "{%s : %s}" % (self.name, self.players)


class Player():
    uid = -1
    name = ''
    group = ''
    pick_order = -1

    def __init__(self, uid: str | int, name: str, group: str, pick_order=-1):
        self.uid = uid
        self.name = name
        self.group = group
        self.pick_order = pick_order

    def __repr__(self):
        return "[{groups}]{name}({UID})".format(
            UID=self.uid,
            name=self.name,
            groups=self.group
        )
