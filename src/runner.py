
from pathlib import Path

from src.translation_finder import find_translations_in_string, has_translations


def run(path, config: dict[str: str]):
    used_translations = {}
    result = list(Path(path).rglob("*.tsx"))

    for p in result:
        with open(p, 'r') as f:
            source_code = f.read()
            if (has_translations(source_code)):
                translations = find_translations_in_string(source_code, config['default_namespace'])
                for t in translations:
                    if not t.namespance+'.'+t.key in used_translations:
                        used_translations[t.namespance+'.'+t.key]=1
                    used_translations[t.namespance+'.'+t.key] = used_translations[t.namespance+'.'+t.key] +1

    with open(config['report_path'], 'w+') as f:
        for ut in used_translations:
            t = used_translations[ut]
            f.write(ut + ":" + str(t))
            f.write("\n")


    """
    TODO: Now i need to get all the translations available with the corresponding namespaces and search witch one
     of those are not in use
    """

    print('done!')



