import pandas as pd
import numpy as np

file_path = "sudoku.csv"
n_samples = 1

def load_sudoku_dataset(file_path, n_samples, seed=42):
    df = pd.read_csv(file_path)
    df = df.sample(n=n_samples, random_state = seed)
    return df[['puzzle', 'solution']]

def parse_sudoku(board_str):
    return np.array([int(c) for c in board_str]).reshape((9, 9))

def print_board(board):
    for i, row in enumerate(board):
        linha = []
        for num in row:
            if num != 0:
                linha.append(str(num))  #Converte número para string
            else:
                linha.append('.')  #Substitui zeros por '.'

        linha = ' '.join(linha)  #Junta tudo com espaço

        print(linha)
        if (i + 1) % 3 == 0 and i < 8:
            print('-' * 21)

def solve_sudoku(board):
    #Candidates serve como matriz para armazenar os numeros que não se repetem nas linhas/colunas e podem ser alocados para preencher.
    candidates = [
        [set(range(1, 10)) if board[i][j] == 0 else {board[i][j]}
         for j in range(9)]
        for i in range(9)
    ]
    
    def get_used_numbers(i, j): #Parametros da linha[i] e coluna[j].
        row_nums = set(board[i]) - {0} #Percorre a linha [i] para ver os repetidos e remove os 0 (celulas vazias)
        col_nums = set(board[r][j] for r in range(9)) - {0} #Percorre todas as linhas (r de 0 a 8) pegando a coluna j e remove os 0 s.
        box_i, box_j = (i // 3) * 3, (j // 3) * 3 #Descobre a célula superior esquerda do bloco 3x3 onde (i, j) está localizado.
        box_nums = set(board[r][c] for r in range(box_i, box_i + 3) for c in range(box_j, box_j + 3)) - {0} #Itera sobre todas as células dentro desse bloco e remove os 0 s.
        return row_nums | col_nums | box_nums #Retorna a união (|) dos três conjuntos, representando todos os números que não podem ser usados na célula (i, j).


    progress = True #Inicializa progress = True para entrar no loop de preenchimento do Sudoku.
    while progress:
        progress = False #O loop continua enquanto pelo menos uma célula for preenchida a cada iteração.
        for i in range(9):
            for j in range(9): #Percorre todas as 81 células do Sudoku.
                if board[i][j] == 0: #Se a célula estiver vazia (0), tenta preencher ela
                    candidates[i][j] -= get_used_numbers(i, j) #Removemos do conjunto de candidatos todos os números que já estão na linha, coluna ou bloco 3x3.
                    if len(candidates[i][j]) == 1: #Se restar apenas um candidato possível, sabe-se que essa célula só pode conter esse número.
                        board[i][j] = candidates[i][j].pop() #É preenchido a célula (board[i][j] = candidates[i][j].pop()) e 
                        progress = True #é marcado progress = True para indicar que foi feito progresso nesta iteração.
    return board #Retorna o tabuleiro modificado, agora (idealmente) resolvido.

def main():
    df = load_sudoku_dataset(file_path, n_samples)
    
    for index, row in df.iterrows():  #Itera sobre cada linha do DataFrame contendo os Sudokus.
            print(f"\nSudoku {index+1} - Inicial:")  #Exibe o número do Sudoku que está sendo processado.
            sudoku = parse_sudoku(row['puzzle'])  #Converte o Sudoku de string (81 caracteres) para uma matriz 9x9.
            print_board(sudoku)  #Imprime o tabuleiro formatado do Sudoku inicial.

            print("\nSolucionado:")  #Indica que a próxima saída mostrará a solução obtida pelo algoritmo.
            solved_sudoku = solve_sudoku(sudoku.copy())  #Chama a função para resolver o Sudoku (fazendo uma cópia para não alterar o original).
            print_board(solved_sudoku)  #Imprime o tabuleiro resolvido pelo algoritmo.

            expected_solution = parse_sudoku(row['solution'])  #Converte a solução oficial do Kaggle de string para matriz 9x9.
            print("\nSolução correta:")  #Indica que será exibida a solução oficial para comparação.
            print_board(expected_solution)  #Imprime a solução correta fornecida pelo dataset.

            if np.array_equal(solved_sudoku, expected_solution):  #Compara a solução gerada com a solução oficial do Kaggle.
                print("\nSolução encontrada corretamente!\n")  #Exibe uma mensagem de sucesso caso as matrizes sejam idênticas.
            else:  #Se a solução gerada não for idêntica à solução esperada:
                print("\nSolução incompleta ou incorreta!\n")  #Exibe uma mensagem indicando erro na solução gerada.


if __name__ == "__main__": #Chamada da função "Main" para o funcionamento do programa.
    main()