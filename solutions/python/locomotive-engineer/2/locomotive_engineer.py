"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *list_wagons, = args
    return list_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # First 2 wagons have to be on the end of the return list
    # The missing_wagons list should be put after the 3th wagon
    first, second, third, *rest = each_wagons_id
    *fixed_list, = third, *missing_wagons, *rest, first, second
    return fixed_list


def add_missing_stops(routing_information, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *all_stops, = kwargs.values()
    routing_information['stops'] = all_stops
    return routing_information


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    for chave, valor in more_route_information.items():
        route[chave] = valor
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    *organized_list, = zip(*wagons_rows)
    return [[*row] for row in organized_list]