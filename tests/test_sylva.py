#!/usr/bin/env python3
"""
Simple test script for SYLVA components.
Run this to verify that all components are working correctly.
"""

import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

def test_metaphor_engine():
    """Test the metaphor engine functionality."""
    print("Testing Metaphor Engine...")
    
    try:
        from utils.metaphor_engine import MetaphorEngine
        
        engine = MetaphorEngine()
        
        # Test basic response generation
        test_inputs = [
            "I'm feeling sad",
            "I'm so angry right now",
            "I'm anxious about everything",
            "I'm exhausted",
            "I feel lost"
        ]
        
        for test_input in test_inputs:
            response = engine.generate_response(test_input)
            print(f"  Input: '{test_input}'")
            print(f"  Response: '{response}'")
            print()
        
        # Test archetype listing
        archetypes = engine.list_archetypes()
        print(f"Available archetypes: {archetypes}")
        print()
        
        print("✅ Metaphor Engine test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Metaphor Engine test failed: {e}")
        return False

def test_memory_logger():
    """Test the memory logger functionality."""
    print("Testing Memory Logger...")
    
    try:
        from utils.memory_log import MemoryLogger
        
        # Test with temporary memory file
        test_memory_file = "test_memory.json"
        logger = MemoryLogger(test_memory_file)
        
        # Test logging interactions
        test_interactions = [
            ("I'm feeling sad", "The tide recedes, but it will return."),
            ("I'm angry", "The ember holds steady in the wind."),
            ("I'm anxious", "The spiral has its own wisdom.")
        ]
        
        for user_input, sylva_response in test_interactions:
            logger.log_interaction(user_input, sylva_response, "ROOT")
        
        # Test interaction count
        count = logger.get_interaction_count()
        print(f"  Logged {count} interactions")
        
        # Test recent interactions
        recent = logger.get_recent_interactions(2)
        print(f"  Recent interactions: {len(recent)}")
        
        # Clean up test file
        import os
        if os.path.exists(test_memory_file):
            os.remove(test_memory_file)
        
        print("✅ Memory Logger test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Memory Logger test failed: {e}")
        return False

def test_config():
    """Test the configuration system."""
    print("Testing Configuration...")
    
    try:
        from config import SYLVA_CONFIG, get_config, get_archetype_config
        
        # Test basic config access
        version = get_config("version")
        print(f"  SYLVA version: {version}")
        
        # Test archetype config
        ember_config = get_archetype_config("the_ember")
        print(f"  Ember archetype color: {ember_config.get('color', 'unknown')}")
        
        # Test required config keys
        required_keys = ["version", "enable_rituals", "max_response_length"]
        for key in required_keys:
            if key not in SYLVA_CONFIG:
                raise ValueError(f"Missing required config key: {key}")
        
        print("✅ Configuration test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Running SYLVA Component Tests")
    print("=" * 50)
    
    tests = [
        test_config,
        test_metaphor_engine,
        test_memory_logger
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! SYLVA is ready to use.")
        print("\nTo start SYLVA, run: python main.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 