# Sudoku Solver com Heurísticas e Técnicas Algorítmicas

## Sobre o Projeto
Este projeto implementa um solucionador de Sudoku utilizando heurísticas inspiradas em estratégias humanas combinadas com técnicas algorítmicas. O objetivo é resolver tabuleiros de Sudoku de diferentes níveis de dificuldade de maneira eficiente.

## Tecnologias Utilizadas
- Linguagem: Python 3.12+
- Bibliotecas: `numpy`, `pandas`

## Metodologia

### Representação do Tabuleiro
O tabuleiro de Sudoku é representado por uma matriz 9x9, onde:
- Os números de 1 a 9 representam células preenchidas.
- O valor 0 indica células vazias.

### Aplicação de Heurísticas
São utilizadas as seguintes estratégias:
- **Naked Singles**: Quando uma célula tem apenas um candidato possível.
- **Hidden Singles**: Quando um número só pode aparecer em uma célula específica dentro de uma linha, coluna ou bloco 3x3.

### Aplicação Iterativa
As heurísticas são aplicadas iterativamente até que o tabuleiro esteja completo ou que nenhuma outra célula possa ser resolvida com essas regras.

### Busca (Backtracking)
Caso as heurísticas não sejam suficientes, um algoritmo de backtracking é utilizado para encontrar a solução correta.

## Resultados
- Testado com uma base de Sudokus do Kaggle.
- Sudokus fáceis e médios são resolvidos apenas com heurísticas.
- Sudokus difíceis exigem o uso de backtracking para garantir a solução.
- Tempo de execução médio: <1s para Sudokus intermediários.

## Estrutura do Projeto
```
├── sudoku.csv       # Base de dados do Kaggle contendo os puzzles e soluções
├── SUDOKU.PY        # Script Python que implementa o solucionador de Sudoku
└── README.md        # Documentação do projeto
```

## Como Executar
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/sudoku-solver.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd sudoku-solver
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Execute o solucionador:
   ```sh
   python SUDOKU.PY
   ```

## Testes
Para rodar os testes unitários, utilize:
```sh
pytest tests/
```

## Base de Dados
Este projeto utiliza a base de dados **Sudoku Dataset** disponível no Kaggle:
- Kaggle: [Sudoku Dataset](https://www.kaggle.com/datasets/rohanrao/sudoku/code)

