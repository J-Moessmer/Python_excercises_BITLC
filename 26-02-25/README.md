<h1 align="center">Graphics & Random Simulations</h1>

<br>

This section focuses on more advanced `turtle` graphics using randomization and loops, as well as an introduction to GUI development with `tkinter`.

<br>

---

<br>

<h2 align="center">🎨 Project Directory</h2>

<br>

| Project | Description | Documentation |
| :--- | :--- | :--- |
| **01. Rotating Squares** | Generative art with expanding geometric patterns. | [View Details](./01_Rotating_Squares/README.md) |
| **02. Simple Editor** | A basic text editor prototype using `tkinter`. | [View Details](./02_Simple_Editor/README.md) |
| **03. Random Movement** | A "drunkard's walk" simulation with boundary logic. | [View Details](./03_Random_Movement/README.md) |

<br>

---

<br>

<h2 align="center">📊 Simulation Logic</h2>

<br>

<h3 align="center">Rotating Pattern Flow</h3>
<p align="center">
  The 01_ROTQUAD algorithm follows a strictly iterative path to generate its complex visuals.
</p>

```mermaid
graph TD
    A[Start] --> B[Loop: Count]
    B --> C[Set Random Color]
    C --> D[Draw Shape]
    D --> E[Rotate Heading]
    E --> B
```

<br>

<h3 align="center">Boundary Detection</h3>
<p align="center">
  The Random Movement simulation uses coordinate checking to keep the turtle within the defined arena.
</p>

```mermaid
graph LR
    A[X/Y Position] --> B{Out of Bounds?}
    B -- Yes --> C[Teleport to Center]
    B -- No --> D[Continue Move]
    C --> D
```
