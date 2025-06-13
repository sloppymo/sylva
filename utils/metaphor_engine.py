"""
Metaphor Engine for SYLVA
Generates symbolic, archetype-based responses to emotional input with subsystem tracking.

This engine avoids advice-giving, cheerleading, or simulated empathy.
Instead, it contains emotions using metaphors and symbolic language.
Subsystems: MARROW (deep core), ROOT (grounding), AURA (protective boundary)
"""

import random
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime

class MetaphorEngine:
    """
    Generates symbolic responses using metaphors, archetypes, and subsystem awareness.
    Trauma-safe approach: contains rather than advises, honors rather than fixes.
    """
    
    def __init__(self):
        """Initialize the metaphor engine with symbolic archetypes and subsystem mapping."""
        self.load_metaphor_data()
        self.init_subsystem_mapping()
        self.init_ritual_closures()
        
    def load_metaphor_data(self):
        """Load metaphor data from JSON file."""
        data_path = Path(__file__).parent.parent / "data" / "sample_metaphors.json"
        
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.metaphors = data.get("metaphors", {})
                self.universal_responses = data.get("universal_responses", [])
                self.ritual_phrases = data.get("ritual_phrases", [])
                self.safety_responses = data.get("safety_responses", {})
        except FileNotFoundError:
            # Fallback to hardcoded metaphors if file not found
            self.init_fallback_metaphors()
    
    def init_fallback_metaphors(self):
        """Initialize fallback metaphors if JSON file unavailable."""
        self.metaphors = {
            "the_ember": {
                "responses": [
                    "The ember holds steady in the wind.",
                    "You carry the ember within you.",
                    "The ember knows its own rhythm."
                ],
                "subsystem": "MARROW"
            }
        }
        self.universal_responses = [
            "You are here, and that is enough.",
            "The moment holds what it holds."
        ]
        self.ritual_phrases = []
        self.safety_responses = {}
    
    def init_subsystem_mapping(self):
        """Initialize emotional keyword to subsystem mapping."""
        # MARROW - Deep core processing, trauma, core wounds, essence
        self.marrow_keywords = [
            "shame", "trauma", "betrayal", "abandoned", "worthless", "broken",
            "hollow", "empty", "core", "essence", "soul", "deep", "profound",
            "shattered", "wounded", "raw", "exposed", "vulnerable", "naked"
        ]
        
        # ROOT - Grounding, stability, basic needs, safety, foundation
        self.root_keywords = [
            "unstable", "groundless", "floating", "disconnected", "untethered",
            "safe", "secure", "stable", "grounded", "rooted", "foundation",
            "basic", "fundamental", "survival", "shelter", "home", "belonging",
            "steady", "solid", "reliable", "trust", "dependable"
        ]
        
        # AURA - Boundaries, protection, interface with world, energy
        self.aura_keywords = [
            "boundaries", "overwhelmed", "invaded", "crowded", "suffocated",
            "protected", "shielded", "space", "distance", "buffer", "barrier",
            "energy", "drained", "recharged", "sensitive", "permeable",
            "defended", "guarded", "open", "closed", "filtered"
        ]
        
        # Expanded affective keyword mapping with subsystem awareness
        self.emotion_subsystem_map = {
            # MARROW emotions - core wounds and essence
            "shame": {"keywords": ["shame", "humiliated", "disgrace", "worthless"], "subsystem": "MARROW"},
            "betrayal": {"keywords": ["betrayed", "deceived", "lied to", "abandoned"], "subsystem": "MARROW"}, 
            "grief": {"keywords": ["grief", "loss", "mourning", "bereaved"], "subsystem": "MARROW"},
            "despair": {"keywords": ["despair", "hopeless", "devastated"], "subsystem": "MARROW"},
            
            # ROOT emotions - stability and grounding
            "fear": {"keywords": ["fear", "afraid", "scared", "terrified", "panic"], "subsystem": "ROOT"},
            "anxiety": {"keywords": ["anxious", "worried", "nervous", "uneasy"], "subsystem": "ROOT"},
            "insecurity": {"keywords": ["insecure", "uncertain", "unstable"], "subsystem": "ROOT"},
            "safety": {"keywords": ["safe", "secure", "protected", "calm"], "subsystem": "ROOT"},
            
            # AURA emotions - boundaries and energy
            "overwhelmed": {"keywords": ["overwhelmed", "flooded", "too much"], "subsystem": "AURA"},
            "invaded": {"keywords": ["invaded", "intruded", "violated"], "subsystem": "AURA"},
            "drained": {"keywords": ["drained", "exhausted", "depleted"], "subsystem": "AURA"},
            "energized": {"keywords": ["energized", "vibrant", "alive"], "subsystem": "AURA"},
            
            # Multi-subsystem emotions
            "anger": {"keywords": ["angry", "rage", "furious", "mad"], "subsystem": "MARROW"},
            "sad": {"keywords": ["sad", "depressed", "down", "melancholy"], "subsystem": "MARROW"},
            "tired": {"keywords": ["tired", "weary", "fatigued"], "subsystem": "AURA"},
            "confused": {"keywords": ["confused", "lost", "directionless"], "subsystem": "ROOT"},
            "alone": {"keywords": ["alone", "lonely", "isolated"], "subsystem": "AURA"}
        }
    
    def init_ritual_closures(self):
        """Initialize randomized ritual closure lines."""
        self.ritual_closures = [
            "That's enough for now.",
            "We'll build from that ember.",
            "Let it be named and left.",
            "The container holds what needs holding.",
            "The sacred pause honors your words.",
            "What has been spoken has been witnessed.",
            "The circle completes itself.",
            "The ritual of naming draws to rest.",
            "Let the echo settle into silence.",
            "The moment finds its own completion.",
            "What is held is held with reverence.",
            "The speaking and the silence are both sacred.",
            "The thread of connection remains.",
            "What needed voice has found voice.",
            "The container remains, even as words settle."
        ]
    
    def detect_subsystem(self, text: str) -> str:
        """
        Detect which subsystem should respond based on emotional content.
        
        Args:
            text: User's emotional expression
            
        Returns:
            Subsystem name (MARROW, ROOT, or AURA)
        """
        text_lower = text.lower()
        
        # Check for direct keyword matches first
        marrow_matches = sum(1 for keyword in self.marrow_keywords if keyword in text_lower)
        root_matches = sum(1 for keyword in self.root_keywords if keyword in text_lower)
        aura_matches = sum(1 for keyword in self.aura_keywords if keyword in text_lower)
        
        # Check emotion-based mapping
        emotion_matches = {"MARROW": 0, "ROOT": 0, "AURA": 0}
        
        for emotion, data in self.emotion_subsystem_map.items():
            for keyword in data["keywords"]:
                if keyword in text_lower:
                    emotion_matches[data["subsystem"]] += 1
        
        # Combine direct and emotion-based matches
        total_scores = {
            "MARROW": marrow_matches + emotion_matches["MARROW"],
            "ROOT": root_matches + emotion_matches["ROOT"], 
            "AURA": aura_matches + emotion_matches["AURA"]
        }
        
        # Return subsystem with highest score, with tie-breaking preference
        max_score = max(total_scores.values())
        if max_score == 0:
            # No clear match - default to ROOT for grounding
            return "ROOT"
        
        # If tie, prefer in order: MARROW (depth), ROOT (stability), AURA (boundary)
        if total_scores["MARROW"] == max_score:
            return "MARROW"
        elif total_scores["ROOT"] == max_score:
            return "ROOT"
        else:
            return "AURA"
    
    def select_metaphor_for_subsystem(self, subsystem: str, text: str) -> Dict:
        """
        Select appropriate metaphor based on subsystem and content.
        
        Args:
            subsystem: The responding subsystem (MARROW/ROOT/AURA)
            text: User's emotional expression
            
        Returns:
            Selected metaphor data
        """
        # Map subsystems to preferred archetypes
        subsystem_archetypes = {
            "MARROW": ["the_ember", "the_spiral", "the_moon", "the_forest"],
            "ROOT": ["the_mountain", "the_forest", "the_river", "the_tide"],
            "AURA": ["the_mask", "the_tide", "the_moon", "the_river"]
        }
        
        # Get archetypes for this subsystem
        preferred_archetypes = subsystem_archetypes.get(subsystem, list(self.metaphors.keys()))
        
        # Filter available metaphors by preferred archetypes
        available_metaphors = {
            name: data for name, data in self.metaphors.items() 
            if name in preferred_archetypes
        }
        
        if not available_metaphors:
            # Fallback to any available metaphor
            available_metaphors = self.metaphors
        
        # Select a metaphor
        metaphor_name = random.choice(list(available_metaphors.keys()))
        return {
            "name": metaphor_name,
            "data": available_metaphors[metaphor_name]
        }
    
    def construct_subsystem_response(
        self, metaphor: Dict, subsystem: str, user_input: str
    ) -> str:
        """
        Construct a response incorporating subsystem awareness.
        
        Args:
            metaphor: Selected metaphor data
            subsystem: Active subsystem
            user_input: Original user input
            
        Returns:
            Symbolic response string
        """
        # Get base response from metaphor
        metaphor_data = metaphor["data"]
        
        # 70% chance for metaphor-specific response, 30% for universal
        if random.random() < 0.7 and "responses" in metaphor_data:
            base_response = random.choice(metaphor_data["responses"])
        else:
            base_response = random.choice(self.universal_responses)
        
        # Add subtle subsystem context (optional, 30% chance)
        if random.random() < 0.3:
            subsystem_context = {
                "MARROW": " The deep systems recognize this.",
                "ROOT": " The foundation holds steady.",
                "AURA": " The boundary honors what is needed."
            }
            base_response += subsystem_context.get(subsystem, "")
        
        return base_response
    
    def append_ritual_closure(self, response: str) -> str:
        """
        Ensure response ends with one of the three canonical ritual closures.
        
        Args:
            response: Base response
            
        Returns:
            Response with guaranteed ritual closure
        """
        # The three canonical ritual closures
        canonical_closures = [
            "That's enough for now.",
            "We'll build from that ember.",
            "Let it be named and left."
        ]
        
        # Check if response already ends with one of the canonical closures
        response_stripped = response.strip()
        if not any(response_stripped.endswith(closure) for closure in canonical_closures):
            closure = random.choice(canonical_closures)
            return response_stripped + " " + closure
        
        return response
    
    def generate_response(self, user_input: str) -> Tuple[str, str]:
        """
        Generate a symbolic response to the user's emotional input.
        
        Args:
            user_input: The user's emotional expression
            
        Returns:
            Tuple of (symbolic response, active subsystem)
        """
        # Detect which subsystem should respond
        active_subsystem = self.detect_subsystem(user_input)
        
        # Select appropriate metaphor for this subsystem
        selected_metaphor = self.select_metaphor_for_subsystem(active_subsystem, user_input)
        
        # Construct the symbolic response
        response = self.construct_subsystem_response(
            selected_metaphor, active_subsystem, user_input
        )
        
        # Ensure ritual closure is present
        final_response = self.append_ritual_closure(response)
        
        return final_response, active_subsystem
    
    def get_subsystem_info(self, subsystem: str) -> Dict[str, str]:
        """
        Get information about a specific subsystem.
        
        Args:
            subsystem: Name of subsystem (MARROW/ROOT/AURA)
            
        Returns:
            Subsystem information dictionary
        """
        subsystem_info = {
            "MARROW": {
                "description": "Deep core processing - essence, wounds, and transformation",
                "focus": "Core wounds, trauma, essence, identity, profound change",
                "approach": "Deep witnessing, holding space for core truth"
            },
            "ROOT": {
                "description": "Grounding and stability - foundation, safety, basic needs",
                "focus": "Safety, stability, grounding, basic needs, survival, trust",
                "approach": "Providing stability, ensuring safety, grounding techniques"
            },
            "AURA": {
                "description": "Protective boundary - energy, interface with world, protection",
                "focus": "Boundaries, energy, protection, overwhelm, sensitivity",
                "approach": "Boundary work, energy management, protective strategies"
            }
        }
        
        return subsystem_info.get(subsystem, {})
    
    def get_metaphor_info(self, metaphor_name: str) -> Optional[Dict]:
        """
        Get information about a specific metaphor archetype.
        
        Args:
            metaphor_name: Name of the metaphor archetype
            
        Returns:
            Metaphor information dictionary
        """
        return self.metaphors.get(metaphor_name)
    
    def list_archetypes(self) -> List[str]:
        """
        Return a list of all available metaphor archetypes.
        
        Returns:
            List of archetype names
        """
        return list(self.metaphors.keys())
    
    def list_subsystems(self) -> List[str]:
        """
        Return a list of all subsystems.
        
        Returns:
            List of subsystem names
        """
        return ["MARROW", "ROOT", "AURA"] 