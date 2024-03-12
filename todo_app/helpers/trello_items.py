import os
import requests
from .item_class_helper import Card_Item

api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')

def get_items():
    """
    Fetches all saved items from the trello board.

    Returns:
        list: The list of saved items.
    """
    try:
        response = requests.get(url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/cards?key={api_key}&token={api_token}")
        response.raise_for_status()
        cards = response.json()
        to_do_items=[]
        for card in cards:
            item = Card_Item.from_trello_card(card)
            to_do_items.append(item)
        return to_do_items
    except Exception as e:
        print(f"Getting items failed: {e}")
        raise Exception


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title, description):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    try:
        requests.post(url = f"https://api.trello.com/1/cards?idList={os.getenv('TO_DO_LIST_ID')}&key={api_key}&token={api_token}&name={title}&desc={description}")
    except Exception as e:
        print(f"Adding new items failed: {e}")

def toggle_list(id):
    try:
        requests.put(url = f"https://api.trello.com/1/cards/{id}?idList={os.getenv('DONE_LIST_ID')}&key={api_key}&token={api_token}")
    except Exception as e:
        print(f"Updating list items failed: {e}")

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """


    return item
