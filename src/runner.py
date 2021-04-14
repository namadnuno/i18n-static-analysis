from pathlib import Path
import json

from src.json_reader import get_translation_in_json
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
                    if not t.namespance + '.' + t.key in used_translations:
                        used_translations[t.namespance + '.' + t.key] = 1
                    used_translations[t.namespance + '.' + t.key] = used_translations[t.namespance + '.' + t.key] + 1

    translations = list(Path(config['translations_folder']).rglob("*.json"))
    translations_in_json = []
    for tf in translations:
        with open(tf, 'r') as translations_file:
            content = json.load(translations_file)
            translations_in_json += get_translation_in_json(content, tf.name.replace(".json", ""))
            with open(config['report_path'], 'w+') as f:
                for ut in used_translations:
                    if ut not in translations_in_json:
                        f.write(ut)
                        f.write("\n")

    print('done!')
