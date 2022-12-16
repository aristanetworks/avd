from itertools import groupby as itergroupby


def groupby(list_of_dictionaries: list, key: str):
    """
    Group list of dictionaries by key
    """

    def getkey(dictionary: dict):
        return dictionary.get(key)

    sorted_list = sorted(list_of_dictionaries, key=getkey)
    return itergroupby(sorted_list, getkey)
