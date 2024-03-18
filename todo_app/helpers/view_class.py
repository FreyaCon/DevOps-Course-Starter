from todo_app.helpers.item_class_helper import Card_Item

class ViewModel:
    def __init__(self, items: list[Card_Item]):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        done_items =[]
        for item in self.items:
            if item.status == "Done":
                done_items.append(item)
        return done_items
    
    @property
    def to_do_items(self):
        to_do_items =[]
        for item in self.items:
            if item.status == "To do":
                to_do_items.append(item)
        return to_do_items