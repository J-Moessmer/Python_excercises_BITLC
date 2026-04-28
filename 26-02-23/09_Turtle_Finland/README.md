# 09 - Turtle Finland

A graphical exercise using the `turtle` module to draw the national flag of Finland.

## 📝 Description
This script uses absolute positioning (`goto`) and fill colors to precisely render the blue cross on a white background, following the proportions of the Finnish flag.

## 📊 Drawing Steps
1. Draw white rectangular frame.
2. Fill background with white.
3. Draw blue horizontal stripe.
4. Draw blue vertical stripe.

## 💻 Code Snippet
```python
# Draw the blue horizontal stripe
myPen.color("#4169E1")
myPen.fillcolor("#4169E1")
myPen.begin_fill()
myPen.goto(180, -20)
myPen.goto(180, 20)
myPen.goto(-180, 20)
myPen.goto(-180, -20)
myPen.end_fill()
```
