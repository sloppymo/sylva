"""
Memory Logger for SYLVA
Handles logging of user interactions and system responses to JSON files with subsystem tracking.

Maintains a timestamped record of conversations for reflection and continuity,
including symbolic subsystem activity (MARROW, ROOT, AURA) for pattern analysis.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import typer

class MemoryLogger:
    """
    Logs SYLVA interactions to JSON files for memory and reflection.
    Tracks subsystem activity for symbolic pattern analysis.
    """
    
    def __init__(self, custom_memory_path: Optional[str] = None):
        """
        Initialize the memory logger with subsystem tracking capability.
        
        Args:
            custom_memory_path: Optional custom path for memory file
        """
        if custom_memory_path:
            self.memory_file = Path(custom_memory_path)
        else:
            # Default to memory/user_log.json relative to project root
            self.memory_file = Path(__file__).parent.parent / "memory" / "user_log.json"
        
        # Ensure the memory directory exists
        self.memory_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize memory file if it doesn't exist
        self._initialize_memory_file()
    
    def _initialize_memory_file(self):
        """Initialize the memory file with enhanced structure including subsystem tracking."""
        if not self.memory_file.exists():
            initial_data = {
                "metadata": {
                    "created": datetime.now().isoformat(),
                    "version": "2.0",
                    "description": "SYLVA interaction memory log with subsystem tracking",
                    "subsystems": {
                        "MARROW": "Deep core processing - essence, wounds, transformation",
                        "ROOT": "Grounding and stability - foundation, safety, basic needs", 
                        "AURA": "Protective boundary - energy, interface with world, protection"
                    }
                },
                "interactions": [],
                "subsystem_activity": {
                    "MARROW": 0,
                    "ROOT": 0,
                    "AURA": 0
                }
            }
            self._write_memory(initial_data)
    
    def _read_memory(self) -> Dict:
        """
        Read the current memory file with error handling.
        
        Returns:
            Dictionary containing memory data
        """
        try:
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Ensure subsystem tracking exists in older logs
                if "subsystem_activity" not in data:
                    data["subsystem_activity"] = {"MARROW": 0, "ROOT": 0, "AURA": 0}
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            # If file is corrupted or missing, reinitialize
            self._initialize_memory_file()
            return self._read_memory()
    
    def _write_memory(self, data: Dict):
        """
        Write data to the memory file with error handling.
        
        Args:
            data: Dictionary to write to JSON file
        """
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            typer.echo(f"Warning: Could not write to memory file: {str(e)}")
    
    def log_interaction(self, user_input: str, sylva_response: str, subsystem: str):
        """
        Log a single interaction between user and SYLVA with subsystem tracking.
        
        Args:
            user_input: The user's emotional expression
            sylva_response: SYLVA's symbolic response
            subsystem: The active subsystem (MARROW/ROOT/AURA)
        """
        memory_data = self._read_memory()
        
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "sylva_response": sylva_response,
            "subsystem": subsystem,
            "session_id": self._get_session_id(),
            "interaction_id": self._generate_interaction_id()
        }
        
        memory_data["interactions"].append(interaction)
        
        # Update subsystem activity tracking
        if subsystem in memory_data["subsystem_activity"]:
            memory_data["subsystem_activity"][subsystem] += 1
        
        # Keep only the last 1000 interactions to prevent file bloat
        if len(memory_data["interactions"]) > 1000:
            memory_data["interactions"] = memory_data["interactions"][-1000:]
            # Recalculate subsystem activity for remaining interactions
            self._recalculate_subsystem_activity(memory_data)
        
        self._write_memory(memory_data)
    
    def _generate_interaction_id(self) -> str:
        """
        Generate a unique interaction ID.
        
        Returns:
            Unique interaction identifier
        """
        return datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:17]
    
    def _recalculate_subsystem_activity(self, memory_data: Dict):
        """
        Recalculate subsystem activity counts from remaining interactions.
        
        Args:
            memory_data: Memory data dictionary to update
        """
        activity_counts = {"MARROW": 0, "ROOT": 0, "AURA": 0}
        
        for interaction in memory_data["interactions"]:
            subsystem = interaction.get("subsystem", "ROOT")
            if subsystem in activity_counts:
                activity_counts[subsystem] += 1
        
        memory_data["subsystem_activity"] = activity_counts
    
    def _get_session_id(self) -> str:
        """
        Generate a session identifier based on current date.
        
        Returns:
            Session ID string
        """
        return datetime.now().strftime("%Y%m%d")
    
    def display_memory(self, limit: int = 10):
        """
        Display recent interactions from memory with symbolic formatting.
        
        Args:
            limit: Number of recent interactions to display
        """
        memory_data = self._read_memory()
        interactions = memory_data.get("interactions", [])
        
        if not interactions:
            typer.echo("\nNo previous interactions found.")
            typer.echo("The memory container awaits your first symbolic exchange.\n")
            return
        
        typer.echo(f"\n📖 Recent SYLVA Interactions (last {min(limit, len(interactions))}):")
        typer.echo("=" * 60)
        
        # Display most recent interactions first
        recent_interactions = interactions[-limit:]
        
        for i, interaction in enumerate(recent_interactions, 1):
            timestamp = interaction.get("timestamp", "Unknown")
            user_input = interaction.get("user_input", "")
            sylva_response = interaction.get("sylva_response", "")
            subsystem = interaction.get("subsystem", "UNKNOWN")
            
            # Format timestamp for display
            try:
                dt = datetime.fromisoformat(timestamp)
                formatted_time = dt.strftime("%Y-%m-%d %H:%M")
            except:
                formatted_time = timestamp
            
            # Subsystem symbols for visual identification
            subsystem_symbols = {
                "MARROW": "🔥",  # Core/fire
                "ROOT": "🌳",    # Grounding/tree
                "AURA": "🌙",    # Boundary/moon
                "UNKNOWN": "❓"
            }
            symbol = subsystem_symbols.get(subsystem, "❓")
            
            typer.echo(f"\n{i}. {formatted_time} {symbol} {subsystem}")
            typer.echo(f"   You: {user_input}")
            typer.echo(f"   SYLVA: {sylva_response}")
            typer.echo("-" * 40)
        
        # Display subsystem activity summary
        self._display_subsystem_summary(memory_data)
        
        typer.echo(f"\nTotal interactions: {len(interactions)}")
        typer.echo(f"Memory file: {self.memory_file}")
    
    def _display_subsystem_summary(self, memory_data: Dict):
        """
        Display subsystem activity summary.
        
        Args:
            memory_data: Memory data containing subsystem activity
        """
        activity = memory_data.get("subsystem_activity", {})
        total_interactions = sum(activity.values())
        
        if total_interactions == 0:
            return
        
        typer.echo("\n🧠 Subsystem Activity Patterns:")
        typer.echo("-" * 30)
        
        for subsystem in ["MARROW", "ROOT", "AURA"]:
            count = activity.get(subsystem, 0)
            percentage = (count / total_interactions) * 100 if total_interactions > 0 else 0
            
            # Visual bar representation
            bar_length = int(percentage / 5)  # 5% per character
            bar = "█" * bar_length + "░" * (20 - bar_length)
            
            subsystem_symbols = {"MARROW": "🔥", "ROOT": "🌳", "AURA": "🌙"}
            symbol = subsystem_symbols.get(subsystem, "")
            
            typer.echo(f"{symbol} {subsystem}: {bar} {count} ({percentage:.1f}%)")
    
    def get_interaction_count(self) -> int:
        """
        Get the total number of logged interactions.
        
        Returns:
            Number of interactions in memory
        """
        memory_data = self._read_memory()
        return len(memory_data.get("interactions", []))
    
    def get_recent_interactions(self, count: int = 5) -> List[Dict]:
        """
        Get the most recent interactions with subsystem information.
        
        Args:
            count: Number of recent interactions to retrieve
            
        Returns:
            List of recent interaction dictionaries
        """
        memory_data = self._read_memory()
        interactions = memory_data.get("interactions", [])
        return interactions[-count:] if interactions else []
    
    def get_subsystem_activity(self) -> Dict[str, int]:
        """
        Get subsystem activity counts.
        
        Returns:
            Dictionary of subsystem activity counts
        """
        memory_data = self._read_memory()
        return memory_data.get("subsystem_activity", {"MARROW": 0, "ROOT": 0, "AURA": 0})
    
    def get_subsystem_patterns(self, days: int = 7) -> Dict[str, List[str]]:
        """
        Analyze subsystem patterns over recent days.
        
        Args:
            days: Number of days to analyze
            
        Returns:
            Dictionary mapping dates to subsystem sequences
        """
        memory_data = self._read_memory()
        interactions = memory_data.get("interactions", [])
        
        patterns = {}
        cutoff_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        cutoff_date = cutoff_date.replace(day=cutoff_date.day - days)
        
        for interaction in interactions:
            try:
                timestamp = datetime.fromisoformat(interaction["timestamp"])
                if timestamp >= cutoff_date:
                    date_key = timestamp.strftime("%Y-%m-%d")
                    if date_key not in patterns:
                        patterns[date_key] = []
                    patterns[date_key].append(interaction.get("subsystem", "UNKNOWN"))
            except (ValueError, KeyError):
                continue
        
        return patterns
    
    def clear_memory(self, confirm: bool = False) -> bool:
        """
        Clear all interaction memory while preserving structure.
        
        Args:
            confirm: Whether to skip confirmation prompt
            
        Returns:
            True if memory was cleared, False otherwise
        """
        if not confirm:
            response = typer.prompt(
                "Are you sure you want to clear all SYLVA memory? The sacred container will be emptied. (yes/no)"
            ).lower()
            if response not in ['yes', 'y']:
                typer.echo("Memory clearing cancelled. The container remains.")
                return False
        
        initial_data = {
            "metadata": {
                "created": datetime.now().isoformat(),
                "version": "2.0",
                "description": "SYLVA interaction memory log with subsystem tracking (cleared)",
                "subsystems": {
                    "MARROW": "Deep core processing - essence, wounds, transformation",
                    "ROOT": "Grounding and stability - foundation, safety, basic needs",
                    "AURA": "Protective boundary - energy, interface with world, protection"
                }
            },
            "interactions": [],
            "subsystem_activity": {
                "MARROW": 0,
                "ROOT": 0,
                "AURA": 0
            }
        }
        
        self._write_memory(initial_data)
        typer.echo("SYLVA memory has been cleared. The container is ready for new symbolic exchanges.")
        return True
    
    def export_memory(self, export_path: str) -> bool:
        """
        Export memory to a specified file with symbolic formatting.
        
        Args:
            export_path: Path where to export the memory file
            
        Returns:
            True if export was successful, False otherwise
        """
        try:
            memory_data = self._read_memory()
            export_file = Path(export_path)
            
            # Ensure export directory exists
            export_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Add export metadata
            memory_data["export_metadata"] = {
                "exported_at": datetime.now().isoformat(),
                "total_interactions": len(memory_data.get("interactions", [])),
                "subsystem_activity": memory_data.get("subsystem_activity", {}),
                "export_note": "SYLVA symbolic interaction memory export"
            }
            
            with open(export_file, 'w', encoding='utf-8') as f:
                json.dump(memory_data, f, indent=2, ensure_ascii=False)
            
            typer.echo(f"Memory exported to: {export_file}")
            typer.echo("The sacred record has been preserved.")
            return True
            
        except Exception as e:
            typer.echo(f"Export failed: {str(e)}")
            typer.echo("The memory container could not be transferred.")
            return False
    
    def get_memory_stats(self) -> Dict[str, any]:
        """
        Get comprehensive memory statistics.
        
        Returns:
            Dictionary containing memory statistics
        """
        memory_data = self._read_memory()
        interactions = memory_data.get("interactions", [])
        activity = memory_data.get("subsystem_activity", {})
        
        total_interactions = len(interactions)
        
        # Calculate session distribution
        sessions = {}
        for interaction in interactions:
            session_id = interaction.get("session_id", "unknown")
            sessions[session_id] = sessions.get(session_id, 0) + 1
        
        # Find most active subsystem
        most_active_subsystem = "NONE"
        if activity:
            most_active_subsystem = max(activity, key=activity.get)
        
        return {
            "total_interactions": total_interactions,
            "unique_sessions": len(sessions),
            "subsystem_activity": activity,
            "most_active_subsystem": most_active_subsystem,
            "memory_file_size": self.memory_file.stat().st_size if self.memory_file.exists() else 0,
            "created_date": memory_data.get("metadata", {}).get("created", "unknown"),
            "version": memory_data.get("metadata", {}).get("version", "1.0")
        } 