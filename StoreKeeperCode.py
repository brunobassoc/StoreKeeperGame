from collections import deque
from typing import List

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def f(i: int, j: int) -> int:
            return i * n + j

        def check(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n and grid[i][j] != "#"

        def pairwise(iterable):
            "s -> (s0,s1), (s1,s2), (s2, s3), ..."
            a, b = iter(iterable), iter(iterable)
            next(b, None)
            return zip(a, b)

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        
        # Encontra as posições iniciais do jogador (S) e da caixa (B)
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "S":
                    si, sj = i, j
                elif c == "B":
                    bi, bj = i, j

# Inicializa a fila para BFS, a matriz de visitados e adiciona o estado inicial
        q = deque([(f(si, sj), f(bi, bj), 0)])
        vis = [[False] * (m * n) for _ in range(m * n)]
        vis[f(si, sj)][f(bi, bj)] = True

        while q:
            s, b, d = q.popleft()
            bi, bj = b // n, b % n
            if grid[bi][bj] == "T":
                return d  # Retorna o número de passos quando a caixa atinge o alvo
            si, sj = s // n, s % n
            
            # Explora os movimentos possíveis do jogador
            for a, b in pairwise(dirs):
                sx, sy = si + a, sj + b
                if not check(sx, sy):
                    continue
                if sx == bi and sy == bj:  # Se o jogador puder empurrar a caixa
                    bx, by = bi + a, bj + b
                    if not check(bx, by) or vis[f(sx, sy)][f(bx, by)]:
                        continue
                    vis[f(sx, sy)][f(bx, by)] = True
                    q.append((f(sx, sy), f(bx, by), d + 1))  # Empurra a caixa e incrementa os passos
                elif not vis[f(sx, sy)][f(bi, bj)]:  # Se o movimento do jogador não envolver empurrar a caixa
                    vis[f(sx, sy)][f(bi, bj)] = True
                    q.appendleft((f(sx, sy), f(bi, bj), d))  # Apenas move o jogador, mantendo o número de passos

        return -1  # Retorna -1 se o alvo não puder ser alcançado

# Exemplo de uso
grid = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "T", "#", "#", "T#", "#"],
    ["#", ".", ".", "B", ".", "#"],
    ["#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", "S", "#"],
    ["#", "#", "#", "#", "#", "#"]
]

sol = Solution()
print(sol.minPushBox(grid))  # Saída esperada: 3