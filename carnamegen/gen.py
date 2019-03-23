from typing import Iterable
import markovify


class CarNameGen(markovify.Text):
    __slots__ = ('chain', 'state_size', 'retain_original', 'parsed_sentences')

    def __init__(self, text: Iterable[str], state_size=2, chain=None,
                 retain_original=True):
        super().__init__(
            None,
            state_size,
            chain,
            self.parse_sentences(text),
            retain_original
        )

    @staticmethod
    def parse_sentences(text):
        return list(map(list, text))

    def sentence_split(self, text: str):
        return text.split("\n")

    def sentence_join(self, sentences):
        return "\n".join(sentences)

    def word_split(self, sentence: str):
        return list(sentence)

    def word_join(self, words):
        return "".join(words)

    def test_sentence_input(self, sentence):
        return bool(sentence.strip())
