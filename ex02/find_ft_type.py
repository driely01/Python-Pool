def all_things_is_obj(object: any) -> int:
    whichtype = type(object)
    splited = ((str(whichtype).split(" "))[1].split("'"))[1].capitalize()
    if splited == "List" or splited == "Tuple" or splited == "Set" or splited == "Dict" or splited == "Str":
        print(splited, ": ", whichtype)
    else:
        print("Type not found")
    return 42