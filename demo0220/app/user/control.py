

def alreadyExist(append_user):
    def dec(*args, **kvarg):
        addItem = args[0]
        container = args[1]
        al = filter(lambda n: n["name"] == addItem["name"], container)
        existLen = len(list(al))
        if (bool(existLen)):
            raise Exception('The user already exists')
        print("check user", args, kvarg)
        return append_user(*args, **kvarg)
    return dec


@alreadyExist
def append_user(user: dict, container: list):
    """
    append user to list
    """
    item = None
    if len(container) > 0:
        ids = map(lambda n: n["id"], container)
        maxId = max(ids)
        item = dict(**user, id=maxId+1)
        container.append(item)
    else:
        item = dict(**user, id=1)
        container.append(item)
    return item


