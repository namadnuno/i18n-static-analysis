import re


class Translation():
    def __init__(self, namespace: str, key: str):
        self.key = key
        self.namespance = namespace


def translation_is_initialized(source_code: str) -> bool:
    r = re.findall(r'{\s?t\s?}\s?=\s?useTranslation\(\'?([a-zA-Z]+)?\'?\)', source_code)
    return len(r) > 0


def get_global_namespace(source_code: str) -> bool:
    return re.findall(r'useTranslation\(\'?([a-zA-Z]+)?\'?\)', source_code).pop()


def get_translations(source_code):
    return re.findall(r'{t\(\'([a-zA-Z\-\.\:]+)\'\)}', source_code)


def find_translations_in_string(source_code: str) -> list[Translation]:
    if not translation_is_initialized(source_code):
        raise Exception("The translations are not initialized")

    g_namespace = get_global_namespace(source_code)

    found = []

    for translation_key in get_translations(source_code):
        found.append(Translation(g_namespace, translation_key))

    return found
