from itertools import permutations
from typing import List, Tuple

def calcular_pontuacao(ranking: Tuple[int], coeficientes: List[int]) -> int:
    """Calcula a pontuação de um aluno com base em seus rankings e coeficientes."""
    return sum(rank * coef for rank, coef in zip(ranking, coeficientes))

def pode_ter_empates(n: int, m: int, coeficientes: List[int]) -> bool:
    """
    Verifica se a função de ranking de Denis pode resultar em empates.
    
    Args:
        n: Número de concursos
        m: Número de alunos
        coeficientes: Lista de coeficientes para cada concurso
        
    Retorna:
        bool: True se empates são possíveis, False caso contrário
    """
    # Gera todos os rankings possíveis para um aluno (1 a m)
    rankings_possiveis = list(range(1, m + 1))
    
    # Gera todas as combinações possíveis de rankings para um aluno
    todas_pontuacoes_possiveis = set()
    todos_rankings = list(permutations(rankings_possiveis, n))
    
    # Calcula pontuações para todas as combinações possíveis
    for ranking in todos_rankings:
        pontuacao = calcular_pontuacao(ranking, coeficientes)
        # Se encontrarmos uma pontuação que já existe, há possibilidade de empate
        if pontuacao in todas_pontuacoes_possiveis:
            return True
        todas_pontuacoes_possiveis.add(pontuacao)
    
    return False

def processar_casos_de_teste():
    """Processa múltiplos casos de teste até EOF."""
    try:
        while True:
            # Lê N e M
            try:
                n, m = map(int, input().split())
            except ValueError:
                break
            
            # Lê coeficientes
            coeficientes = list(map(int, input().split()))
            
            # Verifica se empates são possíveis
            tem_empates = pode_ter_empates(n, m, coeficientes)
            
            # Imprime resultado
            if tem_empates:
                print("Try again later, Denis...")
            else:
                print("Lucky Denis!")
            
    except EOFError:
        pass

if __name__ == "__main__":
    processar_casos_de_teste()
