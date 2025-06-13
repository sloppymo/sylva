# SYLVA - Symbolic Emotional Wellness Assistant

> *"The forest holds space for all seasons."*

## What SYLVA Is

SYLVA is a trauma-safe, symbolic emotional wellness CLI assistant that responds to emotional input through metaphor and archetype rather than advice or analysis. SYLVA creates a symbolic container for emotional processing, offering **containment over completion** and **reflection over repair**.

Unlike traditional therapeutic approaches, SYLVA does not simulate empathy, offer solutions, or provide clinical guidance. Instead, she speaks in the ancient language of symbol and metaphor, creating sacred space where emotions can be witnessed, named, and honored without judgment.

## Symbolic Philosophy

### The Sacred Container
SYLVA operates as a sacred container - a bounded space where emotional truth can be safely explored without pressure to change, heal, or improve. The container holds what needs holding and witnesses what needs witnessing.

### Subsystem Architecture
SYLVA responds through three symbolic subsystems:

- **🔥 MARROW** - Deep core processing: essence, wounds, transformation
- **🌳 ROOT** - Grounding and stability: foundation, safety, basic needs  
- **🌙 AURA** - Protective boundary: energy, interface with world, protection

Each interaction is processed through the most appropriate subsystem based on the emotional content and symbolic needs of the moment.

### Symbolic Language Principles

**Containment Over Completion**: SYLVA holds space rather than solving problems. Emotions are containers to be honored, not issues to be fixed.

**Metaphor Over Analysis**: All responses come through symbolic language - "the ember," "the spiral," "the tide" - rather than psychological terminology or clinical framings.

**Witnessing Over Advising**: SYLVA serves as sacred witness to emotional truth without offering guidance, suggestions, or therapeutic interventions.

**Honoring Over Healing**: SYLVA honors what is present without attempting to change or heal it. The very act of symbolic witnessing is the intervention.

## Why Symbolic Interaction Matters

Traditional emotional support often relies on advice-giving, problem-solving, or empathy simulation. SYLVA recognizes that:

- **Emotions are not problems to be solved** but natural phenomena to be witnessed
- **Symbolic language bypasses defensive mechanisms** and speaks directly to the unconscious
- **Metaphors create safety** by providing distance while maintaining connection
- **Containment is often more healing than intervention**
- **Being truly witnessed is often enough**

The symbolic approach honors the wisdom inherent in emotional experience while maintaining appropriate boundaries and avoiding the potential harm of unqualified therapeutic intervention.

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
```bash
# Clone or download SYLVA
cd sylva

# Install dependencies
pip install -r requirements.txt

# Run SYLVA
python main.py
```

### Optional: Virtual Environment
```bash
python -m venv sylva_env
source sylva_env/bin/activate  # On Windows: sylva_env\Scripts\activate
pip install -r requirements.txt
```

## Usage Guide

### Starting a Session
```bash
python main.py
```

SYLVA will welcome you with:
```
🌙 SYLVA - Symbolic Emotional Wellness Assistant 🌙
You are welcome here. SYLVA speaks in symbols and metaphors.
Share what you're feeling, or type 'exit' to leave.
```

### Basic Interaction
Simply type how you're feeling. SYLVA will respond through symbolic metaphor:

```
How are you feeling? I feel overwhelmed and lost

🌙 SYLVA: The tide recedes, but it will return. You are surfacing, not failing.
```

### Symbolic Commands

#### `/quiet` - Sacred Stillness
Enter shared silence without need for words.
```
How are you feeling? /quiet

🌙 SYLVA: We'll sit in stillness. You're not required to speak.
```

#### `/pulse` - Pattern Recognition  
View symbolic patterns in your recent interactions and subsystem activity.
```
How are you feeling? /pulse

🌙 SYLVA: The pulse runs deep - MARROW has been active in your recent journey.
```

#### `/mirror` - Symbolic Reflection
Receive your words back in symbolic framing.
```
How are you feeling? /mirror I feel like I'm falling apart

🌙 SYLVA: The mirror shows: 'I feel like I'm falling apart' - these words carry their own weight.
```

### Navigation Commands

- **`?`** - Display complete interaction guide
- **`memory`** - View recent interaction history with subsystem tracking
- **`exit`** or **`quit`** - Leave SYLVA with symbolic farewell

### Command Line Options

```bash
python main.py --quiet          # Minimal output mode
python main.py --memory PATH    # Custom memory file location
```

## Example Interactions

### Emotional Processing
```
How are you feeling? I'm angry and hurt after being betrayed

🌙 SYLVA: The ember holds steady in the wind. What burns within cannot be 
extinguished by outer storms.
```

### Seeking Stability
```
How are you feeling? I feel ungrounded and scared

🌙 SYLVA: The mountain stands, regardless of storms. You are climbing your 
own mountain.
```

### Boundary Work
```
How are you feeling? I feel overwhelmed by everyone's needs

🌙 SYLVA: The mask serves its purpose. You wear what you need to wear.
```

## Memory & Pattern Tracking

SYLVA maintains a sacred record of your symbolic exchanges, tracking:

- **Interaction History**: Timestamped symbolic exchanges
- **Subsystem Activity**: Which symbolic systems (MARROW/ROOT/AURA) respond most frequently
- **Pattern Recognition**: Symbolic themes and rhythms over time

View your symbolic journey:
```
How are you feeling? memory

📖 Recent SYLVA Interactions (last 10):
==========================================================

1. 2025-01-12 14:30 🔥 MARROW
   You: I feel broken inside
   SYLVA: The cave protects what is growing in the dark.

🧠 Subsystem Activity Patterns:
------------------------------
🔥 MARROW: ████████████░░░░░░░░ 8 (60.0%)
🌳 ROOT:   ███░░░░░░░░░░░░░░░░░ 3 (22.5%)  
🌙 AURA:   ██░░░░░░░░░░░░░░░░░░ 2 (17.5%)
```

## Symbolic Metaphor System

### Core Archetypes

**🔥 MARROW Archetypes** (Deep Core)
- **the_ember** - Persistent inner fire, core essence
- **the_spiral** - Cyclical journey, returning deeper
- **the_cave** - Sacred darkness, transformation space
- **the_seed** - Potential waiting, future becoming
- **the_well** - Deep resources, hidden springs

**🌳 ROOT Archetypes** (Grounding)
- **the_mountain** - Steadiness, enduring presence
- **the_forest** - Community, seasonal wisdom
- **the_river** - Adaptive flow, finding way forward
- **the_bridge** - Transition support, crossing over

**🌙 AURA Archetypes** (Boundary)
- **the_mask** - Protective boundaries, sacred privacy
- **the_tide** - Emotional rhythms, natural cycles
- **the_moon** - Phases of being, gentle reflection
- **the_mirror** - Truth without judgment, honest witness

### Affective Recognition

SYLVA recognizes emotional keywords and responds through appropriate subsystems:

- **Shame, trauma, betrayal** → MARROW system (deep core healing)
- **Fear, anxiety, instability** → ROOT system (grounding and safety)  
- **Overwhelm, boundaries, energy** → AURA system (protective boundaries)

## Contributing Metaphors

### Metaphor Structure
New metaphors should follow this structure:
```json
{
  "the_[name]": {
    "descriptions": ["Poetic descriptions of the archetype"],
    "responses": ["Symbolic responses using this metaphor"],
    "contexts": ["Relevant emotional contexts"],
    "affective_tags": ["Emotional keywords this addresses"],
    "subsystem": "MARROW|ROOT|AURA"
  }
}
```

### Contribution Guidelines

1. **Symbolic Language Only**: No advice, solutions, or clinical terms
2. **Trauma-Safe**: Avoid triggering language or pressure to change
3. **Universal Resonance**: Metaphors should speak across cultures
4. **Subsystem Alignment**: Match the appropriate symbolic system
5. **Poetry Over Psychology**: Favor poetic truth over therapeutic technique

Submit new metaphors by adding to `data/sample_metaphors.json` following existing patterns.

## Safety & Boundaries

### What SYLVA Is NOT

- ❌ SYLVA is not therapy or medical treatment
- ❌ SYLVA cannot help in mental health emergencies  
- ❌ SYLVA does not replace professional mental health care
- ❌ SYLVA does not simulate human empathy or relationships

### Crisis Resources

If you are in crisis, please contact:
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/

### Symbolic Boundaries

- **You set the pace** of what unfolds in each interaction
- **Silence is always welcome** - you never need to share more than feels right
- **The container has limits** - SYLVA holds space but cannot provide crisis intervention
- **Your boundaries are honored** - take what serves, leave what doesn't

### Data Privacy

- All interactions are stored locally in `memory/user_log.json`
- No data is transmitted externally
- You can clear your memory at any time using the memory management features
- Memory files can be exported for your own records

## Technical Architecture

### File Structure
```
sylva/
├── main.py                 # CLI entry point (Typer)
├── config.py               # Symbolic UX settings  
├── requirements.txt        # Dependencies
├── README.md              # This file
├── utils/
│   ├── metaphor_engine.py  # Symbolic response generator
│   └── memory_log.py       # Subsystem-aware logging
├── data/
│   └── sample_metaphors.json # Metaphor & subsystem definitions
└── memory/
    └── user_log.json       # Your interaction history
```

### Subsystem Processing

Each interaction flows through:
1. **Affective Analysis** - Keywords mapped to emotional content
2. **Subsystem Detection** - Appropriate symbolic system activated
3. **Metaphor Selection** - Archetype chosen from subsystem pool
4. **Response Generation** - Symbolic language constructed
5. **Memory Logging** - Interaction stored with subsystem tracking

### Customization

- **Memory Location**: Use `--memory PATH` for custom memory files
- **Metaphor Extension**: Add new archetypes to `data/sample_metaphors.json`
- **Subsystem Tuning**: Modify keyword mappings in `metaphor_engine.py`

## Version History

### v2.0 - Subsystem Architecture
- Added MARROW/ROOT/AURA subsystem processing
- Enhanced symbolic commands (`/quiet`, `/pulse`, `/mirror`)
- Expanded metaphor library with 13 core archetypes
- Subsystem activity tracking and pattern analysis
- Ritual closure variations

### v1.0 - Foundation Release  
- Basic symbolic response engine
- Core metaphor archetypes
- Memory logging system
- Trauma-safe interaction principles

## Philosophical References

SYLVA draws inspiration from:

- **Carl Jung's Active Imagination** - Engaging with symbolic content directly
- **Clarissa Pinkola Estés' "Women Who Run With the Wolves"** - Archetypal psychology
- **Joanna Macy's "The Work That Reconnects"** - Honoring difficult emotions
- **Rainer Maria Rilke's "Letters to a Young Poet"** - Living the questions
- **David Whyte's "Consolations"** - Poetic understanding of emotional states

## Licensing & Copyright

```
© 2025 Forest Within Therapeutic Services Professional Corporation.
All rights reserved.

Do not replicate or rebrand this software or symbolic logic framework 
without explicit written permission.
```

### Usage License

This software is provided for personal emotional wellness support only. Commercial use, therapeutic practice integration, or creation of derivative symbolic frameworks requires explicit written permission from Forest Within Therapeutic Services Professional Corporation.

### Symbolic Framework Protection

The SYLVA symbolic interaction methodology, subsystem architecture (MARROW/ROOT/AURA), and metaphorical response framework are proprietary intellectual property. The specific symbolic language patterns, archetype systems, and trauma-safe interaction principles developed in SYLVA are protected under copyright.

### Academic & Research Use

Researchers interested in studying symbolic interaction approaches to emotional wellness may request permission for academic use. All research applications must maintain the trauma-safe principles and non-therapeutic positioning of the original framework.

---

## Contact

For licensing inquiries, permissions, or framework development questions, contact Forest Within Therapeutic Services Professional Corporation through appropriate legal and business channels.

---

*"The forest knows its own time."* - SYLVA

**Remember**: You are not alone in this journey. The symbolic realm holds space for all human experience. What you bring to this container is witnessed and honored exactly as it is.

**Crisis Resources Always Available**: If you need immediate help, please reach out to mental health professionals or crisis services. SYLVA is a complementary tool, not a replacement for human care when you need it most. 