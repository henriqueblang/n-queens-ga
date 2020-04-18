import random

from modules import problem

class Chromossome:
    def __init__(self, board = None):
        # [random.randint(0, problem.N_QUEENS - 1) for _ in range(problem.N_QUEENS)]
        genes = board is None and random.sample([i for i in range(problem.N_QUEENS)], problem.N_QUEENS) or Chromossome.get_genotype(board)

        self.__genes = genes

    def get_genes(self):
        return self.__genes

    def set_genes(self, genes):
        self.__genes = genes

    def to_string(self):
        chr_str = "G = [" + ', '.join(map(str, self.__genes)) + "]"

        return chr_str

    @staticmethod
    def get_genotype(board):
        return [row for column in range(problem.N_QUEENS) for row in range(problem.N_QUEENS) if board[row][column]]

    @staticmethod
    def get_fenotype(genes):
        return [[genes[i] == j for i in range(problem.N_QUEENS)] for j in range(problem.N_QUEENS)]