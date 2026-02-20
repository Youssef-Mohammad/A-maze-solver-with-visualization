# 🧭 A* Maze Solver with Visualization

A Python implementation of the **A\*** search algorithm to solve a 2D maze.
The project visualizes both the **search process** and the **final shortest path**
using an animated grid-based interface.

---

## 📌 Features

- Maze/grid representation with walls, start, and goal
- A* search algorithm with **Manhattan heuristic**
- Detects unreachable goals
- Console-based path output
- **Animated 2D visualization**
- Clean, modular Python code

---

## 🧠 Algorithm Overview

The A* algorithm evaluates nodes using:
f(n) = g(n) + h(n)


Where:
- `g(n)` is the cost from the start node to node `n`
- `h(n)` is the heuristic estimate from `n` to the goal
- `f(n)` is the total estimated cost

The heuristic used is **Manhattan Distance**, suitable for grid-based movement
without diagonals.

---

## 🗺️ Maze Representation

- `0` → Free cell  
- `1` → Wall  
- Start and goal are defined by coordinates

Movement is allowed in **four directions**:
up, down, left, right.

---

## 🎮 Visualization

- 🟦 Blue: explored nodes
- 🟨 Yellow: final shortest path
- 🟩 Green: start node
- 🟥 Red: goal node

### Demo
//![A* Demo](./Assets/Dem.gif)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Youssef-Mohammad/A-maze-solver-with-visualization.git
cd astar-maze-solver
