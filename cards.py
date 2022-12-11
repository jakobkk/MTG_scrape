import constants

class Cards:
    _deck_name = ''
    _deck_attr = set()
    deck = {}
    def __init__(self,deck_name:str, deck_attr:set={constants.FOIL_ATTR, constants.PRERELEASE_ATTR}):
        self._deck_name = deck_name
        self._deck_attr = deck_attr
        return
    
    def print_val(self):
        print(self._deck_name)

    def add_cards(self, card_list, card_type):
        self.deck[card_type] = [card_list]
    
if __name__ == "__main__":
    bro = Cards('BRO')
    bro.print_val()