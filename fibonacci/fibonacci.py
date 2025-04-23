# fibonacci.py

class Fibonacci:
    def __init__(self, n_terms: int):
        self.n_terms = n_terms
        self.sequence = self._generate_sequence()

    def _generate_sequence(self) -> list[int]:
        if self.n_terms == 1:
            return [0]
        seq = [0, 1]
        for _ in range(2, self.n_terms):
            seq.append(seq[-1] + seq[-2])
        return seq
