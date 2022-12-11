import constants


from BRO_cards import BRO, SET_NUMS

class Cards:
    _deck_name = ''
    _deck_attr = set()
    deck = {}
    set_nums = {}
    def __init__(self,deck_name:str, set_nums, deck_attr:set={constants.FOIL_ATTR, constants.PRERELEASE_ATTR}):
        self._deck_name = deck_name
        self._deck_attr = deck_attr
        self.set_nums = set_nums
        return
        
    def print_val(self):
        print(self._deck_name)

    def add_cards(self, card_dict):
        self.deck = card_dict
    
if __name__ == "__main__":
    bro = Cards('BRO',SET_NUMS)
    bro.add_cards(BRO)
