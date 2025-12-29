# 🤝 Contributing to PaisyUI

Thank you for your interest in contributing to PaisyUI! This guide will help you get started.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Poetry (for dependency management)
- Basic understanding of DaisyUI components
- Familiarity with BeautifulSoup4

### Setup Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bs-dasyui
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Run tests** (if available)
   ```bash
   poetry run pytest
   ```

---

## 📝 How to Contribute

### Reporting Issues

Before creating an issue:
- Check if the issue already exists
- Verify it's not a duplicate
- Provide a clear description and steps to reproduce

**Issue Template:**
- **Description**: What is the issue?
- **Expected Behavior**: What should happen?
- **Actual Behavior**: What actually happens?
- **Steps to Reproduce**: How can we reproduce this?
- **Environment**: Python version, OS, etc.

### Suggesting Features

Feature suggestions are welcome! Please include:
- **Use Case**: Why is this feature needed?
- **Proposed Solution**: How should it work?
- **Alternatives**: Other approaches considered?

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/my-new-component
   ```

3. **Make your changes**
   - Follow the code style
   - Add docstrings to new components
   - Update documentation if needed

4. **Test your changes**
   - Ensure existing functionality still works
   - Test your new component thoroughly

5. **Commit your changes**
   ```bash
   git commit -m "Add: New component description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/my-new-component
   ```

7. **Create a Pull Request**
   - Provide a clear description
   - Reference any related issues
   - Include examples of usage

---

## 🧩 Adding New Components

### Component Structure

All components should:
1. Inherit from `PUIComponentABC`
2. Define HTML structure in the docstring
3. Use `[[content]]` placeholder for children
4. Follow naming convention: `PUI{ComponentName}`

### Example: Creating a New Component

```python
from paisy_ui import PUIComponentABC
from paisy_ui.mixins import PUIVariantMixin, PUILayoutMixin

class PUINewComponent(PUIComponentABC, PUIVariantMixin, PUILayoutMixin):
    """
    <div class="new-component">
        <div class="new-component-header">[[content]]</div>
    </div>
    """
    
    _variant_prefix = "new-component"
    
    def __init__(self, *classes, title: str = None, **attributes):
        super().__init__(*classes, **attributes)
        if title:
            # Add title logic here
            pass
```

### Component Checklist

- [ ] Component follows naming convention
- [ ] HTML structure defined in docstring
- [ ] `[[content]]` placeholder used correctly
- [ ] Appropriate mixins added
- [ ] Docstrings added for public methods
- [ ] Component added to `__init__.py`
- [ ] Component added to `__all__` list
- [ ] README.md updated with component
- [ ] Example usage provided

---

## 📚 Code Style

### Python Style

- Follow PEP 8
- Use type hints where possible
- Keep functions focused and small
- Use descriptive variable names

### Component Style

- Use docstrings for HTML structure
- Keep `__init__` simple
- Use properties for variant methods
- Return `self` for method chaining

### Example

```python
class PUIExample(PUIComponentABC, PUIVariantMixin):
    """<div class="example">[[content]]</div>"""
    
    _variant_prefix = "example"
    
    @property
    def large(self):
        """Make component large."""
        self.css("example-lg")
        return self
```

---

## 🧪 Testing

### Testing Components

When adding a component, test:

1. **Basic Rendering**
   ```python
   component = PUINewComponent()["Test"]
   assert "Test" in str(component)
   ```

2. **Variant Properties**
   ```python
   component = PUINewComponent().primary
   assert "example-primary" in str(component)
   ```

3. **Attributes**
   ```python
   component = PUINewComponent(id="test")
   assert 'id="test"' in str(component)
   ```

### Running Tests

```bash
poetry run pytest
```

---

## 📖 Documentation

### Updating Documentation

When adding a component:

1. **Update README.md**
   - Add to Component Reference table
   - Mark implementation status

2. **Update API Reference** (`docs/api.md`)
   - Add component documentation
   - Include usage examples

3. **Update Advanced Usage** (`docs/advanced.md`) if applicable
   - Add patterns or examples

### Documentation Style

- Use clear, concise descriptions
- Include code examples
- Show both basic and advanced usage
- Link to related components

---

## 🎯 Priority Areas

We're especially looking for contributions in:

1. **Navigation Components**
   - Menu
   - Breadcrumbs
   - Pagination

2. **Form Validation**
   - Validation helpers
   - Error handling

3. **Examples**
   - Real-world use cases
   - Framework integrations
   - Common patterns

4. **Documentation**
   - More examples
   - Tutorials
   - Best practices

5. **Testing**
   - Test coverage
   - Test utilities
   - Integration tests

---

## 🔍 Review Process

1. **Automated Checks**
   - Code style validation
   - Basic tests

2. **Code Review**
   - Maintainers review PRs
   - Feedback provided within 48 hours

3. **Merge**
   - Approved PRs are merged
   - Contributors are credited

---

## 📞 Getting Help

- **Questions?** Open a discussion
- **Found a bug?** Open an issue
- **Need clarification?** Ask in issues

---

## 🙏 Thank You!

Your contributions make PaisyUI better for everyone. We appreciate your time and effort!

---

## 📋 Checklist for PRs

Before submitting, ensure:

- [ ] Code follows style guidelines
- [ ] Tests pass (if applicable)
- [ ] Documentation updated
- [ ] README.md updated
- [ ] Component added to exports
- [ ] Examples provided
- [ ] No breaking changes (or documented)

---

**Happy contributing! 🌻**

