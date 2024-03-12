from .list_id_helper import get_list_id_map

class Card_Item:
    def __init__(self, id_short, long_id, name, description, status):
        self.id = id_short
        self.long_id = long_id
        self.name = name
        self.description = description 
        self.status = status

    @classmethod
    def from_trello_card(cls, card):
        return cls(card['idShort'],card['id'], card['name'], card['desc'], get_list_id_map()[card['idList']])
    