# 07 - Circle

A class-based approach to geometric calculations for circles.

## 📝 Description
This exercise demonstrates how to perform calculations (Circumference and Area) directly within the `__init__` method and store them as attributes.

## 📊 Calculation Logic
- **Circumference**: $Radius \times 2 \times 3.14$
- **Area**: $3.14 \times Radius^2$

## 💻 Code Snippet
```python
class circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.circumference = radius*2*3.14
        self.area = 3.14*radius**2
```
