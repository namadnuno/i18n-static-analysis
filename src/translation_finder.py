import re


class Translation():
    def __init__(self, namespace: str, key: str):
        self.key = key
        self.namespance = namespace


def translation_is_initialized(source_code: str) -> bool:
    r = re.findall(r'{\s?t\:?\s?,?\s?([a-zA-Z1-9]+)?\s?}\s?=\s?useTranslation\(\'?([a-zA-Z]+)?\'?\)', source_code)
    return len(r) > 0


def get_global_namespace(source_code: str) -> bool:
    return re.findall(r'useTranslation\(\'?([a-zA-Z]+)?\'?\)', source_code).pop()


def get_translations(source_code):
    return re.findall(r'{t\(\'([a-zA-Z\-\.\:]+)\'\)}', source_code)


def get_namespace_from_translation(translation_key: str, default_namespace):
    if len(translation_key.split('.')) == 1:
        return default_namespace
    return translation_key.split('.')[0]


def find_translations_in_string(source_code: str, default_namespace: str = '') -> list[Translation]:
    if not translation_is_initialized(source_code):
        raise Exception("The translations are not initialized, see: \n" + source_code)

    g_namespace = get_global_namespace(source_code)

    found = []

    for translation_key in get_translations(source_code):
        namespace = g_namespace
        key = translation_key
        if not namespace:
            namespace = get_namespace_from_translation(translation_key, default_namespace)
            key = translation_key.replace(namespace + '.', '')
        found.append(Translation(namespace, key))

    return found


def has_translations(source_code: str):
    return translation_is_initialized(source_code)