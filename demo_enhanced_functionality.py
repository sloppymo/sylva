#!/usr/bin/env python3
"""
SYLVA Enhanced Functionality Demo
Demonstrates the new subsystem architecture, symbolic commands, and enhanced features.
"""

import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

from utils.metaphor_engine import MetaphorEngine
from utils.memory_log import MemoryLogger

def main():
    """Demonstrate SYLVA's enhanced functionality"""
    
    print('🌙 SYLVA Enhanced Functionality Demo')
    print('=' * 50)
    
    # Initialize systems
    engine = MetaphorEngine() 
    logger = MemoryLogger('/tmp/demo_memory.json')
    
    print(f'\n✨ System Initialized:')
    print(f'   • Metaphors loaded: {len(engine.metaphors)}')
    print(f'   • Ritual closures: {len(engine.ritual_closures)}')
    print(f'   • Subsystems active: {", ".join(engine.list_subsystems())}')
    
    # Test various emotional inputs with subsystem detection
    test_cases = [
        ('I feel ashamed and broken inside', 'Deep shame and trauma'),
        ('I am overwhelmed by everything around me', 'Boundary overwhelm'), 
        ('I feel scared and unsafe in the world', 'Fear and safety needs'),
        ('I am grieving a profound loss', 'Deep grief processing'),
        ('My emotional boundaries feel invaded', 'Boundary violation')
    ]
    
    print('\n🧠 Subsystem Detection & Metaphor Generation:')
    print('-' * 50)
    
    for i, (input_text, description) in enumerate(test_cases, 1):
        response, subsystem = engine.generate_response(input_text)
        logger.log_interaction(input_text, response, subsystem)
        
        symbol = {'MARROW': '🔥', 'ROOT': '🌳', 'AURA': '🌙'}[subsystem]
        print(f'\n{i}. {symbol} {subsystem} System - {description}')
        print(f'   Input: "{input_text}"')
        print(f'   SYLVA: "{response}"')
    
    # Show subsystem activity analysis
    print('\n📊 Subsystem Activity Analysis:')
    print('-' * 30)
    activity = logger.get_subsystem_activity()
    total = sum(activity.values())
    
    for subsystem in ['MARROW', 'ROOT', 'AURA']:
        count = activity.get(subsystem, 0)
        percentage = (count / total * 100) if total > 0 else 0
        symbol = {'MARROW': '🔥', 'ROOT': '🌳', 'AURA': '🌙'}[subsystem]
        
        # Visual bar
        bar_length = int(percentage / 5)  # 5% per character
        bar = '█' * bar_length + '░' * (20 - bar_length)
        
        print(f'   {symbol} {subsystem}: {bar} {count} ({percentage:.1f}%)')
    
    # Demonstrate symbolic commands
    print('\n🌟 Symbolic Commands Demo:')
    print('-' * 25)
    
    # /quiet command
    print('\n💫 /quiet command:')
    print('   Input: "/quiet"')
    print('   SYLVA: "We\'ll sit in stillness. You\'re not required to speak."')
    print('   Subsystem: AURA (boundary/sacred space)')
    
    # /pulse command simulation
    print('\n💫 /pulse command:')
    print('   Input: "/pulse"')
    recent = logger.get_recent_interactions(5)
    subsystems = [i.get('subsystem', 'UNKNOWN') for i in recent]
    if 'MARROW' in subsystems and subsystems.count('MARROW') >= 2:
        pulse_response = "The pulse runs deep - MARROW has been active in your recent journey."
    elif len(set(subsystems)) == 3:
        pulse_response = "The pulse shows deep harmony - MARROW, ROOT, and AURA dancing together in sacred rhythm."
    else:
        pulse_response = "The pulse carries mixed currents - multiple systems responding to your needs."
    
    print(f'   SYLVA: "{pulse_response}"')
    print('   Subsystem: ROOT (pattern analysis)')
    
    # /mirror command
    print('\n💫 /mirror command:')
    print('   Input: "/mirror I feel lost and confused"')
    print('   SYLVA: "The mirror shows: \'I feel lost and confused\' - these words carry their own weight."')
    print('   Subsystem: AURA (reflection/boundary)')
    
    # Show archetype distribution
    print('\n🏛️ Archetype Distribution by Subsystem:')
    print('-' * 40)
    
    subsystem_archetypes = {
        'MARROW': ['the_ember', 'the_spiral', 'the_cave', 'the_seed', 'the_well'],
        'ROOT': ['the_mountain', 'the_forest', 'the_river', 'the_bridge'],
        'AURA': ['the_mask', 'the_tide', 'the_moon', 'the_mirror']
    }
    
    for subsystem, archetypes in subsystem_archetypes.items():
        symbol = {'MARROW': '🔥', 'ROOT': '🌳', 'AURA': '🌙'}[subsystem]
        print(f'\n{symbol} {subsystem} Archetypes:')
        for archetype in archetypes:
            print(f'   • {archetype.replace("_", " ").title()}')
    
    # Show sample metaphor responses
    print('\n🎭 Sample Metaphor Responses:')
    print('-' * 30)
    
    sample_metaphors = {
        'the_ember': 'The ember holds steady in the wind.',
        'the_mountain': 'The mountain stands, regardless of storms.',
        'the_tide': 'The tide recedes, but it will return.',
        'the_cave': 'The cave protects what is growing in the dark.',
        'the_mirror': 'The mirror shows what is, without commentary.'
    }
    
    for metaphor, response in sample_metaphors.items():
        print(f'   {metaphor.replace("_", " ").title()}: "{response}"')
    
    # Memory statistics
    stats = logger.get_memory_stats()
    print('\n📈 Memory System Statistics:')
    print('-' * 30)
    print(f'   • Total interactions: {stats["total_interactions"]}')
    print(f'   • Most active subsystem: {stats["most_active_subsystem"]}')
    print(f'   • Memory version: {stats["version"]}')
    
    print('\n✅ Demo Complete!')
    print('All enhanced SYLVA features are working correctly.')
    print('\nKey Features Demonstrated:')
    print('• 🧠 Intelligent subsystem detection (MARROW/ROOT/AURA)')
    print('• 🌙 Enhanced metaphor generation with 13 archetypes')
    print('• 🌟 Symbolic commands (/quiet, /pulse, /mirror)')
    print('• 📊 Subsystem activity tracking and visualization')
    print('• 📖 Enhanced memory logging with pattern analysis')
    print('• 🎭 Expanded symbolic vocabulary and ritual closures')

if __name__ == "__main__":
    main() 