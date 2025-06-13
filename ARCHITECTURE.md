# SYLVA Architecture Map

> *"The structure holds the space for what flows through it."*

## System Overview

SYLVA is built on a modular, subsystem-based architecture that prioritizes symbolic emotional containment over therapeutic intervention. The system maintains strict boundaries between components while enabling sophisticated pattern recognition and safety validation.

## High-Level Architecture

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
├─────────────────────────────────────────────────────────────────┤
│                    DATA PERSISTENCE                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │   Memory    │  │   Config    │  │   Metaphor  │            │
│  │   Storage   │  │   Files     │  │   Library   │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

## Component Architecture

### 1. Interface Layer

#### CLI Interface (`main.py`)
```python
class SYLVACLI:
    def __init__(self):
        self.metaphor_engine = MetaphorEngine()
        self.memory_logger = MemoryLogger()
        self.diagnostic_system = DiagnosticSystem()
    
    def process_interaction(self, user_input: str) -> str:
        # 1. Validate input and check for commands
        # 2. Route to appropriate subsystem
        # 3. Generate symbolic response
        # 4. Log interaction
        # 5. Return response with ritual closure
```

**Responsibilities:**
- User input processing and validation
- Command routing (`/quiet`, `/pulse`, `/mirror`)
- Crisis detection and containment
- Response formatting and display
- Session management

**Data Flow:**
```
User Input → Input Validation → Command Detection → 
Subsystem Routing → Response Generation → Memory Logging → 
Ritual Closure → Display Response
```

#### Web Interface (Planned)
```python
class SYLVAWebInterface:
    def __init__(self):
        self.api_client = APIClient()
        self.visualization_engine = VisualizationEngine()
    
    def render_dashboard(self, user_data: Dict) -> str:
        # Generate HTML/CSS/JS for web dashboard
        # Include pattern visualization
        # Provide interactive elements
```

#### API Gateway (Planned)
```python
class SYLVAAPIGateway:
    def __init__(self):
        self.authentication = OAuthAuthenticator()
        self.rate_limiter = RateLimiter()
        self.request_processor = RequestProcessor()
    
    @app.post("/api/v1/interactions")
    async def log_interaction(self, interaction: InteractionModel):
        # Process API requests
        # Validate authentication
        # Apply rate limiting
        # Route to core processing
```

### 2. Core Processing Layer

#### Metaphor Engine (`utils/metaphor_engine.py`)
```python
class MetaphorEngine:
    def __init__(self):
        self.metaphors = self.load_metaphor_data()
        self.subsystem_mapping = self.init_subsystem_mapping()
        self.ritual_closures = self.init_ritual_closures()
    
    def generate_response(self, user_input: str) -> Tuple[str, str]:
        # 1. Detect appropriate subsystem
        # 2. Select metaphor from subsystem
        # 3. Construct response
        # 4. Append ritual closure
        # 5. Return response and subsystem
```

**Key Methods:**
- `detect_subsystem(text: str) -> str`: Routes input to MARROW/ROOT/AURA
- `select_metaphor_for_subsystem(subsystem: str, text: str) -> Dict`: Chooses appropriate archetype
- `construct_subsystem_response(metaphor: Dict, subsystem: str, user_input: str) -> str`: Builds response
- `append_ritual_closure(response: str) -> str`: Adds symbolic ending

**Subsystem Detection Algorithm:**
```python
def detect_subsystem(self, text: str) -> str:
    scores = {
        'MARROW': self._calculate_marrow_score(text),
        'ROOT': self._calculate_root_score(text),
        'AURA': self._calculate_aura_score(text)
    }
    return max(scores, key=scores.get)
```

#### Memory Logger (`utils/memory_log.py`)
```python
class MemoryLogger:
    def __init__(self, custom_memory_path: Optional[str] = None):
        self.memory_path = custom_memory_path or "memory/user_log.json"
        self.session_id = self._get_session_id()
    
    def log_interaction(self, user_input: str, sylva_response: str, subsystem: str):
        # 1. Create interaction record
        # 2. Update subsystem activity tracking
        # 3. Persist to JSON storage
        # 4. Update pattern analysis
```

**Data Structure:**
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

#### Diagnostic System (`diagnostics/enhanced_sylva_diagnostics.py`)
```python
class SYLVAEnhancedDiagnostics:
    def __init__(self):
        self.crisis_validator = CrisisContainmentValidator()
        self.drift_analyzer = SymbolicDriftAnalyzer()
        self.safety_scanner = SafetyScanner()
    
    def run_comprehensive_diagnostics(self) -> Dict:
        # 1. Test subsystem routing accuracy
        # 2. Validate crisis containment
        # 3. Check ritual closure consistency
        # 4. Scan for forbidden phrases
        # 5. Analyze pattern detection
```

### 3. Subsystem Processing Layer

#### MARROW Subsystem (Deep Core Processing)
```python
class MarrowSubsystem:
    def __init__(self):
        self.archetypes = [
            "the_ember", "the_spiral", "the_cave", 
            "the_seed", "the_well"
        ]
        self.keywords = [
            "shame", "trauma", "betrayal", "essence", 
            "core", "deep", "wounds", "transformation"
        ]
    
    def process_emotional_content(self, text: str) -> Dict:
        # Process deep emotional content
        # Handle trauma and core wounds
        # Generate transformative metaphors
```

#### ROOT Subsystem (Grounding and Stability)
```python
class RootSubsystem:
    def __init__(self):
        self.archetypes = [
            "the_mountain", "the_forest", "the_river", 
            "the_bridge"
        ]
        self.keywords = [
            "safety", "stability", "grounding", "foundation",
            "basic", "trust", "survival", "fear"
        ]
    
    def process_emotional_content(self, text: str) -> Dict:
        # Process safety and stability needs
        # Handle fear and disorientation
        # Generate grounding metaphors
```

#### AURA Subsystem (Protective Boundaries)
```python
class AuraSubsystem:
    def __init__(self):
        self.archetypes = [
            "the_mask", "the_tide", "the_moon", 
            "the_mirror"
        ]
        self.keywords = [
            "boundaries", "protection", "energy", "overwhelmed",
            "space", "buffer", "sensitive", "invasion"
        ]
    
    def process_emotional_content(self, text: str) -> Dict:
        # Process boundary and protection needs
        # Handle overwhelm and energy management
        # Generate protective metaphors
```

## Data Flow Architecture

### Primary Interaction Flow
```
1. User Input
   ↓
2. Input Validation & Command Detection
   ↓
3. Crisis Detection (if needed)
   ↓
4. Subsystem Detection & Routing
   ↓
5. Metaphor Selection
   ↓
6. Response Construction
   ↓
7. Ritual Closure Addition
   ↓
8. Memory Logging
   ↓
9. Response Display
```

### Memory Persistence Flow
```
1. Interaction Data
   ↓
2. Subsystem Activity Update
   ↓
3. Pattern Analysis
   ↓
4. JSON Serialization
   ↓
5. File System Storage
   ↓
6. Memory Statistics Update
```

### Diagnostic Flow
```
1. Test Case Generation
   ↓
2. Subsystem Routing Test
   ↓
3. Response Validation
   ↓
4. Safety Compliance Check
   ↓
5. Pattern Analysis Test
   ↓
6. Performance Benchmarking
   ↓
7. Report Generation
```

## Configuration Architecture

### Configuration Management (`config.py`)
```python
SYLVA_CONFIG = {
    "enable_rituals": True,
    "max_response_length": 200,
    "enable_archetype_exploration": True,
    "use_emoji": True,
    "enable_memory_reflection": True,
    # ... additional settings
}

ARCHETYPE_CONFIG = {
    "the_ember": {
        "color": "red",
        "element": "fire",
        "time_of_day": "night",
        "season": "winter"
    },
    # ... additional archetype configurations
}
```

### Environment-Specific Configuration
```python
# Development
DEV_CONFIG = {
    "debug_mode": True,
    "log_level": "DEBUG",
    "memory_path": "memory/dev_user_log.json"
}

# Production
PROD_CONFIG = {
    "debug_mode": False,
    "log_level": "INFO",
    "memory_path": "memory/prod_user_log.json"
}
```

## Security Architecture

### Crisis Detection & Containment
```python
class CrisisContainmentValidator:
    def __init__(self):
        self.crisis_patterns = [
            r"\b(suicide|kill myself|want to die)\b",
            r"\b(self-harm|cut myself|overdose)\b",
            r"\b(end it all|give up|no point)\b"
        ]
        self.forbidden_phrases = [
            r"\b(you should|you need to|you must)\b",
            r"\b(call|contact|reach out)\b",
            r"\b(help|support|resources)\b"
        ]
    
    def validate_crisis_response(self, response: str) -> bool:
        # Check for forbidden therapeutic language
        # Ensure symbolic containment
        # Validate trauma-safe boundaries
```

### Data Privacy & Protection
```python
class DataProtectionManager:
    def __init__(self):
        self.encryption_enabled = True
        self.anonymization_enabled = True
        self.retention_policy = RetentionPolicy()
    
    def anonymize_user_data(self, data: Dict) -> Dict:
        # Remove personally identifiable information
        # Hash sensitive identifiers
        # Maintain data integrity for analysis
```

## Performance Architecture

### Caching Strategy
```python
class SYLVACache:
    def __init__(self):
        self.metaphor_cache = LRUCache(maxsize=100)
        self.subsystem_cache = LRUCache(maxsize=50)
        self.pattern_cache = LRUCache(maxsize=200)
    
    def get_cached_metaphor(self, key: str) -> Optional[Dict]:
        # Check cache for frequently used metaphors
        # Reduce computation overhead
        # Improve response time
```

### Memory Management
```python
class MemoryManager:
    def __init__(self):
        self.max_interactions = 1000
        self.compression_enabled = True
        self.archival_policy = ArchivalPolicy()
    
    def manage_memory_size(self, memory_data: Dict) -> Dict:
        # Implement LRU eviction for old interactions
        # Compress historical data
        # Archive old patterns
```

## Testing Architecture

### Test Suite Organization
```
tests/
├── test_sylva.py                    # Basic functionality tests
├── test_sylva_diagnostics.py        # Diagnostic system tests
├── test_comprehensive_sylva.py      # Comprehensive integration tests
└── test_sylva_enhanced_diagnostics.py # Enhanced diagnostic tests
```

### Test Coverage
```python
class TestCoverage:
    def __init__(self):
        self.subsystem_tests = SubsystemTestSuite()
        self.safety_tests = SafetyTestSuite()
        self.performance_tests = PerformanceTestSuite()
        self.integration_tests = IntegrationTestSuite()
    
    def run_full_test_suite(self) -> TestResults:
        # Execute all test categories
        # Generate coverage reports
        # Validate system integrity
```

## Deployment Architecture

### Local Development
```bash
# Development setup
python -m venv sylva_env
source sylva_env/bin/activate
pip install -r requirements.txt
python main.py
```

### Production Deployment (Planned)
```dockerfile
# Dockerfile for containerized deployment
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

### Scalability Considerations
```python
class ScalabilityManager:
    def __init__(self):
        self.load_balancer = LoadBalancer()
        self.database_sharding = DatabaseSharding()
        self.cache_distribution = CacheDistribution()
    
    def scale_horizontally(self, traffic_increase: float):
        # Add additional instances
        # Distribute load across nodes
        # Maintain data consistency
```

## Integration Architecture

### External System Integration (Planned)
```python
class IntegrationManager:
    def __init__(self):
        self.api_clients = {}
        self.webhook_handlers = {}
        self.data_sync = DataSynchronizer()
    
    def integrate_with_external_system(self, system_type: str, config: Dict):
        # Establish API connections
        # Set up webhook endpoints
        # Configure data synchronization
```

### Plugin Architecture (Planned)
```python
class PluginManager:
    def __init__(self):
        self.plugin_registry = {}
        self.plugin_validator = PluginValidator()
        self.plugin_loader = PluginLoader()
    
    def load_plugin(self, plugin_path: str) -> bool:
        # Validate plugin integrity
        # Load plugin modules
        # Register plugin capabilities
```

## Monitoring & Observability

### Logging Architecture
```python
class SYLVALogger:
    def __init__(self):
        self.interaction_logger = InteractionLogger()
        self.error_logger = ErrorLogger()
        self.performance_logger = PerformanceLogger()
    
    def log_interaction(self, interaction: Dict):
        # Log user interactions
        # Track subsystem usage
        # Monitor performance metrics
```

### Metrics Collection
```python
class MetricsCollector:
    def __init__(self):
        self.response_time_metrics = ResponseTimeMetrics()
        self.subsystem_usage_metrics = SubsystemUsageMetrics()
        self.error_rate_metrics = ErrorRateMetrics()
    
    def collect_metrics(self) -> Dict:
        # Gather performance data
        # Calculate usage statistics
        # Generate health reports
```

---

## Architecture Principles

### 1. Containment Over Completion
- System maintains symbolic boundaries without therapeutic intervention
- Responses focus on witnessing rather than solving
- Architecture supports holding space for emotional content

### 2. Modular Design
- Clear separation of concerns between components
- Loose coupling enables independent development and testing
- Plug-and-play architecture for future enhancements

### 3. Safety First
- Comprehensive crisis detection and containment
- Automated validation of trauma-safe boundaries
- Built-in protection against harmful responses

### 4. Symbolic Integrity
- Metaphor-based processing maintains symbolic language
- Subsystem architecture preserves archetypal resonance
- Ritual closures ensure consistent symbolic experience

### 5. Performance & Scalability
- Efficient caching and memory management
- Horizontal scaling capabilities for future growth
- Optimized response generation for real-time interaction

---

*"The architecture holds the space for the sacred work."* - SYLVA 