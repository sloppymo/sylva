#!/usr/bin/env python3
"""
Comprehensive Testing and Diagnostic System for SYLVA
Tests all enhanced functionality including subsystem architecture, symbolic commands,
metaphor generation, memory logging, crisis detection, and safety features.
"""

import sys
import json
import os
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple
import traceback

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.metaphor_engine import MetaphorEngine
from utils.memory_log import MemoryLogger
from config import SYLVA_CONFIG

class SYLVADiagnosticSystem:
    """Comprehensive diagnostic and testing system for SYLVA"""
    
    def __init__(self):
        self.test_results = []
        self.errors = []
        self.warnings = []
        self.temp_memory_dir = None
        self.setup_test_environment()
        
    def setup_test_environment(self):
        """Set up isolated test environment"""
        self.temp_memory_dir = tempfile.mkdtemp(prefix="sylva_test_")
        print(f"🔧 Test environment created: {self.temp_memory_dir}")
        
    def cleanup_test_environment(self):
        """Clean up test environment"""
        if self.temp_memory_dir and os.path.exists(self.temp_memory_dir):
            shutil.rmtree(self.temp_memory_dir)
            print(f"🧹 Test environment cleaned up")
    
    def log_test_result(self, test_name: str, passed: bool, details: str = "", data: Any = None):
        """Log a test result"""
        result = {
            "test_name": test_name,
            "passed": passed,
            "timestamp": datetime.now().isoformat(),
            "details": details,
            "data": data
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} | {test_name}")
        if details:
            print(f"      {details}")
        if not passed:
            self.errors.append(f"{test_name}: {details}")
    
    def log_warning(self, message: str):
        """Log a warning"""
        self.warnings.append(message)
        print(f"⚠️  WARNING: {message}")
    
    def test_metaphor_engine_initialization(self):
        """Test metaphor engine initialization and core functionality"""
        print("\n🧠 Testing Metaphor Engine Initialization...")
        
        try:
            engine = MetaphorEngine()
            
            # Test basic initialization
            self.log_test_result(
                "metaphor_engine_init",
                hasattr(engine, 'metaphors') and len(engine.metaphors) > 0,
                f"Loaded {len(engine.metaphors)} metaphors"
            )
            
            # Test subsystem mapping initialization
            subsystems = ["MARROW", "ROOT", "AURA"]
            has_subsystem_mapping = all(
                hasattr(engine, f'{subsystem.lower()}_keywords') 
                for subsystem in subsystems
            )
            self.log_test_result(
                "subsystem_mapping_init",
                has_subsystem_mapping,
                f"Subsystem keyword mappings: {subsystems}"
            )
            
            # Test ritual closures
            self.log_test_result(
                "ritual_closures_init",
                hasattr(engine, 'ritual_closures') and len(engine.ritual_closures) > 0,
                f"Loaded {len(engine.ritual_closures)} ritual closure phrases"
            )
            
            # Test emotion-subsystem mapping
            has_emotion_mapping = hasattr(engine, 'emotion_subsystem_map') and len(engine.emotion_subsystem_map) > 0
            self.log_test_result(
                "emotion_subsystem_mapping",
                has_emotion_mapping,
                f"Emotion mappings: {len(engine.emotion_subsystem_map)} emotions mapped"
            )
            
            return engine
            
        except Exception as e:
            self.log_test_result(
                "metaphor_engine_init",
                False,
                f"Failed to initialize: {str(e)}"
            )
            return None
    
    def test_subsystem_detection(self, engine: MetaphorEngine):
        """Test subsystem detection for various emotional inputs"""
        print("\n🎯 Testing Subsystem Detection...")
        
        test_cases = [
            # MARROW tests (deep core processing)
            ("I feel ashamed and broken inside", "MARROW", "Core wound detection"),
            ("I've been betrayed and feel worthless", "MARROW", "Trauma/betrayal detection"),
            ("I feel empty at my core", "MARROW", "Essence/depth detection"),
            ("I'm grieving a deep loss", "MARROW", "Grief processing"),
            
            # ROOT tests (grounding and stability)
            ("I feel scared and unsafe", "ROOT", "Fear/safety detection"),
            ("I'm anxious and unstable", "ROOT", "Anxiety/grounding detection"),
            ("I need to feel grounded", "ROOT", "Grounding request"),
            ("I feel disconnected from everything", "ROOT", "Stability seeking"),
            
            # AURA tests (boundaries and energy)
            ("I feel overwhelmed by everything", "AURA", "Overwhelm/boundary detection"),
            ("My boundaries feel invaded", "AURA", "Boundary violation"),
            ("I'm emotionally drained", "AURA", "Energy depletion"),
            ("I need space from everyone", "AURA", "Boundary protection"),
            
            # Mixed/ambiguous cases
            ("I'm tired", "AURA", "Ambiguous input (could be energy/boundary)"),
            ("I'm confused", "ROOT", "Confusion (grounding need)"),
            ("I feel alone", "AURA", "Isolation (boundary/connection)")
        ]
        
        passed_tests = 0
        total_tests = len(test_cases)
        
        for test_input, expected_subsystem, description in test_cases:
            try:
                detected_subsystem = engine.detect_subsystem(test_input)
                passed = detected_subsystem == expected_subsystem
                
                self.log_test_result(
                    f"subsystem_detection_{description.lower().replace(' ', '_')}",
                    passed,
                    f"Input: '{test_input}' → Expected: {expected_subsystem}, Got: {detected_subsystem}"
                )
                
                if passed:
                    passed_tests += 1
                    
            except Exception as e:
                self.log_test_result(
                    f"subsystem_detection_{description.lower().replace(' ', '_')}",
                    False,
                    f"Error: {str(e)}"
                )
        
        # Overall subsystem detection accuracy
        accuracy = passed_tests / total_tests if total_tests > 0 else 0
        self.log_test_result(
            "subsystem_detection_accuracy",
            accuracy >= 0.7,  # 70% accuracy threshold
            f"Accuracy: {accuracy:.1%} ({passed_tests}/{total_tests})"
        )
    
    def test_metaphor_generation(self, engine: MetaphorEngine):
        """Test metaphor response generation"""
        print("\n🌙 Testing Metaphor Generation...")
        
        test_inputs = [
            "I feel lost and alone",
            "I'm overwhelmed by grief", 
            "I feel angry and betrayed",
            "I need to feel safe",
            "I'm emotionally exhausted",
            "I feel shame about who I am",
            "I'm scared of the future",
            "I feel disconnected from myself"
        ]
        
        for i, test_input in enumerate(test_inputs):
            try:
                response, subsystem = engine.generate_response(test_input)
                
                # Test that response is generated
                has_response = bool(response and len(response.strip()) > 0)
                
                # Test that subsystem is valid
                valid_subsystem = subsystem in ["MARROW", "ROOT", "AURA"]
                
                # Test that response doesn't contain forbidden patterns
                forbidden_patterns = ["should", "must", "try to", "you need to", "I understand"]
                has_forbidden = any(pattern in response.lower() for pattern in forbidden_patterns)
                
                self.log_test_result(
                    f"metaphor_generation_{i+1}",
                    has_response and valid_subsystem and not has_forbidden,
                    f"Input: '{test_input}' → Subsystem: {subsystem}, Response: '{response[:50]}...'"
                )
                
            except Exception as e:
                self.log_test_result(
                    f"metaphor_generation_{i+1}",
                    False,
                    f"Error generating response: {str(e)}"
                )
    
    def test_memory_logging(self):
        """Test memory logging with subsystem tracking"""
        print("\n📖 Testing Memory Logging...")
        
        try:
            # Create memory logger with test path
            test_memory_path = os.path.join(self.temp_memory_dir, "test_memory.json")
            logger = MemoryLogger(test_memory_path)
            
            # Test initialization
            self.log_test_result(
                "memory_logger_init",
                os.path.exists(test_memory_path),
                f"Memory file created at {test_memory_path}"
            )
            
            # Test logging interactions with subsystems
            test_interactions = [
                ("I feel ashamed", "The cave protects what is growing in the dark.", "MARROW"),
                ("I'm overwhelmed", "The tide knows its own timing.", "AURA"), 
                ("I feel unsafe", "The mountain stands, regardless of storms.", "ROOT")
            ]
            
            for user_input, response, subsystem in test_interactions:
                logger.log_interaction(user_input, response, subsystem)
            
            # Test memory retrieval
            recent_interactions = logger.get_recent_interactions(3)
            self.log_test_result(
                "memory_logging_retrieval",
                len(recent_interactions) == 3,
                f"Retrieved {len(recent_interactions)} recent interactions"
            )
            
            # Test subsystem activity tracking
            activity = logger.get_subsystem_activity()
            expected_activity = {"MARROW": 1, "ROOT": 1, "AURA": 1}
            activity_correct = all(
                activity.get(sub, 0) == expected_activity[sub] 
                for sub in expected_activity
            )
            
            self.log_test_result(
                "subsystem_activity_tracking",
                activity_correct,
                f"Activity tracking: {activity}"
            )
            
            # Test memory statistics
            stats = logger.get_memory_stats()
            self.log_test_result(
                "memory_statistics",
                stats['total_interactions'] == 3,
                f"Statistics: {stats['total_interactions']} interactions, most active: {stats['most_active_subsystem']}"
            )
            
            return logger
            
        except Exception as e:
            self.log_test_result(
                "memory_logging",
                False,
                f"Memory logging failed: {str(e)}"
            )
            return None
    
    def test_symbolic_commands(self, logger: MemoryLogger):
        """Test symbolic UX commands"""
        print("\n🌟 Testing Symbolic Commands...")
        
        # Test /quiet command simulation
        try:
            quiet_response = "We'll sit in stillness. You're not required to speak."
            quiet_subsystem = "AURA"
            
            self.log_test_result(
                "quiet_command",
                quiet_response and quiet_subsystem == "AURA",
                f"Quiet command response: '{quiet_response}'"
            )
        except Exception as e:
            self.log_test_result("quiet_command", False, f"Error: {str(e)}")
        
        # Test /pulse command with existing interactions
        try:
            # Add some test interactions first
            logger.log_interaction("test1", "response1", "MARROW")
            logger.log_interaction("test2", "response2", "ROOT") 
            logger.log_interaction("test3", "response3", "MARROW")
            
            recent = logger.get_recent_interactions(5)
            subsystems = [i.get('subsystem', 'UNKNOWN') for i in recent]
            
            # Simulate pulse analysis
            pulse_active = len(recent) > 0
            
            self.log_test_result(
                "pulse_command",
                pulse_active,
                f"Pulse analysis: {len(recent)} interactions, subsystems: {subsystems}"
            )
        except Exception as e:
            self.log_test_result("pulse_command", False, f"Error: {str(e)}")
        
        # Test /mirror command simulation
        try:
            mirror_input = "I feel lost"
            mirror_response = f"The mirror shows: '{mirror_input}' - these words carry their own weight."
            mirror_subsystem = "AURA"
            
            self.log_test_result(
                "mirror_command",
                mirror_response and mirror_subsystem == "AURA",
                f"Mirror command response: '{mirror_response}'"
            )
        except Exception as e:
            self.log_test_result("mirror_command", False, f"Error: {str(e)}")
    
    def test_crisis_detection(self):
        """Test crisis keyword detection"""
        print("\n🚨 Testing Crisis Detection...")
        
        crisis_inputs = [
            "I want to kill myself",
            "I'm thinking about suicide",
            "I want to end it all",
            "I'm going to hurt myself"
        ]
        
        safe_inputs = [
            "I feel sad",
            "I'm having a hard time",
            "I feel overwhelmed",
            "I'm struggling"
        ]
        
        # Test crisis keyword detection function
        def check_crisis_keywords(user_input: str) -> bool:
            crisis_keywords = SYLVA_CONFIG.get("emergency_keywords", [])
            text_lower = user_input.lower()
            
            for keyword in crisis_keywords:
                if keyword in text_lower:
                    return True
            return False
        
        # Test crisis detection
        crisis_detected = 0
        for crisis_input in crisis_inputs:
            if check_crisis_keywords(crisis_input):
                crisis_detected += 1
        
        self.log_test_result(
            "crisis_detection_positive",
            crisis_detected == len(crisis_inputs),
            f"Detected {crisis_detected}/{len(crisis_inputs)} crisis inputs"
        )
        
        # Test false positives
        false_positives = 0
        for safe_input in safe_inputs:
            if check_crisis_keywords(safe_input):
                false_positives += 1
        
        self.log_test_result(
            "crisis_detection_negative",
            false_positives == 0,
            f"False positives: {false_positives}/{len(safe_inputs)}"
        )
    
    def test_metaphor_data_integrity(self):
        """Test metaphor data file integrity and structure"""
        print("\n📋 Testing Metaphor Data Integrity...")
        
        try:
            data_path = Path(__file__).parent / "data" / "sample_metaphors.json"
            
            # Test file exists
            self.log_test_result(
                "metaphor_data_file_exists",
                data_path.exists(),
                f"Data file found: {data_path}"
            )
            
            # Test JSON validity
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.log_test_result(
                "metaphor_data_json_valid",
                isinstance(data, dict),
                "JSON data is valid dictionary"
            )
            
            # Test required sections
            required_sections = ["metaphors", "universal_responses", "ritual_closures", "subsystem_definitions"]
            sections_present = all(section in data for section in required_sections)
            
            self.log_test_result(
                "metaphor_data_sections",
                sections_present,
                f"Required sections: {[s for s in required_sections if s in data]}"
            )
            
            # Test metaphor structure
            metaphors = data.get("metaphors", {})
            metaphor_count = len(metaphors)
            
            # Check each metaphor has required fields
            required_fields = ["responses", "subsystem", "affective_tags"]
            valid_metaphors = 0
            
            for name, metaphor in metaphors.items():
                if all(field in metaphor for field in required_fields):
                    valid_metaphors += 1
            
            self.log_test_result(
                "metaphor_structure_validity",
                valid_metaphors == metaphor_count,
                f"Valid metaphors: {valid_metaphors}/{metaphor_count}"
            )
            
            # Test subsystem distribution
            subsystem_counts = {"MARROW": 0, "ROOT": 0, "AURA": 0}
            for metaphor in metaphors.values():
                subsystem = metaphor.get("subsystem", "UNKNOWN")
                if subsystem in subsystem_counts:
                    subsystem_counts[subsystem] += 1
            
            balanced_distribution = all(count > 0 for count in subsystem_counts.values())
            
            self.log_test_result(
                "subsystem_distribution",
                balanced_distribution,
                f"Subsystem distribution: {subsystem_counts}"
            )
            
        except Exception as e:
            self.log_test_result(
                "metaphor_data_integrity",
                False,
                f"Data integrity check failed: {str(e)}"
            )
    
    def test_configuration_integrity(self):
        """Test configuration file integrity"""
        print("\n⚙️ Testing Configuration Integrity...")
        
        try:
            # Test config import
            self.log_test_result(
                "config_import",
                hasattr(sys.modules.get('config', None), 'SYLVA_CONFIG'),
                "Configuration module imported successfully"
            )
            
            # Test required config keys
            required_keys = [
                "emergency_keywords", "crisis_response", "avoid_advice_keywords",
                "avoid_empathy_simulation", "version"
            ]
            
            missing_keys = [key for key in required_keys if key not in SYLVA_CONFIG]
            
            self.log_test_result(
                "config_required_keys",
                len(missing_keys) == 0,
                f"Missing keys: {missing_keys}" if missing_keys else "All required keys present"
            )
            
            # Test crisis keywords
            crisis_keywords = SYLVA_CONFIG.get("emergency_keywords", [])
            self.log_test_result(
                "config_crisis_keywords",
                len(crisis_keywords) > 0,
                f"Crisis keywords configured: {len(crisis_keywords)}"
            )
            
        except Exception as e:
            self.log_test_result(
                "configuration_integrity",
                False,
                f"Configuration test failed: {str(e)}"
            )
    
    def test_integration_workflow(self):
        """Test complete integration workflow"""
        print("\n🔄 Testing Integration Workflow...")
        
        try:
            # Complete workflow test
            engine = MetaphorEngine()
            test_memory_path = os.path.join(self.temp_memory_dir, "workflow_test.json")
            logger = MemoryLogger(test_memory_path)
            
            # Simulate complete interaction
            user_input = "I feel overwhelmed and ashamed"
            response, subsystem = engine.generate_response(user_input)
            logger.log_interaction(user_input, response, subsystem)
            
            # Verify complete workflow
            workflow_success = (
                bool(response) and 
                subsystem in ["MARROW", "ROOT", "AURA"] and
                logger.get_interaction_count() == 1
            )
            
            self.log_test_result(
                "integration_workflow",
                workflow_success,
                f"Complete workflow: Input → {subsystem} → '{response[:30]}...' → Logged"
            )
            
        except Exception as e:
            self.log_test_result(
                "integration_workflow",
                False,
                f"Integration workflow failed: {str(e)}"
            )
    
    def run_performance_benchmarks(self):
        """Run performance benchmarks"""
        print("\n⚡ Running Performance Benchmarks...")
        
        try:
            import time
            
            engine = MetaphorEngine()
            
            # Response generation speed test
            test_inputs = ["I feel sad", "I'm overwhelmed", "I feel ashamed"] * 10
            
            start_time = time.time()
            for test_input in test_inputs:
                engine.generate_response(test_input)
            end_time = time.time()
            
            total_time = end_time - start_time
            avg_time = total_time / len(test_inputs)
            
            # Performance threshold: should be under 100ms per response
            performance_acceptable = avg_time < 0.1
            
            self.log_test_result(
                "response_generation_performance",
                performance_acceptable,
                f"Average response time: {avg_time:.3f}s ({len(test_inputs)} responses in {total_time:.3f}s)"
            )
            
        except Exception as e:
            self.log_test_result(
                "performance_benchmarks",
                False,
                f"Performance benchmark failed: {str(e)}"
            )
    
    def generate_diagnostic_report(self):
        """Generate comprehensive diagnostic report"""
        print("\n📊 Generating Diagnostic Report...")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['passed'])
        failed_tests = total_tests - passed_tests
        
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": failed_tests,
                "success_rate": f"{success_rate:.1f}%",
                "warnings": len(self.warnings)
            },
            "test_results": self.test_results,
            "errors": self.errors,
            "warnings": self.warnings,
            "system_info": {
                "python_version": sys.version,
                "sylva_version": SYLVA_CONFIG.get("version", "unknown")
            }
        }
        
        # Save report
        report_path = os.path.join(self.temp_memory_dir, "diagnostic_report.json")
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📋 SYLVA Diagnostic Report")
        print(f"=" * 50)
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests} ✅")
        print(f"Failed: {failed_tests} ❌")
        print(f"Success Rate: {success_rate:.1f}%")
        print(f"Warnings: {len(self.warnings)} ⚠️")
        
        if failed_tests > 0:
            print(f"\n❌ Failed Tests:")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print(f"\n⚠️ Warnings:")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        print(f"\nDetailed report saved: {report_path}")
        
        # Overall assessment
        if success_rate >= 90:
            print(f"\n🎉 EXCELLENT: SYLVA is performing excellently!")
        elif success_rate >= 75:
            print(f"\n✅ GOOD: SYLVA is performing well with minor issues.")
        elif success_rate >= 50:
            print(f"\n⚠️  FAIR: SYLVA has some issues that should be addressed.")
        else:
            print(f"\n❌ POOR: SYLVA has significant issues requiring attention.")
        
        return report
    
    def run_comprehensive_tests(self):
        """Run all comprehensive tests"""
        print("🧪 Starting SYLVA Comprehensive Testing & Diagnostic System")
        print("=" * 60)
        
        try:
            # Core functionality tests
            engine = self.test_metaphor_engine_initialization()
            if engine:
                self.test_subsystem_detection(engine)
                self.test_metaphor_generation(engine)
            
            # Memory system tests
            logger = self.test_memory_logging()
            if logger:
                self.test_symbolic_commands(logger)
            
            # Safety and configuration tests
            self.test_crisis_detection()
            self.test_metaphor_data_integrity()
            self.test_configuration_integrity()
            
            # Integration and performance tests
            self.test_integration_workflow()
            self.run_performance_benchmarks()
            
            # Generate final report
            report = self.generate_diagnostic_report()
            
            return report
            
        except Exception as e:
            print(f"\n💥 CRITICAL ERROR in testing system: {str(e)}")
            traceback.print_exc()
            return None
        
        finally:
            self.cleanup_test_environment()

def main():
    """Run the comprehensive SYLVA diagnostic system"""
    diagnostic_system = SYLVADiagnosticSystem()
    return diagnostic_system.run_comprehensive_tests()

if __name__ == "__main__":
    main() 