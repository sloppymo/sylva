# SYLVA Module Guide

> *"Each component serves the sacred whole."*

## Overview

This guide provides detailed documentation for each module in the SYLVA symbolic emotional wellness system. Each module serves a specific purpose in maintaining the trauma-safe, symbolic interaction framework.

## Core Modules

### 1. Main Interface (`main.py`)

**Purpose**: Primary CLI interface and entry point for SYLVA interactions.

**Key Components**:
- `main()`: Primary CLI application using Typer
- `print_welcome()`: Displays symbolic welcome message
- `print_help()`: Shows comprehensive help information
- `print_farewell()`: Displays symbolic farewell message
- `handle_quiet_command()`: Processes `/quiet` symbolic command
- `handle_pulse_command()`: Processes `/pulse` pattern analysis command
- `handle_mirror_command()`: Processes `/mirror` reflection command
- `check_crisis_keywords()`: Detects crisis language in user input
- `handle_crisis_response()`: Provides trauma-safe crisis containment

**Usage Example**:
```bash
# Basic usage
python main.py

# With custom memory path
python main.py --memory /path/to/custom/memory.json

# Quiet mode
python main.py --quiet
```

**Key Features**:
- **Command Line Options**: `--quiet`, `--memory`
- **Symbolic Commands**: `/quiet`, `/pulse`, `/mirror`
- **Crisis Detection**: Automatic detection of crisis language
- **Session Management**: Handles user sessions and interaction flow

### 2. Configuration Management (`config.py`)

**Purpose**: Centralized configuration management for SYLVA settings and behavior.

**Key Components**:
- `SYLVA_CONFIG`: Main configuration dictionary
- `ARCHETYPE_CONFIG`: Archetype-specific settings
- `EMOTION_KEYWORDS`: Emotional keyword mappings
- `get_config()`: Configuration retrieval function
- `get_archetype_config()`: Archetype configuration access
- `get_emotion_keywords()`: Emotional keyword access

**Configuration Categories**:

#### Symbolic UX Settings
```python
"enable_rituals": True,              # Enable ritual-like interactions
"max_response_length": 200,          # Maximum response length
"enable_archetype_exploration": True, # Allow archetype exploration
"use_emoji": True,                   # Use emoji in responses
"enable_memory_reflection": True,    # Enable memory reflection
```

#### Interaction Settings
```python
"default_memory_limit": 10,          # Default interactions to show
"max_memory_entries": 1000,          # Maximum interactions to keep
"session_timeout_minutes": 30,       # Session timeout
```

#### Safety Settings
```python
"emergency_keywords": [               # Crisis detection keywords
    "suicide", "kill myself", "want to die"
],
"crisis_response": "If you're in crisis...", # Crisis response message
```

**Usage Example**:
```python
from config import get_config, get_archetype_config

# Get configuration value
max_length = get_config("max_response_length", 200)

# Get archetype configuration
ember_config = get_archetype_config("the_ember")
```

### 3. Metaphor Engine (`utils/metaphor_engine.py`)

**Purpose**: Core symbolic response generation with subsystem-based processing.

**Key Components**:
- `MetaphorEngine`: Main metaphor processing class
- `load_metaphor_data()`: Loads metaphor library from JSON
- `init_fallback_metaphors()`: Initializes fallback metaphors
- `init_subsystem_mapping()`: Sets up subsystem keyword mappings
- `init_ritual_closures()`: Loads ritual closure phrases
- `detect_subsystem()`: Routes input to appropriate subsystem
- `select_metaphor_for_subsystem()`: Chooses metaphor from subsystem
- `construct_subsystem_response()`: Builds complete response
- `append_ritual_closure()`: Adds symbolic ending to response
- `generate_response()`: Main response generation method

**Subsystem Detection Algorithm**:
```python
def detect_subsystem(self, text: str) -> str:
    """Routes emotional content to appropriate symbolic subsystem."""
    scores = {
        'MARROW': self._calculate_marrow_score(text),
        'ROOT': self._calculate_root_score(text),
        'AURA': self._calculate_aura_score(text)
    }
    return max(scores, key=scores.get)
```

**Usage Example**:
```python
from utils.metaphor_engine import MetaphorEngine

engine = MetaphorEngine()
response, subsystem = engine.generate_response("I feel overwhelmed")
print(f"Response: {response}")
print(f"Subsystem: {subsystem}")
```

**Key Features**:
- **Subsystem Routing**: MARROW/ROOT/AURA processing
- **Metaphor Selection**: Context-aware archetype selection
- **Ritual Closures**: Symbolic ending phrases
- **Safety Validation**: Trauma-safe response generation

### 4. Memory Logger (`utils/memory_log.py`)

**Purpose**: Interaction logging and pattern analysis with subsystem tracking.

**Key Components**:
- `MemoryLogger`: Main memory management class
- `_initialize_memory_file()`: Creates memory file structure
- `_read_memory()`: Reads memory data from JSON
- `_write_memory()`: Writes memory data to JSON
- `log_interaction()`: Logs user interaction with metadata
- `_generate_interaction_id()`: Creates unique interaction IDs
- `_recalculate_subsystem_activity()`: Updates subsystem statistics
- `_get_session_id()`: Manages session identification
- `display_memory()`: Shows interaction history
- `_display_subsystem_summary()`: Shows subsystem activity
- `get_interaction_count()`: Returns interaction count
- `get_recent_interactions()`: Retrieves recent interactions
- `get_subsystem_activity()`: Returns subsystem statistics
- `get_subsystem_patterns()`: Analyzes subsystem patterns
- `clear_memory()`: Clears interaction history
- `export_memory()`: Exports memory data
- `get_memory_stats()`: Returns memory statistics

**Memory Data Structure**:
```json
{
  "interactions": [
    {
      "id": "uuid",
      "timestamp": "2025-01-12T14:30:00Z",
      "session_id": "session_uuid",
      "user_input": "I feel overwhelmed",
      "sylva_response": "The tide recedes, but it will return.",
      "subsystem": "AURA",
      "metaphor_used": "the_tide"
    }
  ],
  "subsystem_activity": {
    "MARROW": 8,
    "ROOT": 3,
    "AURA": 2
  },
  "patterns": {
    "recent_subsystems": ["AURA", "MARROW", "AURA"],
    "metaphor_frequency": {"the_tide": 3, "the_ember": 2}
  }
}
```

**Usage Example**:
```python
from utils.memory_log import MemoryLogger

logger = MemoryLogger()
logger.log_interaction("I feel lost", "The mountain stands.", "ROOT")
logger.display_memory(limit=5)
```

**Key Features**:
- **Interaction Logging**: Complete interaction history
- **Subsystem Tracking**: Activity statistics by subsystem
- **Pattern Analysis**: Temporal pattern detection
- **Memory Management**: Export, clear, and statistics
- **Session Management**: Session-based interaction grouping

## Data Modules

### 5. Metaphor Library (`data/sample_metaphors.json`)

**Purpose**: Comprehensive metaphor library with archetype definitions and subsystem mappings.

**Structure**:
```json
{
  "metaphors": {
    "the_ember": {
      "descriptions": ["A small flame that persists in darkness"],
      "responses": ["The ember holds steady in the wind."],
      "contexts": ["darkness", "persistence", "hope"],
      "affective_tags": ["anger", "passion", "core_wounds"],
      "subsystem": "MARROW"
    }
  },
  "universal_responses": ["You are here, and that is enough."],
  "ritual_phrases": ["The circle is cast, the space is held."],
  "ritual_closures": ["That's enough for now."],
  "safety_responses": {
    "crisis": "If you're in crisis..."
  },
  "subsystem_definitions": {
    "MARROW": {
      "description": "Deep core processing",
      "keywords": ["shame", "trauma", "betrayal"]
    }
  },
  "affective_keyword_mapping": {
    "shame": {
      "metaphors": ["the_cave", "the_mask"],
      "subsystem": "MARROW"
    }
  }
}
```

**Key Features**:
- **13 Core Archetypes**: Complete symbolic vocabulary
- **Subsystem Organization**: MARROW/ROOT/AURA categorization
- **Affective Mapping**: Emotional keyword associations
- **Safety Responses**: Crisis containment phrases
- **Ritual Language**: Sacred interaction phrases

## Testing Modules

### 6. Basic Tests (`tests/test_sylva.py`)

**Purpose**: Basic functionality testing for core SYLVA components.

**Test Categories**:
- `test_metaphor_engine()`: Metaphor engine functionality
- `test_memory_logger()`: Memory logging system
- `test_config()`: Configuration management

**Usage**:
```bash
pytest tests/test_sylva.py -v
```

### 7. Diagnostic Tests (`tests/test_sylva_diagnostics.py`)

**Purpose**: Comprehensive diagnostic testing with pattern analysis and safety validation.

**Key Components**:
- `generate_symbolic_response()`: Symbolic response generation
- `log_interaction()`: Interaction logging
- `get_memory_entries()`: Memory retrieval
- `SymbolicDriftAnalyzer`: Pattern drift analysis
- `CrisisContainmentValidator`: Safety validation
- `run_enhanced_symbolic_tests()`: Comprehensive test suite

**Usage**:
```bash
pytest tests/test_sylva_diagnostics.py -v
```

### 8. Comprehensive Tests (`tests/test_comprehensive_sylva.py`)

**Purpose**: Full system integration testing with performance benchmarking.

**Key Components**:
- `SYLVADiagnosticSystem`: Complete diagnostic system
- `test_metaphor_engine_initialization()`: Engine setup testing
- `test_subsystem_detection()`: Subsystem routing validation
- `test_metaphor_generation()`: Response generation testing
- `test_memory_logging()`: Memory system validation
- `test_symbolic_commands()`: Command system testing
- `test_crisis_detection()`: Safety system validation
- `test_metaphor_data_integrity()`: Data integrity checking
- `test_configuration_integrity()`: Configuration validation
- `test_integration_workflow()`: Integration testing
- `run_performance_benchmarks()`: Performance testing
- `generate_diagnostic_report()`: Report generation

**Usage**:
```bash
pytest tests/test_comprehensive_sylva.py -v
```

### 9. Enhanced Diagnostic Tests (`tests/test_sylva_enhanced_diagnostics.py`)

**Purpose**: Advanced diagnostic testing with drift analysis and safety validation.

**Key Components**:
- `SYLVAEnhancedDiagnostics`: Enhanced diagnostic system
- `test_subsystem_drift_simulation()`: Drift pattern testing
- `test_ritual_closure_validation()`: Ritual closure checking
- `test_forbidden_phrase_detection()`: Safety phrase detection
- `test_visual_subsystem_glyphs()`: Visual glyph testing
- `test_ux_command_validation()`: UX command validation
- `test_high_distress_safety_scan()`: High distress safety testing

**Usage**:
```bash
pytest tests/test_sylva_enhanced_diagnostics.py -v
```

## Diagnostic Modules

### 10. Enhanced Diagnostics (`diagnostics/enhanced_sylva_diagnostics.py`)

**Purpose**: Advanced diagnostic tools for system validation and pattern analysis.

**Key Components**:
- `check_ritual_closure()`: Ritual closure validation
- `detect_forbidden_phrases()`: Forbidden phrase detection
- `log_with_glyph()`: Glyph-based logging
- `run_drift_simulation()`: Drift pattern simulation
- `run_symbolic_tests()`: Symbolic test execution

**Usage**:
```python
from diagnostics.enhanced_sylva_diagnostics import run_symbolic_tests
results = run_symbolic_tests()
```

### 11. Diagnostic Documentation (`diagnostics/SYLVA_DIAGNOSTIC_ENHANCEMENTS.md`)

**Purpose**: Documentation of diagnostic system enhancements and capabilities.

**Content**:
- Enhanced subsystem routing
- Crisis containment validation
- Symbolic drift analysis
- Visual subsystem glyphs
- Safety constraint enforcement

## Utility Modules

### 12. Utils Package (`utils/__init__.py`)

**Purpose**: Package initialization and utility function exports.

**Exports**:
- `MetaphorEngine`: Main metaphor processing class
- `MemoryLogger`: Memory management class
- Utility functions and constants

## Demo Modules

### 13. Enhanced Functionality Demo (`demo_enhanced_functionality.py`)

**Purpose**: Demonstration of SYLVA's enhanced features and capabilities.

**Key Features**:
- Subsystem detection demonstration
- Pattern analysis visualization
- Symbolic command examples
- Archetype distribution display
- Memory system statistics

**Usage**:
```bash
python demo_enhanced_functionality.py
```

## Module Interactions

### Data Flow Between Modules

```
User Input (main.py)
    ↓
Input Validation & Command Detection
    ↓
Crisis Detection (if needed)
    ↓
Subsystem Detection (metaphor_engine.py)
    ↓
Metaphor Selection (metaphor_engine.py)
    ↓
Response Construction (metaphor_engine.py)
    ↓
Ritual Closure Addition (metaphor_engine.py)
    ↓
Memory Logging (memory_log.py)
    ↓
Response Display (main.py)
```

### Configuration Flow

```
config.py
    ↓
SYLVA_CONFIG → Main application settings
    ↓
ARCHETYPE_CONFIG → Archetype-specific settings
    ↓
EMOTION_KEYWORDS → Emotional keyword mappings
    ↓
Metaphor Engine & Memory Logger
```

### Testing Flow

```
test_sylva.py → Basic functionality
    ↓
test_sylva_diagnostics.py → Diagnostic testing
    ↓
test_comprehensive_sylva.py → Integration testing
    ↓
test_sylva_enhanced_diagnostics.py → Advanced diagnostics
```

## Module Dependencies

### Core Dependencies
- `main.py` → `utils/metaphor_engine.py`, `utils/memory_log.py`, `config.py`
- `utils/metaphor_engine.py` → `data/sample_metaphors.json`, `config.py`
- `utils/memory_log.py` → `config.py`
- All test modules → Core modules

### External Dependencies
- `typer`: CLI framework
- `rich`: Terminal formatting
- `pathlib2`: Path manipulation
- `pytest`: Testing framework (development)

## Module Configuration

### Environment-Specific Settings

#### Development
```python
DEV_CONFIG = {
    "debug_mode": True,
    "log_level": "DEBUG",
    "memory_path": "memory/dev_user_log.json"
}
```

#### Production
```python
PROD_CONFIG = {
    "debug_mode": False,
    "log_level": "INFO",
    "memory_path": "memory/prod_user_log.json"
}
```

### Module-Specific Configuration

#### Metaphor Engine
```python
METAPHOR_ENGINE_CONFIG = {
    "max_response_length": 200,
    "archetype_response_probability": 0.7,
    "universal_response_probability": 0.3
}
```

#### Memory Logger
```python
MEMORY_LOGGER_CONFIG = {
    "max_interactions": 1000,
    "session_timeout_minutes": 30,
    "enable_compression": True
}
```

## Module Maintenance

### Regular Maintenance Tasks

#### Daily
- Check memory file integrity
- Monitor subsystem activity patterns
- Validate ritual closure consistency

#### Weekly
- Run comprehensive test suite
- Analyze pattern drift
- Update metaphor library if needed

#### Monthly
- Performance benchmarking
- Security validation
- Documentation updates

### Troubleshooting Common Issues

#### Metaphor Engine Issues
```python
# Debug subsystem detection
def debug_subsystem_detection(text: str) -> Dict:
    engine = MetaphorEngine()
    scores = {
        'MARROW': engine._calculate_marrow_score(text),
        'ROOT': engine._calculate_root_score(text),
        'AURA': engine._calculate_aura_score(text)
    }
    return {'input': text, 'scores': scores, 'detected': max(scores, key=scores.get)}
```

#### Memory Logger Issues
```python
# Debug memory system
def debug_memory_system(memory_path: str) -> Dict:
    try:
        with open(memory_path, 'r') as f:
            data = json.load(f)
        return {
            'file_exists': True,
            'interaction_count': len(data.get('interactions', [])),
            'subsystem_activity': data.get('subsystem_activity', {})
        }
    except Exception as e:
        return {'file_exists': False, 'error': str(e)}
```

## Module Extensions

### Adding New Metaphors
```python
# Add to data/sample_metaphors.json
{
  "the_new_archetype": {
    "descriptions": ["Poetic description"],
    "responses": ["Symbolic response"],
    "contexts": ["emotional_context"],
    "affective_tags": ["emotion"],
    "subsystem": "MARROW|ROOT|AURA"
  }
}
```

### Adding New Subsystems
```python
# Update config.py
NEW_SUBSYSTEM_KEYWORDS = {
    "NEW_SUBSYSTEM": ["keyword1", "keyword2", "keyword3"]
}

# Update metaphor_engine.py
def _calculate_new_subsystem_score(self, text: str) -> float:
    # Implementation for new subsystem scoring
    pass
```

### Adding New Commands
```python
# Update main.py
def handle_new_command():
    """Process new symbolic command."""
    return "Symbolic response for new command"

# Update command routing in main()
elif user_input.startswith('/newcommand'):
    response = handle_new_command()
```

---

## Module Best Practices

### Code Organization
- Keep modules focused on single responsibility
- Use clear, descriptive module names
- Maintain consistent import structure
- Document all public interfaces

### Testing Strategy
- Unit tests for individual modules
- Integration tests for module interactions
- Performance tests for critical paths
- Safety tests for trauma-safe boundaries

### Documentation Standards
- Comprehensive docstrings for all functions
- Clear module purpose statements
- Usage examples for complex functionality
- Troubleshooting guides for common issues

### Performance Considerations
- Cache frequently accessed data
- Optimize memory usage for large datasets
- Profile critical code paths
- Monitor subsystem performance

---

*"Each module serves the sacred whole, and the whole serves each module."* - SYLVA 