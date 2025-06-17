import json
from pathlib import Path


arquivo_pikachu_json = Path('pikachu.json').read_text()
arquivo_json = json.loads(arquivo_pikachu_json)


print(arquivo_json['abilities'][1]['ability']['name'])