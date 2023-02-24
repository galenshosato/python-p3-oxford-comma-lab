def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        short_list = " and ".join(items)
        return short_list
    else:
        last_item = items.pop()
        new_items = ", ".join(items)
        new_list = new_items + f", and {last_item}"
        return new_list
