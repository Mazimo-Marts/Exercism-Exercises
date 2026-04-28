"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    
    new_dict = read_notes(items_to_add)

    for chave, valor in new_dict.items():
          if chave in current_cart:
                current_cart[chave] = valor + current_cart[chave]
          else:
                current_cart.setdefault(chave, valor)
             
    return current_cart
    
          
def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    dict_item = {}
    for item in notes:
        dict_item[item] = notes.count(item)

    return dict_item


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for receita, material in recipe_updates:
        ideas[receita] = material
        
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    
    aisle_mapping_copy = aisle_mapping.copy()
    
    for chave in aisle_mapping:
        if chave in cart:
            aux = aisle_mapping[chave]
            aux.insert(0, cart[chave])
            aisle_mapping_copy[chave] = aux
        else:
            del aisle_mapping_copy[chave]

    aisle_mapping_sorted = sort_entries(aisle_mapping_copy)
    return dict(reversed(aisle_mapping_sorted.items()))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    
    for item, quantidade in store_inventory.items():
        if item in fulfillment_cart.keys():
            store_inventory[item][0] = quantidade[0] - fulfillment_cart[item][0]
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = 'Out of Stock'

    return store_inventory