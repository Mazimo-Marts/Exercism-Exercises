"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    dict = {}
    count = 0
    for item in items:
        count = items.count(item)
        dict[item] = count
    return dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    dict = create_inventory(items)
    novo_inventario = inventory.copy()
    for chave, valor in dict.items():
        if chave in inventory:
            novo_inventario[chave] += valor
        else:
            novo_inventario[chave] = valor
    return novo_inventario


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    dict = create_inventory(items)
    novo_inventario = inventory.copy()
    for chave, valor in inventory.items():
        if chave in dict:
            novo_inventario[chave] = valor - dict[chave]
        if novo_inventario[chave] < 0:
            novo_inventario[chave] = 0
        
    return novo_inventario
            


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, "Inexistente")
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    result = []
    for chave, valor in inventory.items():
        if valor > 0:
            result.append((chave, valor))
    return result

