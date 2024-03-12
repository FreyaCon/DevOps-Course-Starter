import os

def get_list_id_map():
    list_id_to_do = os.getenv('TO_DO_LIST_ID') 
    list_id_done = os.getenv('DONE_LIST_ID')

    LIST_ID ={
        list_id_to_do: "To do",
        list_id_done: "Done"
    }
    return LIST_ID