# SYLVA Development Guide

> *"The craft honors the sacred work."*

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Environment](#development-environment)
3. [Code Standards](#code-standards)
4. [Testing Procedures](#testing-procedures)
5. [Contributing Guidelines](#contributing-guidelines)
6. [Debugging & Troubleshooting](#debugging--troubleshooting)
7. [Performance Optimization](#performance-optimization)
8. [Security Considerations](#security-considerations)
9. [Deployment](#deployment)

## Getting Started

### Prerequisites

- **Python 3.8+** (3.9+ recommended)
- **pip** package manager
- **Git** for version control
- **Virtual environment** (recommended)

### Initial Setup

```bash
# Clone the repository
git clone https://github.com/your-org/sylva.git
cd sylva

# Create virtual environment
python -m venv sylva_env

# Activate virtual environment
# On Windows:
sylva_env\Scripts\activate
# On macOS/Linux:
source sylva_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python main.py --help
```

### Project Structure

```
sylva/
├── main.py                          # CLI entry point
├── config.py                        # Configuration management
├── requirements.txt                 # Python dependencies
├── README.md                       # User documentation
├── CHANGELOG.md                    # Version history
├── ROADMAP.md                      # Development roadmap
├── ARCHITECTURE.md                 # System architecture
├── DEVELOPMENT.md                  # This file
├── utils/                          # Core utilities
│   ├── __init__.py
│   ├── metaphor_engine.py          # Symbolic response generation
│   └── memory_log.py               # Interaction logging
├── data/                           # Data files
│   └── sample_metaphors.json       # Metaphor library
├── memory/                         # User data storage
│   └── user_log.json              # Interaction history
├── tests/                          # Test suite
│   ├── test_sylva.py              # Basic functionality tests
│   ├── test_sylva_diagnostics.py  # Diagnostic system tests
│   ├── test_comprehensive_sylva.py # Comprehensive tests
│   └── test_sylva_enhanced_diagnostics.py # Enhanced diagnostics
├── diagnostics/                    # Diagnostic tools
│   ├── enhanced_sylva_diagnostics.py
│   └── SYLVA_DIAGNOSTIC_ENHANCEMENTS.md
└── tools/                          # Development tools
```

## Development Environment

### IDE Configuration

#### VS Code Setup
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./sylva_env/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests/"],
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

#### PyCharm Setup
1. Open project in PyCharm
2. Set project interpreter to `sylva_env/bin/python`
3. Configure pytest as test runner
4. Enable code inspection and formatting

### Development Tools

#### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

#### Code Formatting
```bash
# Install formatting tools
pip install black isort

# Format code
black .
isort .

# Check formatting
black --check .
isort --check-only .
```

#### Linting
```bash
# Install linting tools
pip install flake8 pylint

# Run linting
flake8 .
pylint utils/ tests/ main.py config.py
```

## Code Standards

### Python Style Guide

#### General Principles
- Follow **PEP 8** style guidelines
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all classes and functions
- Use **descriptive variable names**
- Keep functions **small and focused**

#### Example Code Structure
```python
"""
SYLVA Metaphor Engine

Core symbolic response generation system with subsystem-based processing.
Maintains trauma-safe boundaries and symbolic integrity.
"""

from typing import Dict, List, Optional, Tuple
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class MetaphorEngine:
    """
    Symbolic response generation engine with subsystem routing.
    
    Routes emotional content to appropriate symbolic subsystems (MARROW/ROOT/AURA)
    and generates trauma-safe metaphorical responses.
    """
    
    def __init__(self, config_path: Optional[Path] = None) -> None:
        """
        Initialize the metaphor engine.
        
        Args:
            config_path: Optional path to custom configuration file
            
        Raises:
            FileNotFoundError: If metaphor data file cannot be found
            ValueError: If metaphor data is malformed
        """
        self.config_path = config_path or Path("data/sample_metaphors.json")
        self.metaphors = self._load_metaphor_data()
        self.subsystem_mapping = self._init_subsystem_mapping()
        
        logger.info("MetaphorEngine initialized successfully")
    
    def generate_response(self, user_input: str) -> Tuple[str, str]:
        """
        Generate symbolic response for user input.
        
        Args:
            user_input: User's emotional expression
            
        Returns:
            Tuple of (response_text, subsystem_used)
            
        Raises:
            ValueError: If user_input is empty or invalid
        """
        if not user_input or not user_input.strip():
            raise ValueError("User input cannot be empty")
        
        subsystem = self._detect_subsystem(user_input)
        metaphor = self._select_metaphor_for_subsystem(subsystem, user_input)
        response = self._construct_response(metaphor, subsystem)
        
        logger.debug(f"Generated response for subsystem: {subsystem}")
        return response, subsystem
```

### Symbolic Language Standards

#### Metaphor Definition Format
```python
METAPHOR_TEMPLATE = {
    "the_archetype_name": {
        "descriptions": [
            "Poetic description 1",
            "Poetic description 2"
        ],
        "responses": [
            "Symbolic response 1",
            "Symbolic response 2"
        ],
        "contexts": [
            "emotional_context_1",
            "emotional_context_2"
        ],
        "affective_tags": [
            "emotion_1",
            "emotion_2"
        ],
        "subsystem": "MARROW|ROOT|AURA"
    }
}
```

#### Safety Validation Standards
```python
class SafetyValidator:
    """Validates symbolic responses for trauma-safe boundaries."""
    
    FORBIDDEN_PATTERNS = [
        r"\b(you should|you need to|you must)\b",
        r"\b(call|contact|reach out)\b",
        r"\b(help|support|resources)\b",
        r"\b(better|improve|heal)\b"
    ]
    
    REQUIRED_PATTERNS = [
        r"\b(container|vessel|space|silence)\b",
        r"\b(hold|holds|holding|held)\b",
        r"\b(darkness|shadow|depth|ground)\b"
    ]
    
    def validate_response(self, response: str) -> bool:
        """
        Validate response for safety compliance.
        
        Args:
            response: Generated symbolic response
            
        Returns:
            True if response is safe, False otherwise
        """
        # Implementation details...
```

### Error Handling Standards

#### Exception Hierarchy
```python
class SYLVAError(Exception):
    """Base exception for SYLVA system."""
    pass


class MetaphorError(SYLVAError):
    """Exception for metaphor-related errors."""
    pass


class SafetyError(SYLVAError):
    """Exception for safety validation failures."""
    pass


class MemoryError(SYLVAError):
    """Exception for memory system errors."""
    pass
```

#### Error Handling Patterns
```python
def safe_operation(func):
    """Decorator for safe operation with proper error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            raise SYLVAError(f"Required file missing: {e}")
        except ValueError as e:
            logger.error(f"Invalid value: {e}")
            raise SYLVAError(f"Invalid input: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise SYLVAError(f"System error: {e}")
    return wrapper
```

## Testing Procedures

### Test Structure

#### Unit Tests
```python
"""
Test suite for SYLVA Metaphor Engine.

Tests core functionality, subsystem detection, and response generation.
"""

import pytest
from unittest.mock import Mock, patch
from utils.metaphor_engine import MetaphorEngine


class TestMetaphorEngine:
    """Test cases for MetaphorEngine class."""
    
    @pytest.fixture
    def engine(self):
        """Create MetaphorEngine instance for testing."""
        return MetaphorEngine()
    
    def test_initialization(self, engine):
        """Test MetaphorEngine initialization."""
        assert engine is not None
        assert hasattr(engine, 'metaphors')
        assert hasattr(engine, 'subsystem_mapping')
    
    def test_subsystem_detection_marrow(self, engine):
        """Test MARROW subsystem detection."""
        test_inputs = [
            "I feel ashamed and broken inside",
            "The trauma runs deep in my core",
            "I am numb and empty"
        ]
        
        for test_input in test_inputs:
            subsystem = engine._detect_subsystem(test_input)
            assert subsystem == "MARROW"
    
    def test_subsystem_detection_root(self, engine):
        """Test ROOT subsystem detection."""
        test_inputs = [
            "I feel scared and unsafe",
            "I need grounding and stability",
            "The world feels unstable"
        ]
        
        for test_input in test_inputs:
            subsystem = engine._detect_subsystem(test_input)
            assert subsystem == "ROOT"
    
    def test_subsystem_detection_aura(self, engine):
        """Test AURA subsystem detection."""
        test_inputs = [
            "I feel overwhelmed by everything",
            "My boundaries feel invaded",
            "I need protection from the world"
        ]
        
        for test_input in test_inputs:
            subsystem = engine._detect_subsystem(test_input)
            assert subsystem == "AURA"
    
    def test_response_generation(self, engine):
        """Test complete response generation."""
        user_input = "I feel overwhelmed"
        response, subsystem = engine.generate_response(user_input)
        
        assert isinstance(response, str)
        assert len(response) > 0
        assert subsystem in ["MARROW", "ROOT", "AURA"]
        assert "That's enough for now." in response or "We'll build from that ember." in response
    
    def test_invalid_input_handling(self, engine):
        """Test handling of invalid inputs."""
        with pytest.raises(ValueError):
            engine.generate_response("")
        
        with pytest.raises(ValueError):
            engine.generate_response("   ")
```

#### Integration Tests
```python
"""
Integration tests for SYLVA system components.

Tests interaction between metaphor engine, memory logger, and CLI interface.
"""

import pytest
import tempfile
import json
from pathlib import Path
from utils.metaphor_engine import MetaphorEngine
from utils.memory_log import MemoryLogger


class TestSYLVAIntegration:
    """Integration tests for SYLVA system."""
    
    @pytest.fixture
    def temp_memory_file(self):
        """Create temporary memory file for testing."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({"interactions": [], "subsystem_activity": {}}, f)
            return f.name
    
    def test_complete_interaction_flow(self, temp_memory_file):
        """Test complete interaction flow from input to memory storage."""
        engine = MetaphorEngine()
        logger = MemoryLogger(temp_memory_file)
        
        # Generate response
        user_input = "I feel lost and confused"
        response, subsystem = engine.generate_response(user_input)
        
        # Log interaction
        logger.log_interaction(user_input, response, subsystem)
        
        # Verify memory storage
        with open(temp_memory_file, 'r') as f:
            memory_data = json.load(f)
        
        assert len(memory_data["interactions"]) == 1
        assert memory_data["interactions"][0]["user_input"] == user_input
        assert memory_data["interactions"][0]["sylva_response"] == response
        assert memory_data["interactions"][0]["subsystem"] == subsystem
```

#### Performance Tests
```python
"""
Performance tests for SYLVA system.

Tests response time, memory usage, and scalability.
"""

import time
import psutil
import pytest
from utils.metaphor_engine import MetaphorEngine


class TestSYLVAPerformance:
    """Performance tests for SYLVA system."""
    
    @pytest.fixture
    def engine(self):
        """Create MetaphorEngine instance for performance testing."""
        return MetaphorEngine()
    
    def test_response_time(self, engine):
        """Test response generation time."""
        test_inputs = [
            "I feel overwhelmed",
            "I am deeply ashamed",
            "I need safety and grounding",
            "My boundaries feel violated",
            "I am lost in darkness"
        ]
        
        total_time = 0
        for test_input in test_inputs:
            start_time = time.time()
            response, subsystem = engine.generate_response(test_input)
            end_time = time.time()
            
            response_time = end_time - start_time
            total_time += response_time
            
            # Individual responses should be fast
            assert response_time < 0.1  # 100ms threshold
        
        # Average response time should be reasonable
        avg_time = total_time / len(test_inputs)
        assert avg_time < 0.05  # 50ms average threshold
    
    def test_memory_usage(self, engine):
        """Test memory usage during operation."""
        process = psutil.Process()
        initial_memory = process.memory_info().rss
        
        # Generate many responses
        for i in range(100):
            engine.generate_response(f"Test input {i}")
        
        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Memory increase should be reasonable
        assert memory_increase < 10 * 1024 * 1024  # 10MB threshold
```

### Running Tests

#### Basic Test Execution
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_sylva.py

# Run specific test class
pytest tests/test_sylva.py::TestMetaphorEngine

# Run specific test method
pytest tests/test_sylva.py::TestMetaphorEngine::test_subsystem_detection_marrow

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=utils --cov-report=html
```

#### Test Configuration
```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    performance: marks tests as performance tests
```

## Contributing Guidelines

### Development Workflow

#### 1. Feature Development
```bash
# Create feature branch
git checkout -b feature/enhanced-subsystem-detection

# Make changes
# ... edit files ...

# Run tests
pytest

# Format code
black .
isort .

# Commit changes
git add .
git commit -m "feat: enhance subsystem detection accuracy

- Improve keyword mapping for MARROW subsystem
- Add context-aware scoring algorithm
- Update test coverage for new functionality

Closes #123"
```

#### 2. Pull Request Process
1. **Fork** the repository
2. **Create** feature branch from `main`
3. **Implement** changes with tests
4. **Run** full test suite
5. **Update** documentation
6. **Submit** pull request with detailed description

#### 3. Commit Message Standards
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

**Examples:**
```
feat(engine): add adaptive metaphor selection

- Implement learning-based metaphor selection
- Add user preference tracking
- Update subsystem detection algorithm

Closes #456

fix(memory): resolve JSON serialization error

- Handle Unicode characters in user input
- Add proper error handling for malformed data
- Update memory validation logic

Fixes #789
```

### Code Review Standards

#### Review Checklist
- [ ] **Functionality**: Does the code work as intended?
- [ ] **Safety**: Are trauma-safe boundaries maintained?
- [ ] **Performance**: Are there performance implications?
- [ ] **Testing**: Are there adequate tests?
- [ ] **Documentation**: Is documentation updated?
- [ ] **Style**: Does code follow style guidelines?
- [ ] **Security**: Are there security considerations?

#### Review Process
1. **Automated Checks**: CI/CD pipeline runs tests and linting
2. **Peer Review**: At least one team member reviews
3. **Safety Review**: Special attention to symbolic integrity
4. **Integration Testing**: Verify system integration
5. **Documentation Review**: Ensure documentation is updated

## Debugging & Troubleshooting

### Common Issues

#### 1. Subsystem Detection Problems
```python
# Debug subsystem detection
def debug_subsystem_detection(text: str) -> Dict:
    """Debug subsystem detection for given text."""
    engine = MetaphorEngine()
    
    scores = {
        'MARROW': engine._calculate_marrow_score(text),
        'ROOT': engine._calculate_root_score(text),
        'AURA': engine._calculate_aura_score(text)
    }
    
    detected = max(scores, key=scores.get)
    
    return {
        'input': text,
        'scores': scores,
        'detected': detected,
        'keywords_found': engine._extract_keywords(text)
    }
```

#### 2. Memory System Issues
```python
# Debug memory logging
def debug_memory_system(memory_path: str) -> Dict:
    """Debug memory system issues."""
    try:
        with open(memory_path, 'r') as f:
            data = json.load(f)
        
        return {
            'file_exists': True,
            'file_size': Path(memory_path).stat().st_size,
            'interaction_count': len(data.get('interactions', [])),
            'subsystem_activity': data.get('subsystem_activity', {}),
            'last_interaction': data.get('interactions', [])[-1] if data.get('interactions') else None
        }
    except Exception as e:
        return {
            'file_exists': False,
            'error': str(e)
        }
```

#### 3. Performance Issues
```python
# Performance profiling
import cProfile
import pstats

def profile_metaphor_engine():
    """Profile metaphor engine performance."""
    profiler = cProfile.Profile()
    profiler.enable()
    
    engine = MetaphorEngine()
    for i in range(1000):
        engine.generate_response(f"Test input {i}")
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(20)
```

### Logging Configuration

#### Development Logging
```python
# logging_config.py
import logging

def setup_development_logging():
    """Setup logging for development environment."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('sylva_dev.log'),
            logging.StreamHandler()
        ]
    )
```

#### Production Logging
```python
def setup_production_logging():
    """Setup logging for production environment."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('sylva_prod.log'),
            logging.StreamHandler()
        ]
    )
```

## Performance Optimization

### Caching Strategies

#### Metaphor Caching
```python
from functools import lru_cache

class CachedMetaphorEngine(MetaphorEngine):
    """Metaphor engine with caching for performance optimization."""
    
    @lru_cache(maxsize=1000)
    def _detect_subsystem(self, text: str) -> str:
        """Cached subsystem detection."""
        return super()._detect_subsystem(text)
    
    @lru_cache(maxsize=500)
    def _select_metaphor_for_subsystem(self, subsystem: str, text: str) -> Dict:
        """Cached metaphor selection."""
        return super()._select_metaphor_for_subsystem(subsystem, text)
```

#### Memory Optimization
```python
class OptimizedMemoryLogger(MemoryLogger):
    """Memory logger with optimization for large datasets."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_interactions = 1000
        self.compression_enabled = True
    
    def _compress_old_interactions(self, data: Dict) -> Dict:
        """Compress old interactions to save memory."""
        if len(data.get('interactions', [])) > self.max_interactions:
            # Keep only recent interactions
            data['interactions'] = data['interactions'][-self.max_interactions:]
            
            # Update subsystem activity
            self._recalculate_subsystem_activity(data)
        
        return data
```

### Profiling Tools

#### Memory Profiling
```python
import tracemalloc

def profile_memory_usage():
    """Profile memory usage during operation."""
    tracemalloc.start()
    
    engine = MetaphorEngine()
    for i in range(100):
        engine.generate_response(f"Test input {i}")
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
    
    tracemalloc.stop()
```

## Security Considerations

### Input Validation

#### User Input Sanitization
```python
import re
from typing import Optional

class InputValidator:
    """Validates and sanitizes user input."""
    
    def __init__(self):
        self.max_length = 1000
        self.forbidden_patterns = [
            r'<script.*?>.*?</script>',
            r'javascript:',
            r'on\w+\s*=',
            r'<.*?>'
        ]
    
    def validate_input(self, user_input: str) -> Optional[str]:
        """Validate and sanitize user input."""
        if not user_input or not user_input.strip():
            return None
        
        if len(user_input) > self.max_length:
            return None
        
        # Remove potentially dangerous patterns
        sanitized = user_input
        for pattern in self.forbidden_patterns:
            sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
        
        return sanitized.strip()
```

### Data Protection

#### Encryption for Sensitive Data
```python
from cryptography.fernet import Fernet
import base64

class DataEncryption:
    """Handles encryption of sensitive user data."""
    
    def __init__(self, key: Optional[str] = None):
        if key:
            self.key = base64.urlsafe_b64encode(key.encode())
        else:
            self.key = Fernet.generate_key()
        
        self.cipher = Fernet(self.key)
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()
```

## Deployment

### Local Development Deployment

#### Development Server
```bash
# Run development server
python main.py

# Run with custom memory path
python main.py --memory /path/to/custom/memory.json

# Run in quiet mode
python main.py --quiet
```

#### Docker Development
```dockerfile
# Dockerfile.dev
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

### Production Deployment

#### Production Dockerfile
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 sylva
RUN chown -R sylva:sylva /app
USER sylva

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run application
CMD ["python", "main.py"]
```

#### Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  sylva:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./memory:/app/memory
      - ./data:/app/data
    environment:
      - SYLVA_ENV=production
      - SYLVA_LOG_LEVEL=INFO
    restart: unless-stopped
    
  sylva-test:
    build: .
    command: ["pytest"]
    volumes:
      - ./tests:/app/tests
      - ./utils:/app/utils
    environment:
      - SYLVA_ENV=testing
```

### CI/CD Pipeline

#### GitHub Actions
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov black isort flake8
    
    - name: Run linting
      run: |
        black --check .
        isort --check-only .
        flake8 .
    
    - name: Run tests
      run: |
        pytest --cov=utils --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v1
      with:
        file: ./coverage.xml
```

---

## Development Resources

### Documentation
- [SYLVA README](README.md) - User documentation
- [SYLVA Architecture](ARCHITECTURE.md) - System architecture
- [SYLVA Roadmap](ROADMAP.md) - Development roadmap
- [SYLVA Changelog](CHANGELOG.md) - Version history

### External Resources
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Type Hints (PEP 484)](https://www.python.org/dev/peps/pep-0484/)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Code Formatter](https://black.readthedocs.io/)

### Community
- **Discussions**: GitHub Discussions for questions and ideas
- **Issues**: GitHub Issues for bug reports and feature requests
- **Contributions**: Pull requests welcome for improvements

---

*"The craft serves the sacred work."* - SYLVA 