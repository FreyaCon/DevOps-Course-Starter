from todo_app.helpers.view_class import ViewModel
from todo_app.helpers.item_class_helper import Card_Item

def test_view_model_done_property():
    # Arrange
    card = Card_Item(1, 123, "something to do", "something to do", "TO DO")
    card2 = Card_Item(2, 1234, "something to do aswell", "something to do", "DONE")
    model = ViewModel([card, card2])

    # Act
    done_items = model.done_items

    # Assert
    assert done_items == [card2]
    