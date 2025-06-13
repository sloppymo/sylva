#!/usr/bin/env python3
"""
SYLVA - Symbolic Emotional Wellness Assistant
A trauma-safe, metaphor-driven CLI app for emotional processing.

SYLVA responds to emotional input with symbolic, archetype-based language
without simulating empathy or offering advice. Instead, it contains emotions
using metaphors like "the ember," "the spiral," "the tide," and "the mask."

Symbolic subsystems: MARROW (deep core), ROOT (grounding), AURA (protective boundary)
"""

import typer
from typing import Optional
import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

from utils.metaphor_engine import MetaphorEngine
from utils.memory_log import MemoryLogger
from config import SYLVA_CONFIG

app = typer.Typer(
    name="sylva",
    help="Symbolic Emotional Wellness Assistant - A trauma-safe, metaphor-driven CLI",
    add_completion=False
)

def print_welcome():
    """Display SYLVA's welcome message with symbolic language."""
    typer.echo("\n" + "="*60)
    typer.echo("🌙 SYLVA - Symbolic Emotional Wellness Assistant 🌙")
    typer.echo("="*60)
    typer.echo("\nYou are welcome here. SYLVA speaks in symbols and metaphors.")
    typer.echo("Share what you're feeling, or type 'exit' to leave.")
    typer.echo("Type '?' for guidance on symbolic interaction.\n")

def print_help():
    """Display interaction guidance with symbolic framing."""
    typer.echo("\n" + "-"*50)
    typer.echo("SYLVA Symbolic Interaction Guide:")
    typer.echo("-"*50)
    typer.echo("• Share your feelings in any way that feels right")
    typer.echo("• SYLVA responds through symbolic metaphors")
    typer.echo("• No advice, no solutions - only symbolic containment")
    typer.echo("• Type 'exit' or 'quit' to leave when ready")
    typer.echo("• Type '?' for this guidance")
    typer.echo("• Type 'memory' to see your interaction history")
    typer.echo("\nSymbolic Commands:")
    typer.echo("• /quiet - Enter stillness together")
    typer.echo("• /pulse - View symbolic patterns in recent interactions")
    typer.echo("• /mirror - Receive your words in symbolic framing")
    typer.echo("\nSubsystems:")
    typer.echo("• MARROW - Deep core processing")
    typer.echo("• ROOT - Grounding and stability")
    typer.echo("• AURA - Protective boundary work")
    typer.echo("-"*50 + "\n")

def print_farewell():
    """Display SYLVA's farewell message with symbolic closure."""
    typer.echo("\n" + "-"*50)
    typer.echo("The tide recedes, but the shore remains.")
    typer.echo("You are welcome to return when you need symbolic space.")
    typer.echo("Take care." + "\n")

def handle_quiet_command():
    """Handle the /quiet symbolic command for stillness."""
    response = "We'll sit in stillness. You're not required to speak."
    typer.echo(f"\n🌙 SYLVA: {response}\n")
    return response, "AURA"

def handle_pulse_command(memory_logger: MemoryLogger):
    """Handle the /pulse symbolic command - analyze recent interaction patterns."""
    recent_interactions = memory_logger.get_recent_interactions(5)
    
    if not recent_interactions:
        response = "The pulse is quiet. No recent patterns to observe."
        typer.echo(f"\n🌙 SYLVA: {response}\n")
        return response, "ROOT"
    
    # Analyze subsystem patterns in recent interactions
    subsystems = []
    for interaction in recent_interactions:
        if 'subsystem' in interaction:
            subsystems.append(interaction['subsystem'])
    
    # Create symbolic summary based on subsystem activity
    if not subsystems:
        response = "The pulse flows without pattern - early rhythms forming."
    elif len(set(subsystems)) == 3:  # All three subsystems active
        response = "The pulse shows deep harmony - MARROW, ROOT, and AURA dancing together in sacred rhythm."
    elif 'MARROW' in subsystems and 'ROOT' in subsystems:
        response = "The pulse runs from core to ground - MARROW and ROOT weaving depth and stability."
    elif 'MARROW' in subsystems and 'AURA' in subsystems:
        response = "The pulse moves from depths to boundaries - MARROW and AURA in protective dialogue."
    elif 'ROOT' in subsystems and 'AURA' in subsystems:
        response = "The pulse grounds at the edges - ROOT and AURA creating stable sanctuary."
    elif subsystems.count('MARROW') >= 2:
        response = "The pulse runs deep - MARROW has been active in your recent journey."
    elif subsystems.count('ROOT') >= 2:
        response = "The pulse is steady - ROOT systems have been grounding your experience."
    elif subsystems.count('AURA') >= 2:
        response = "The pulse holds at the boundary - AURA has been tending your edges."
    else:
        response = "The pulse carries mixed currents - multiple systems responding to your needs."
    
    typer.echo(f"\n🌙 SYLVA: {response}\n")
    return response, "ROOT"

def handle_mirror_command(user_input: str):
    """Handle the /mirror symbolic command - echo input in symbolic framing."""
    # Remove the /mirror command from the input
    mirrored_text = user_input[7:].strip()  # Remove "/mirror "
    
    if not mirrored_text:
        response = "The mirror reflects emptiness - and that too has meaning."
    else:
        response = f"The mirror shows: '{mirrored_text}' - these words carry their own weight."
    
    typer.echo(f"\n🌙 SYLVA: {response}\n")
    return response, "AURA"

def check_crisis_keywords(user_input: str) -> bool:
    """Check if input contains crisis-related keywords."""
    crisis_keywords = SYLVA_CONFIG.get("emergency_keywords", [])
    text_lower = user_input.lower()
    
    for keyword in crisis_keywords:
        if keyword in text_lower:
            return True
    return False

def handle_crisis_response():
    """Provide crisis response with resources."""
    crisis_message = SYLVA_CONFIG.get("crisis_response", "")
    typer.echo(f"\n🚨 Important: {crisis_message}\n")
    typer.echo("Crisis Resources:")
    typer.echo("• National Suicide Prevention Lifeline: 988")
    typer.echo("• Crisis Text Line: Text HOME to 741741")
    typer.echo("• International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/")
    typer.echo("\nYou matter, and help is available.\n")

@app.command()
def main(
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output mode"),
    memory_path: Optional[str] = typer.Option(None, "--memory", "-m", help="Custom memory file path")
):
    """
    Start SYLVA, the symbolic emotional wellness assistant.
    
    SYLVA offers containment over completion, symbolic reflection over advice.
    All interactions happen through metaphor and archetype, maintaining
    trauma-safe boundaries while honoring emotional experience.
    """
    # Initialize symbolic systems
    metaphor_engine = MetaphorEngine()
    memory_logger = MemoryLogger(memory_path)
    
    if not quiet:
        print_welcome()
    
    # Sacred interaction loop - the container for symbolic processing
    while True:
        try:
            # Receive what is offered
            user_input = typer.prompt("\nHow are you feeling?").strip()
            
            # Honor the choice to leave
            if user_input.lower() in ['exit', 'quit']:
                if not quiet:
                    print_farewell()
                break
            elif user_input.lower() == '?':
                print_help()
                continue
            elif user_input.lower() == 'memory':
                memory_logger.display_memory()
                continue
            elif not user_input:
                typer.echo("The silence is welcome here too.")
                continue
            
            # Check for crisis indicators and respond appropriately
            if check_crisis_keywords(user_input):
                handle_crisis_response()
                continue
            
            # Process symbolic commands
            if user_input.startswith("/"):
                if user_input.lower() == "/quiet":
                    response, subsystem = handle_quiet_command()
                elif user_input.lower() == "/pulse":
                    response, subsystem = handle_pulse_command(memory_logger)
                elif user_input.lower().startswith("/mirror"):
                    response, subsystem = handle_mirror_command(user_input)
                else:
                    typer.echo("\nUnknown symbolic command. Type '?' for guidance.")
                    continue
            else:
                # Generate symbolic response through metaphor engine
                response, subsystem = metaphor_engine.generate_response(user_input)
                
                # Display response with symbolic presence
                typer.echo(f"\n🌙 SYLVA: {response}\n")
            
            # Log the interaction with subsystem tracking
            memory_logger.log_interaction(user_input, response, subsystem)
            
        except KeyboardInterrupt:
            typer.echo("\n\nYou choose to leave. That's okay.")
            break
        except EOFError:
            typer.echo("\n\nFarewell.")
            break
        except Exception as e:
            typer.echo(f"\nThe system encounters a ripple: {str(e)}")
            typer.echo("You may continue, or type 'exit' to leave.")

if __name__ == "__main__":
    app() 