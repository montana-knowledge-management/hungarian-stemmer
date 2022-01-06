from hunspell import Hunspell
from importlib_resources import files


class HungarianStemmer:
    def __init__(self):
        resource_path = str(files("hungarian_stemmer") / "resources" / "hu_HU")
        self.hunspell = Hunspell(resource_path, resource_path)

    def stem(self, word: str, *args, **kwargs):
        return self.hunspell.stem(word, *args, **kwargs)

    def spell(self, word: str, *args, **kwargs):
        return self.hunspell.spell(word, *args, **kwargs)

    def suggest(self, word: str, *args, **kwargs):
        return self.hunspell.suggest(word, *args, **kwargs)

    def suffix_suggest(self, word: str, *args, **kwargs):
        return self.hunspell.suffix_suggest(word, *args, **kwargs)

    def analyze(self, word: str, *args, **kwargs):
        return self.hunspell.analyze(word, *args, **kwargs)
