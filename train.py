from pathlib import Path
import markovify


class MarkovTrainer:

    def __init__(self, name1, name2, corpora_dir):

        self.corpora_dir = corpora_dir
        self.corpus1 = self._get_corpus(name1)
        self.corpus2 = self._get_corpus(name2)

        self.model1 = None
        self.model2 = None

        self.combination = None

    def train(self, state_size=4):

        self.model1 = self._make_model(self.corpus1, state_size)
        self.model2 = self._make_model(self.corpus2, state_size)

        self.combination = markovify.combine([self.model1, self.model2], [3, 1])

    def sample(self, n=3, short=True):

        for i in range(n):
            if short:
                print(self.combination.make_short_sentence(280))
            else:
                print(self.combination.make_sentence())

    def _get_corpus(self, name):

        corpus_path = Path(f'{self.corpora_dir}{name}/{name}.txt')

        with open(corpus_path, 'rb') as f:
            text = f.read()
            return str(text)

    def _make_model(self, text, state_size):
        return markovify.Text(text, state_size)

