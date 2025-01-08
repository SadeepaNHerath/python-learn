# Advanced Python Testing Examples

This repository demonstrates comprehensive testing practices using pytest, including various testing approaches and modern testing techniques. The examples cover both traditional unit testing methods and AI-assisted testing strategies.

## 🚀 Features

- Fixture-based testing
- Mock object utilization
- Pytest marks for test organization
- Class-based test structures
- Function-based test patterns
- AI-generated test cases

## 📋 Prerequisites

```bash
python >= 3.8
pytest >= 7.0
pytest-mock >= 3.10
```

## 🛠️ Installation

1. Clone the repository:
```bash
https://github.com/SadeepaNHerath/python-learn.git
cd pytest
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
src venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📚 Project Structure

```
pytest-examples/
├── src/
│   └── __init__.py
│   └── my_functions.py
│   └── school.py
│   └── service.py
│   └── shape.py
├── tests/
│   └── __init__.py
│   └── test_circle.py
│   └── test_mark.py
│   └── test_my_functions.py
│   └── test_rectangle.py
│   └── test_school.py
│   └── test_service.py
│   └── test_square.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🧪 Testing Examples

### Fixtures

```python
# tests/fixtures/common_fixtures.py
import pytest

@pytest.fixture
def sample_data():
    return {
        "id": 1,
        "name": "Test Item"
    }
```

### Mocking

```python
# tests/unit/test_functions.py
def test_external_api_call(mocker):
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {"status": "success"}
    
    result = your_function()
    assert result["status"] == "success"
```

### Marks

```python
# tests/unit/test_features.py
import pytest

@pytest.mark.slow
def test_slow_operation():
    # Test code here
    pass

@pytest.mark.integration
def test_integrated_components():
    # Test code here
    pass
```

### Class-Based Testing

```python
# tests/unit/test_classes.py
class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()
    
    def test_addition(self):
        assert self.calculator.add(2, 2) == 4
    
    def test_subtraction(self):
        assert self.calculator.subtract(5, 3) == 2
```

### Function-Based Testing

```python
# tests/unit/test_functions.py
def test_string_manipulation():
    result = process_string("hello")
    assert result == "HELLO"

def test_error_handling():
    with pytest.raises(ValueError):
        process_invalid_input(None)
```

## 🤖 AI-Generated Tests

The `tests/ai_generated/` directory contains automatically generated test cases using AI tools. These tests complement manual testing efforts and help increase code coverage.

```python
# tests/ai_generated/test_auto_generated.py
def test_ai_generated_case_1():
    # AI-generated test scenario
    pass
```

## 🏃 Running Tests

Run all tests:
```bash
pytest
```

Run specific test categories:
```bash
pytest tests/unit  # Run unit tests only
pytest -m slow     # Run tests marked as 'slow'
pytest -v         # Verbose output
pytest -k "test_string"  # Run tests matching the name pattern
```

## 📊 Test Coverage

Generate coverage report:
```bash
pytest --cov=src tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Sadeepa Herath (@SadeepaNHerath)

## 🙏 Acknowledgments

- pytest documentation and community
- Python testing best practices
- AI testing tools and frameworks used in this project