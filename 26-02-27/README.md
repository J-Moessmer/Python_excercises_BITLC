<h1 align="center">GUI Applications</h1>

<br>

This section contains standalone GUI applications built using Python's `tkinter` library, focusing on layout management and event handling.

<br>

---

<br>

<h2 align="center">🖥️ Application Directory</h2>

<br>

| Project | Description | Documentation |
| :--- | :--- | :--- |
| **01. BITLC Calculator** | A fully functional dark-mode arithmetic calculator. | [View Details](./01_BITLC_Calculator/README.md) |

<br>

---

<br>

<h2 align="center">🧮 Calculator Interface</h2>
<p align="center">
  The calculator uses a 10-column grid to organize numerical and operator buttons.
</p>

```mermaid
graph LR
    A[Button Click] --> B{Type?}
    B -- Number --> C[Update display]
    B -- Operator --> C
    B -- Equals --> D[Evaluate expression]
    B -- Clear --> E[Reset display]
```
