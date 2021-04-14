import json


def get_translation_in_json(content: dict, namespace):
    t_keys: list(str) = []
    for key in content.keys():
        if isinstance(content[key], dict):
            for ki in content[key]:
                t_keys.append(namespace + "." + key + "." + ki)
        else:
            t_keys.append(namespace + "." + key)

    return t_keys