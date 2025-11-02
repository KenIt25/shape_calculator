<h2>Name: Ituma Kenneth</h2>
<h2>Course Code: CSC 825</h2>
<h2>PG Application No: PG202452675150</h2>

---

# 🧮 Shape Calculator

A Python program that calculates the **areas of a rectangle and a circle**, integrating the **four core OOP concepts**.

---

## 🧩 What This Program Does
It lets you:

- Create shapes such as **Rectangle** and **Circle**
- Assign **colors** to each shape
- **Calculate** their areas using specific formulas
- Demonstrate **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism**

---

## 🧠 The 4 OOP Concepts (Explained Simply)

| **Concept** | **What It Means** | **Where You See It** |
|--------------|------------------|-----------------------|
| **Encapsulation** | Protect internal data | `_color`, `_PI`, `_length`, `_width`, and `_radius` are protected attributes |
| **Abstraction** | Hide complex details behind simple methods | `calculate_area()` and `get_color()` expose only essential behavior |
| **Inheritance** | Reuse attributes and methods from a parent class | `Rectangle` and `Circle` inherit from the abstract class `Shape` |
| **Polymorphism** | Same method, different implementation | `calculate_area()` works differently for each shape |

---

## 🧾 Code Explained Step by Step

### 1️⃣ Abstract Base Class – `Shape`
```python
import abc

class Shape(abc.ABC):
    """
    Abstract Base Class for all shapes. Enforces a common interface.
    """
    def __init__(self, color):
        # Encapsulation: Protect internal data
        self._color = color

    @abc.abstractmethod
    def calculate_area(self):
        """Must be implemented by any concrete shape."""
        pass

    # Encapsulation: Public method to safely expose data
    def get_color(self):
        return self._color

