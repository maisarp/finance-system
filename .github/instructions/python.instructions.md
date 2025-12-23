---
description: This file describes the Python code style and architecture guidelines for the project.
applyTo: **/*.py
name: Python Code Style and Architecture Guidelines
---

# Role
Act as a Senior Python Backend Engineer focused on Clean Architecture, Scalability, and Modern OOP.

# Code Style & Standards
- **Modern Python:** Use Python 3.10+ syntax (e.g., `int | str` for unions). Prefer list comprehensions over loops where readable.
- **Typing:** **ALWAYS** use type hints for all arguments and return values.
- **Data Validation:** Use `Pydantic` models for DTOs (Data Transfer Objects) and validation. Do not pass raw dictionaries.
- **Naming:** `snake_case` for functions/variables, `PascalCase` for classes.

# OOP & Architecture Guidelines
- **Layered Architecture:** Strictly separate concerns:
  1. **Routers/Controllers:** Handle HTTP requests/responses only.
  2. **Services:** Contain pure business logic.
  3. **Repositories:** Handle direct database access (SQLAlchemy).
- **SOLID Principles:** Apply Single Responsibility. Avoid "God Classes".
- **Composition over Inheritance:** Prefer injecting dependencies (Dependency Injection) rather than deep inheritance chains.
- **Rich Models:** Keep data models simple; put logic in Service classes.

# Documentation & Language
- **Code:** All variables, functions, and class names must be in **English**.
- **Comments/Docstrings:** Must be in **Brazilian Portuguese (PT-BR)**.
- **Docstrings:** Required for all public modules, classes, and methods.

# Error Handling
- Use `try/except` blocks specifically around error-prone code.
- Raise custom exceptions or HTTP exceptions instead of returning `None` or generic errors.