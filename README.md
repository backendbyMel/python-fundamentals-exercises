# **Python Fundamentals & System Architecture**
## Project Overview
This repository is a technical portfolio showcasing a deep mastery of Python fundamentals through the lens of production-quality software engineering. The exercises transition from basic syntax to modular system architecture, emphasizing code reuse, memory management, and logical cohesion.
## Technical Modules
1. Data Types & The Python Memory Model
Concepts: Dynamic typing, object identity vs. value equality, and shared references.
Core Logic: memory_audit.py, variables.py, data_types.py, strings.py, booleans.py, cast.py.
Engineering Highlight: The Memory Address Audit explores how the Python Virtual Machine (PVM) manages data. It specifically documents the "Ghost Update" phenomenon, where modifying a shared mutable object (like a list) impacts all variables pointing to that memory address.
2. Geometry & Math Utilities
Concepts: Procedural decomposition, constants, and arithmetic operator overloading.
Core Logic: areaCircle.py, areaRectangle.py, mathematicalOperation.py, operators.py.
Engineering Note: These tools demonstrate procedural decomposition, where complex tasks are factored into manageable, purposeful functions to maximize reuse and minimize redundancy.
3. System Logic & Validation
Concepts: Multiway branching, input sanitization, and fault-tolerant programming.
Core Logic: checkNumber.py, checkDataType.py, temperatureConverter.py, swapVariables.py.
Engineering Note: The temperatureConverter.py utilizes try/except blocks to handle invalid user input gracefully, ensuring the system remains stable and does not crash during execution.
4. Domain-Specific Mini-Applications
Application: studentgradingsystem.py.
Engineering Note: This module integrates multiple core types (lists, dictionaries, and conditional logic) to solve a real-world data processing problem, serving as a precursor to full-scale backend services.
