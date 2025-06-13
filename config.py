"""
Configuration settings for SYLVA
Symbolic UX settings and basic app configuration.
"""

from typing import Dict, Any

# Main SYLVA configuration
SYLVA_CONFIG = {
    # Symbolic UX settings
    "enable_rituals": True,  # Enable ritual-like interaction patterns
    "max_response_length": 200,  # Maximum length of SYLVA responses
    "enable_archetype_exploration": True,  # Allow users to explore archetypes
    "use_emoji": True,  # Use emoji in responses and interface
    "enable_memory_reflection": True,  # Allow users to reflect on past interactions
    
    # Interaction settings
    "default_memory_limit": 10,  # Default number of interactions to show
    "max_memory_entries": 1000,  # Maximum interactions to keep in memory
    "session_timeout_minutes": 30,  # Session timeout for memory grouping
    
    # Symbolic language settings
    "preferred_archetypes": [
        "the_ember",
        "the_spiral", 
        "the_tide",
        "the_mask",
        "the_forest",
        "the_mountain",
        "the_river",
        "the_moon"
    ],
    
    # Trauma-safe settings
    "avoid_advice_keywords": [
        "should", "must", "need to", "have to", "ought to",
        "try", "just", "simply", "easily", "quickly"
    ],
    
    "avoid_empathy_simulation": [
        "I understand", "I feel you", "I know how you feel",
        "I'm sorry you're going through this", "That must be hard"
    ],
    
    # Response generation settings
    "archetype_response_probability": 0.7,  # 70% chance to use archetype-specific responses
    "universal_response_probability": 0.3,  # 30% chance to use universal responses
    
    # Memory and logging settings
    "memory_file": "memory/user_log.json",
    "enable_interaction_logging": True,
    "log_timestamps": True,
    "log_session_ids": True,
    
    # Display settings
    "welcome_message": True,
    "farewell_message": True,
    "help_available": True,
    "memory_display_available": True,
    
    # Safety and boundaries
    "emergency_keywords": [
        "suicide", "kill myself", "want to die", "end it all",
        "self-harm", "cut myself", "overdose"
    ],
    
    "crisis_response": "If you're in crisis, please reach out to a crisis helpline or mental health professional. You are not alone, and help is available.",
    
    # File paths and directories
    "data_directory": "data",
    "memory_directory": "memory",
    "utils_directory": "utils",
    
    # Version and metadata
    "version": "1.0.0",
    "description": "Symbolic Emotional Wellness Assistant - A trauma-safe, metaphor-driven CLI",
    "author": "SYLVA Project",
    "license": "MIT"
}

# Archetype-specific configurations
ARCHETYPE_CONFIG = {
    "the_ember": {
        "color": "red",
        "element": "fire",
        "time_of_day": "night",
        "season": "winter"
    },
    "the_spiral": {
        "color": "purple",
        "element": "air",
        "time_of_day": "twilight",
        "season": "autumn"
    },
    "the_tide": {
        "color": "blue",
        "element": "water",
        "time_of_day": "dawn",
        "season": "spring"
    },
    "the_mask": {
        "color": "silver",
        "element": "metal",
        "time_of_day": "day",
        "season": "summer"
    },
    "the_forest": {
        "color": "green",
        "element": "earth",
        "time_of_day": "afternoon",
        "season": "spring"
    },
    "the_mountain": {
        "color": "gray",
        "element": "stone",
        "time_of_day": "sunrise",
        "season": "winter"
    },
    "the_river": {
        "color": "cyan",
        "element": "water",
        "time_of_day": "morning",
        "season": "summer"
    },
    "the_moon": {
        "color": "white",
        "element": "light",
        "time_of_day": "night",
        "season": "autumn"
    }
}

# Emotional keyword mappings for enhanced detection
EMOTION_KEYWORDS = {
    "sad": ["sad", "depressed", "down", "blue", "melancholy", "grief", "loss"],
    "angry": ["angry", "mad", "furious", "irritated", "frustrated", "rage"],
    "anxious": ["anxious", "worried", "nervous", "scared", "afraid", "panicked"],
    "tired": ["tired", "exhausted", "weary", "fatigued", "drained", "burned out"],
    "lost": ["lost", "confused", "uncertain", "directionless", "adrift"],
    "overwhelmed": ["overwhelmed", "swamped", "drowning", "buried", "crushed"],
    "hopeless": ["hopeless", "despair", "helpless", "powerless", "defeated"],
    "stuck": ["stuck", "trapped", "paralyzed", "frozen", "immobile"],
    "alone": ["alone", "lonely", "isolated", "abandoned", "separated"],
    "scared": ["scared", "terrified", "frightened", "fearful", "threatened"]
}

def get_config(key: str, default: Any = None) -> Any:
    """
    Get a configuration value by key.
    
    Args:
        key: Configuration key to retrieve
        default: Default value if key not found
        
    Returns:
        Configuration value or default
    """
    return SYLVA_CONFIG.get(key, default)

def get_archetype_config(archetype: str) -> Dict[str, Any]:
    """
    Get configuration for a specific archetype.
    
    Args:
        archetype: Name of the archetype
        
    Returns:
        Archetype configuration dictionary
    """
    return ARCHETYPE_CONFIG.get(archetype, {})

def get_emotion_keywords(emotion: str) -> list:
    """
    Get keywords associated with a specific emotion.
    
    Args:
        emotion: Name of the emotion
        
    Returns:
        List of keywords for the emotion
    """
    return EMOTION_KEYWORDS.get(emotion, []) 