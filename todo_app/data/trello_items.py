import os
import requests

api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('BOARD_ID') 

def get_items():
    """
    Fetches all saved items from the trello board.

    Returns:
        list: The list of saved items.
    """
    try:
        response = requests.get(url = f"https://api.trello.com/1/boards/{board_id}/cards?key={api_key}&token={api_token}")
        response.raise_for_status()
        cards = response.json()
        return cards
    except Exception as e:
        print(f"Getting items failed: {e}")
    


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
        requests.post(url = f"https://api.trello.com/1/cards?idList=65cb8e035ab1d39df3532134&key={api_key}&token={api_token}&name={title}&desc={description}")
    except Exception as e:
        print(f"Adding new items failed: {e}")


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item
