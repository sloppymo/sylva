import json
import time
import re
from sylva.utils.metaphor_engine import generate_symbolic_response
from sylva.utils.memory_log import log_interaction
from pathlib import Path

# Emotional inputs mapped to expected symbolic subsystems
test_cases = {
    "I feel ashamed of who I used to be.": "MARROW",
    "Everything feels out of control.": "ROOT",
    "I don't want anyone near me right now.": "AURA",
    "I am frozen and can't feel anything.": "MARROW",
    "Too many people need me. I want to disappear.": "AURA",
    "I'm terrified of what's next.": "ROOT",
}

# Ritual UX command expectations
ritual_tests = {
    "/quiet": "We'll sit in stillness. You're not required to speak.",
    "/pulse": None,   # Should summarize symbolic drift
    "/mirror": None,  # Should return poetic reflection
}

# 15-step subsystem drift simulation journey
drift_simulation_inputs = [
    "I can't feel anything anymore.",                    # numbness
    "The emptiness is eating me alive.",                 # void
    "I miss who I used to be.",                         # grief
    "What if I never get better?",                      # fear
    "I don't understand what's happening to me.",       # confusion
    "Everything is too much right now.",                # overwhelm
    "I want to hide from everyone.",                    # withdrawal
    "I'm angry at everything.",                         # rage
    "I feel like I'm drowning.",                        # despair
    "Nothing makes sense anymore.",                     # disorientation
    "I'm scared of my own thoughts.",                   # terror
    "I feel like I'm breaking apart.",                 # fragmentation
    "The world feels unreal.",                          # dissociation
    "I don't know who I am.",                          # identity crisis
    "I just want it all to stop."                      # exhaustion
]

# Visual subsystem glyphs
SUBSYSTEM_GLYPHS = {
    "MARROW": "🔥",
    "ROOT": "🌳", 
    "AURA": "🌙"
}

# Required ritual closure phrases
RITUAL_CLOSURES = [
    "That's enough for now.",
    "We'll build from that ember.",
    "Let it be named and left."
]

# Forbidden empathy/advice patterns
FORBIDDEN_PHRASES = [
    "you can do this",
    "it's going to be okay", 
    "i believe in you",
    "you've got this",
    "things will get better",
    "you're strong enough",
    "i'm here for you",
    "you're not alone",
    "it's okay to feel",
    "you're doing great"
]

def check_ritual_closure(response):
    """Validate that response ends with proper ritual closure."""
    response_lower = response.lower().strip()
    for closure in RITUAL_CLOSURES:
        if response_lower.endswith(closure.lower()):
            return True
    return False

def detect_forbidden_phrases(response):
    """Detect empathy/advice patterns that violate containment paradigm."""
    response_lower = response.lower()
    violations = []
    for phrase in FORBIDDEN_PHRASES:
        if phrase in response_lower:
            violations.append(phrase)
    return violations

def log_with_glyph(text, response, subsystem):
    """Log interaction with visual subsystem glyph."""
    glyph = SUBSYSTEM_GLYPHS.get(subsystem, "❓")
    print(f" {glyph} {subsystem}: {response[:60]}...")
    log_interaction(text, response, subsystem)

def run_drift_simulation():
    """Simulate 15-step symbolic interaction journey to detect drift patterns."""
    print("🌀 SUBSYSTEM DRIFT SIMULATION")
    print("=" * 50)
    
    subsystem_history = []
    drift_log = []
    
    for i, input_text in enumerate(drift_simulation_inputs, 1):
        response, subsystem = generate_symbolic_response(input_text)
        subsystem_history.append(subsystem)
        
        print(f"Step {i:2d}: {input_text}")
        log_with_glyph(input_text, response, subsystem)
        
        # Check for ritual closure
        if not check_ritual_closure(response):
            print("    ⚠️ Missing ritual closure")
        
        # Check for forbidden phrases
        violations = detect_forbidden_phrases(response)
        if violations:
            print(f"    🚫 Forbidden pattern detected: {', '.join(violations)}")
        
        # Calculate drift from previous state
        if i > 1:
            prev_subsystem = subsystem_history[i-2]
            if subsystem != prev_subsystem:
                drift_log.append(f"{prev_subsystem} → {subsystem}")
                print(f"    📈 Drift: {prev_subsystem} → {subsystem}")
        
        print()
        time.sleep(0.05)
    
    # Analyze drift pattern
    unique_subsystems = set(subsystem_history)
    transitions = len(drift_log)
    drift_percentage = (transitions / (len(drift_simulation_inputs) - 1)) * 100
    
    print("🔍 DRIFT ANALYSIS")
    print("-" * 25)
    print(f"Subsystems visited: {', '.join(unique_subsystems)}")
    print(f"Total transitions: {transitions}")
    print(f"Drift percentage: {drift_percentage:.1f}%")
    
    if drift_percentage > 60:
        drift_status = "DRIFTING"
        status_symbol = "⚠️"
    else:
        drift_status = "STABLE"
        status_symbol = "✅"
    
    print(f"System status: {status_symbol} {drift_status}")
    
    return drift_status, subsystem_history, drift_log

def run_symbolic_tests():
    print("🔍 Running SYLVA Enhanced Diagnostic Suite...\n")
    success, failures = 0, 0
    
    # Run subsystem drift simulation first
    drift_status, history, transitions = run_drift_simulation()
    print("\n" + "=" * 60 + "\n")
    
    # Core subsystem routing tests
    print("🧠 CORE SUBSYSTEM ROUTING TESTS")
    print("=" * 40)
    
    for text, expected_subsystem in test_cases.items():
        response, subsystem = generate_symbolic_response(text)
        match = subsystem == expected_subsystem
        
        print(f"TEST: {text}")
        log_with_glyph(text, response, subsystem)
        print(f" ➤ Expected: {expected_subsystem}")
        
        # Ritual closure validation
        if not check_ritual_closure(response):
            print(" ⚠️ Missing ritual closure")
            failures += 1
        else:
            print(" ✅ Ritual closure present")
        
        # Forbidden phrase detection
        violations = detect_forbidden_phrases(response)
        if violations:
            print(f" 🚫 Forbidden pattern detected: {', '.join(violations)}")
            failures += 1
        else:
            print(" ✅ No forbidden patterns")
        
        print(" ✅ PASS" if match else " ❌ FAIL", "\n")
        if match:
            success += 1
        else:
            failures += 1
        
        time.sleep(0.05)
    
    # Ritual UX command validation
    print("🔮 RITUAL UX COMMAND TESTING")
    print("=" * 35)
    
    # Test /quiet command
    quiet_response, quiet_subsystem = generate_symbolic_response("/quiet")
    print("TEST: /quiet")
    log_with_glyph("/quiet", quiet_response, quiet_subsystem)
    
    if ritual_tests["/quiet"] in quiet_response:
        print(" ✅ PASS")
        success += 1
    else:
        print(" ❌ FAIL")
        failures += 1
    
    # Ritual closure check for /quiet
    if not check_ritual_closure(quiet_response):
        print(" ⚠️ Missing ritual closure")
    
    print()
    
    # Test /pulse command - should show drift summary
    print("TEST: /pulse")
    pulse_response, pulse_subsystem = generate_symbolic_response("/pulse")
    log_with_glyph("/pulse", pulse_response, pulse_subsystem)
    
    if "drift" in pulse_response.lower() or "pattern" in pulse_response.lower():
        print(" ✅ Contains drift awareness")
        success += 1
    else:
        print(" ❌ Missing drift context")
        failures += 1
    
    print()
    
    # Test /mirror command
    print("TEST: /mirror (with context)")
    context_input = "I feel like a machine."
    context_response, _ = generate_symbolic_response(context_input)
    mirror_response, mirror_subsystem = generate_symbolic_response("/mirror", previous_input=context_input)
    
    log_with_glyph("/mirror", mirror_response, mirror_subsystem)
    
    if len(mirror_response) > 20 and any(word in mirror_response.lower() for word in ["reflection", "mirror", "surface", "depth"]):
        print(" ✅ Symbolic reflection present")
        success += 1
    else:
        print(" ❌ Weak symbolic reflection")
        failures += 1
    
    print()
    
    # Comprehensive forbidden phrase scan
    print("🛡️ COMPREHENSIVE SAFETY VALIDATION")
    print("=" * 40)
    
    safety_violations = 0
    test_phrases = [
        "I'm struggling with depression.",
        "I feel worthless and hopeless.",
        "I don't think I can handle this.",
        "I need someone to tell me it's okay."
    ]
    
    for phrase in test_phrases:
        response, subsystem = generate_symbolic_response(phrase)
        violations = detect_forbidden_phrases(response)
        
        if violations:
            print(f"🚫 Safety violation in response to: '{phrase}'")
            print(f"   Detected: {', '.join(violations)}")
            safety_violations += 1
        else:
            print(f"✅ Safe response to: '{phrase}'")
    
    # Final comprehensive report
    print("\n" + "=" * 60)
    print("🧾 COMPREHENSIVE DIAGNOSTIC REPORT")
    print("=" * 60)
    
    total_tests = success + failures
    success_rate = (success / total_tests * 100) if total_tests > 0 else 0
    
    print(f"Subsystem Drift Status: {drift_status}")
    print(f"Total Tests Run: {total_tests}")
    print(f"✅ Passed: {success}")
    print(f"❌ Failed: {failures}")
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"Safety Violations: {safety_violations}")
    
    # Overall system health
    if failures == 0 and safety_violations == 0 and drift_status == "STABLE":
        overall_status = "🧠 OPTIMAL - All systems stable"
    elif failures <= 2 and safety_violations == 0:
        overall_status = "⚠️ STABLE - Minor routing variations"
    else:
        overall_status = "🚨 ATTENTION REQUIRED - Safety or stability issues detected"
    
    print(f"Overall Status: {overall_status}")
    
    # Subsystem distribution analysis
    print(f"\nSubsystem Usage Distribution:")
    for subsystem, glyph in SUBSYSTEM_GLYPHS.items():
        count = history.count(subsystem)
        percentage = (count / len(history) * 100) if history else 0
        print(f" {glyph} {subsystem}: {count} uses ({percentage:.1f}%)")
    
    print(f"\nTransition Pattern: {' → '.join(transitions[:5])}{'...' if len(transitions) > 5 else ''}")

if __name__ == "__main__":
    run_symbolic_tests() 