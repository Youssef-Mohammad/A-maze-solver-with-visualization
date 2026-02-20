import pygame
import heapq
import sys

# --------------------
# Configuration
# --------------------
WIDTH = 600
ROWS = 20
TILE = WIDTH // ROWS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (100, 149, 237)
YELLOW = (255, 215, 0)
GRAY = (200, 200, 200)

# --------------------
# Maze Grid (0 = free, 1 = wall)
# --------------------
maze = [
    [0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0],
] * 4

start = (0, 0)
goal = (19, 19)

# --------------------
# Heuristic
# --------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# --------------------
# A* Algorithm as Generator
# --------------------
def astar_steps(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g = {start: 0}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        visited.add(current)
        yield current, visited, None

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            yield current, visited, path[::-1]
            return

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = current[0] + dx, current[1] + dy
            if 0 <= nr < ROWS and 0 <= nc < ROWS and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                temp_g = g[current] + 1
                if temp_g < g.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))

    yield None, visited, None  # Unreachable

# --------------------
# Draw Grid
# --------------------
def draw(win, grid, visited, path):
    win.fill(WHITE)

    for r in range(ROWS):
        for c in range(ROWS):
            color = WHITE
            if grid[r][c] == 1:
                color = BLACK
            pygame.draw.rect(win, color, (c*TILE, r*TILE, TILE, TILE))

    for r, c in visited:
        pygame.draw.rect(win, BLUE, (c*TILE, r*TILE, TILE, TILE))

    if path:
        for r, c in path:
            pygame.draw.rect(win, YELLOW, (c*TILE, r*TILE, TILE, TILE))

    pygame.draw.rect(win, GREEN, (start[1]*TILE, start[0]*TILE, TILE, TILE))
    pygame.draw.rect(win, RED, (goal[1]*TILE, goal[0]*TILE, TILE, TILE))

    for i in range(ROWS):
        pygame.draw.line(win, GRAY, (0, i*TILE), (WIDTH, i*TILE))
        pygame.draw.line(win, GRAY, (i*TILE, 0), (i*TILE, WIDTH))

    pygame.display.update()

# --------------------
# Main Loop
# --------------------
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Maze Solver - 2D Game View")

    clock = pygame.time.Clock()
    astar = astar_steps(maze, start, goal)
    visited = set()
    path = None

    running = True
    while running:
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        try:
            current, visited, path = next(astar)
        except StopIteration:
            pass

        draw(win, maze, visited, path)

    pygame.quit()

main()
