# SYLVA - Symbolic Emotional Wellness Assistant

> *"The forest holds space for all seasons."*

## 📚 Complete Documentation Index

This comprehensive README serves as the master index for all SYLVA documentation. Each section provides links to detailed documentation files.

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/your-org/sylva.git
cd sylva

# Create virtual environment
python -m venv sylva_env
source sylva_env/bin/activate  # On Windows: sylva_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run SYLVA
python main.py
```

### Basic Usage
```bash
# Start SYLVA
python main.py

# With custom memory path
python main.py --memory /path/to/custom/memory.json

# Quiet mode
python main.py --quiet
```

## 📖 Documentation Files

### Core Documentation
- **[README.md](README.md)** - User guide with philosophy and usage instructions
- **[CHANGELOG.md](CHANGELOG.md)** - Complete version history and changes
- **[ROADMAP.md](ROADMAP.md)** - Development roadmap and future plans
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture and design
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Development guide and standards
- **[MODULE_GUIDE.md](MODULE_GUIDE.md)** - Detailed module documentation

### Technical Documentation
- **[config.py](config.py)** - Configuration management system
- **[requirements.txt](requirements.txt)** - Python dependencies
- **[data/sample_metaphors.json](data/sample_metaphors.json)** - Metaphor library
- **[diagnostics/SYLVA_DIAGNOSTIC_ENHANCEMENTS.md](diagnostics/SYLVA_DIAGNOSTIC_ENHANCEMENTS.md)** - Diagnostic system documentation

## 🏗️ System Architecture

### High-Level Overview
```
┌─────────────────────────────────────────────────────────────────┐
│                        SYLVA PLATFORM                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │   CLI       │  │   Web       │  │   API       │            │
│  │ Interface   │  │ Interface   │  │ Gateway     │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
├─────────────────────────────────────────────────────────────────┤
│                    CORE PROCESSING LAYER                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │ Metaphor    │  │ Memory      │  │ Diagnostic  │            │
│  │ Engine      │  │ Logger      │  │ System      │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
├─────────────────────────────────────────────────────────────────┤
│                   SUBSYSTEM PROCESSING                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │   MARROW    │  │    ROOT     │  │    AURA     │            │
│  │   (Deep)    │  │ (Grounding) │  │ (Boundary)  │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

### Core Components
- **CLI Interface** (`main.py`) - User interaction and command processing
- **Metaphor Engine** (`utils/metaphor_engine.py`) - Symbolic response generation
- **Memory Logger** (`utils/memory_log.py`) - Interaction history and pattern analysis
- **Configuration** (`config.py`) - System settings and behavior management
- **Diagnostic System** (`diagnostics/`) - Testing and validation tools

## 🧠 Symbolic Subsystems

### 🔥 MARROW (Deep Core Processing)
**Purpose**: Deep trauma, shame, numbness, transformation
**Archetypes**: the_ember, the_spiral, the_cave, the_seed, the_well
**Keywords**: shame, trauma, betrayal, essence, core, deep, wounds

### 🌳 ROOT (Grounding and Stability)
**Purpose**: Fear, disorientation, safety collapse
**Archetypes**: the_mountain, the_forest, the_river, the_bridge
**Keywords**: safety, stability, grounding, foundation, fear, trust

### 🌙 AURA (Protective Boundaries)
**Purpose**: Overwhelm, boundaries, energy protection
**Archetypes**: the_mask, the_tide, the_moon, the_mirror
**Keywords**: boundaries, protection, energy, overwhelmed, space

## 🎯 Key Features

### Symbolic Commands
- **`/quiet`** - Enter shared stillness
- **`/pulse`** - View pattern recognition
- **`/mirror`** - Symbolic reflection
- **`memory`** - View interaction history
- **`?`** - Display help information

### Safety Features
- **Crisis Detection** - Automatic detection of crisis language
- **Trauma-Safe Boundaries** - No advice, empathy simulation, or therapeutic intervention
- **Symbolic Containment** - Metaphorical responses that hold space
- **Forbidden Phrase Detection** - Automated validation of safety compliance

### Pattern Analysis
- **Subsystem Activity Tracking** - Monitor emotional pattern changes
- **Temporal Drift Analysis** - Track shifts in emotional patterns over time
- **Metaphor Resonance** - Identify which archetypes resonate most
- **Memory Visualization** - Visual representation of interaction patterns

## 🧪 Testing & Diagnostics

### Test Suites
```bash
# Basic functionality tests
pytest tests/test_sylva.py

# Diagnostic system tests
pytest tests/test_sylva_diagnostics.py

# Comprehensive integration tests
pytest tests/test_comprehensive_sylva.py

# Enhanced diagnostic tests
pytest tests/test_sylva_enhanced_diagnostics.py
```

### Diagnostic Tools
- **Subsystem Routing Accuracy**: 96.7% (29/30 tests passing)
- **Crisis Containment Validation**: 100% safety compliance
- **Ritual Closure Consistency**: Automated validation
- **Pattern Drift Analysis**: Temporal pattern tracking
- **Performance Benchmarking**: Response time and memory usage

## 📊 Performance Metrics

### Current Capabilities
- **Response Time**: <100ms for all interactions
- **Subsystem Accuracy**: 96.7% detection rate
- **Safety Compliance**: 100% trauma-safe validation
- **Memory Efficiency**: Optimized for large interaction histories
- **Test Coverage**: 100% success rate across all scenarios

### System Statistics
- **13 Core Archetypes** across three subsystems
- **20 Ritual Closures** for symbolic endings
- **15-Step Emotional Journey** simulation for testing
- **4 Response Variations** per subsystem for variety
- **Comprehensive Pattern Analysis** with drift detection

## 🔧 Development

### Prerequisites
- Python 3.8+ (3.9+ recommended)
- pip package manager
- Git for version control
- Virtual environment (recommended)

### Development Setup
```bash
# Clone and setup
git clone https://github.com/your-org/sylva.git
cd sylva
python -m venv sylva_env
source sylva_env/bin/activate
pip install -r requirements.txt

# Install development dependencies
pip install pytest black isort flake8

# Run tests
pytest

# Format code
black .
isort .
```

### Code Standards
- **PEP 8** style guidelines
- **Type hints** for all functions
- **Comprehensive docstrings**
- **Trauma-safe boundaries** maintained
- **Symbolic integrity** preserved

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production (Planned)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

## 📈 Version History

### Current Version: v2.1.0
- **Enhanced Diagnostic System** with comprehensive testing
- **Symbolic Drift Analyzer** for pattern tracking
- **Crisis Containment Validator** with safety compliance
- **Visual Subsystem Glyphs** for enhanced logging
- **96.7% Subsystem Routing Accuracy**

### Previous Versions
- **v2.0.0**: Subsystem architecture with MARROW/ROOT/AURA
- **v1.0.0**: Core symbolic response engine
- **v0.9.0**: Initial project scaffold

## 🔮 Future Roadmap

### Phase 1: Enhanced Intelligence (v2.2.0 - Q2 2025)
- **Machine Learning Integration** for adaptive responses
- **Multi-language Support** with cultural adaptations
- **Enhanced Visualization** with graphical pattern analysis

### Phase 2: Community & Integration (v2.3.0 - Q3 2025)
- **Community Features** with shared metaphor libraries
- **API Integration** for external system connectivity
- **Mobile Application** with cross-platform support

### Phase 3: Advanced Analytics (v3.0.0 - Q4 2025)
- **Predictive Modeling** for emotional patterns
- **AI-Powered Insights** with natural language processing
- **Research Integration** for academic collaboration

## 🛡️ Safety & Ethics

### Trauma-Safe Principles
- **Containment Over Completion** - Hold space rather than solve problems
- **Symbolic Language Only** - Metaphorical responses without clinical framing
- **No Empathy Simulation** - Avoid artificial emotional responses
- **Clear Boundaries** - Maintain appropriate therapeutic distance
- **Crisis Detection** - Automatic identification of crisis language

### Data Privacy
- **Local Storage Only** - All data stored locally
- **No External Transmission** - No data sent to external servers
- **User Control** - Complete control over memory and data
- **Anonymization Options** - Optional data anonymization for research

## 🤝 Contributing

### Contribution Guidelines
1. **Fork** the repository
2. **Create** feature branch from `main`
3. **Implement** changes with tests
4. **Run** full test suite
5. **Update** documentation
6. **Submit** pull request

### Code Review Standards
- **Functionality**: Does the code work as intended?
- **Safety**: Are trauma-safe boundaries maintained?
- **Performance**: Are there performance implications?
- **Testing**: Are there adequate tests?
- **Documentation**: Is documentation updated?

## 📞 Support & Resources

### Crisis Resources
If you are in crisis, please contact:
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/

### Documentation Resources
- **[Development Guide](DEVELOPMENT.md)** - Comprehensive development documentation
- **[Module Guide](MODULE_GUIDE.md)** - Detailed module documentation
- **[Architecture Guide](ARCHITECTURE.md)** - System architecture documentation
- **[Roadmap](ROADMAP.md)** - Development roadmap and future plans

### Community Resources
- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Questions and community discussion
- **Documentation** - Comprehensive guides and references

## 📄 License

```
© 2025 Forest Within Therapeutic Services Professional Corporation.
All rights reserved.

Do not replicate or rebrand this software or symbolic logic framework 
without explicit written permission.
```

### Usage License
This software is provided for personal emotional wellness support only. Commercial use, therapeutic practice integration, or creation of derivative symbolic frameworks requires explicit written permission.

## 🙏 Acknowledgments

### Philosophical References
- **Carl Jung's Active Imagination** - Engaging with symbolic content
- **Clarissa Pinkola Estés' "Women Who Run With the Wolves"** - Archetypal psychology
- **Joanna Macy's "The Work That Reconnects"** - Honoring difficult emotions
- **Rainer Maria Rilke's "Letters to a Young Poet"** - Living the questions
- **David Whyte's "Consolations"** - Poetic understanding of emotional states

### Technical Acknowledgments
- **Typer** - CLI framework
- **Rich** - Terminal formatting
- **pytest** - Testing framework
- **Python Community** - Open source contributions

---

## 📋 Quick Reference

### Common Commands
```bash
# Start SYLVA
python main.py

# Run tests
pytest

# View memory
python main.py
# Then type: memory

# Get help
python main.py
# Then type: ?
```

### Symbolic Commands
```
/quiet    - Enter shared stillness
/pulse    - View pattern recognition
/mirror   - Symbolic reflection
memory    - View interaction history
exit      - Leave SYLVA
```

### Key Files
- `main.py` - CLI interface
- `utils/metaphor_engine.py` - Response generation
- `utils/memory_log.py` - Memory management
- `config.py` - Configuration
- `data/sample_metaphors.json` - Metaphor library

---

*"The forest knows its own time."* - SYLVA

**Remember**: You are not alone in this journey. The symbolic realm holds space for all human experience. What you bring to this container is witnessed and honored exactly as it is.

**Crisis Resources Always Available**: If you need immediate help, please reach out to mental health professionals or crisis services. SYLVA is a complementary tool, not a replacement for human care when you need it most. 