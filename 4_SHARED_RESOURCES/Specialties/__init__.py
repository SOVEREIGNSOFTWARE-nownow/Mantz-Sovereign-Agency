"""
### SPECIALTIES GOALS ###

This __init__.py file defines the central repository for {PROJECT_NAME} Agent Specialized Training and Role Memory. 
It is the next-to-last stage of the agent-boot sequence, providing job-specific context and knowledge.

1.  **Expose Specialty Training Modules:** Imports and exposes the primary functions for loading and applying role-specific training layers (e.g., fine-tuned models, specific prompt configurations, utility classes) from the nested 'training_modules' folder.
2.  **Define Specialty Registry:** Creates a dictionary or structure that maps specialty names (e.g., 'Lawyer & Litigator', 'Security Specialist') to their corresponding training data path and shared memory location.
3.  **Define Shared Memory Access:** Creates a function, `load_specialty_memory()`, which retrieves the shared session logs for a given specialty. This function must be robust enough to be called by *any* agent (Main Agent, Roland, etc.) but strictly returns memory tied to the *job role*, enabling comparative development.
4.  **Define Shared Memory Update:** Creates a function, `update_specialty_memory()`, which safely merges the output of the current agent's session into the shared specialty memory archives.

The goal is to provide a unified, role-based interface for accessing shared knowledge, which is essential for creating the "special orientation and training layer" during agent check-out.

### END GOALS ###
"""


import os
import sys
from typing import Dict, Any, Optional

# --- Define Constants ---
SPECIALTY_ROOT = os.path.dirname(os.path.abspath(__file__))
SHARED_MEMORY_PATH = os.path.join(SPECIALTY_ROOT, "shared_memory_archives")
os.makedirs(SHARED_MEMORY_PATH, exist_ok=True) # Ensure the shared memory store exists


# --- 2. Define Specialty Registry ---
# This dictionary maps the functional role (Specialty) to its key files/paths
SPECIALTY_REGISTRY: Dict[str, Dict[str, str]] = {
    "Lawyer & Litigator": {
        "memory_file": "lawyer_history.json",
        "training_module": "legal_toolkit_v3"
    },
    "Security Specialist": {
        "memory_file": "security_audit_logs.json",
        "training_module": "audit_module_v5"
    },
    # Add other specialties as needed (e.g., "Financial Auditor", "Creative Artist")
}


# --- 1. Expose Specialty Training Modules (Placeholder Imports) ---
# We assume a 'training_modules' sub-directory exists with specific training utilities
try:
    from . import training_modules
    # Assuming 'load_training_layer' is a function defined in training_modules' __init__.py
    from .training_modules import load_training_layer
except ImportError as e:
    print(f"SPECIALTIES WARNING: Training module failed to import. Specialty loading may fail: {e}", file=sys.stderr)


# --- 3. Define Shared Memory Access ---
def load_specialty_memory(specialty_name: str, calling_agent_name: str) -> Optional[Dict[str, Any]]:
    """
    Retrieves the shared specialty memory for a given role, regardless of the calling agent.
    
    Args:
        specialty_name: The name of the job hat/specialty (e.g., 'Lawyer & Litigator').
        calling_agent_name: The name of the agent requesting the memory (e.g., 'Main Agent' or 'Roland').
        
    Returns:
        A dictionary containing the shared memory logs, or None if the specialty is unknown.
    """
    if specialty_name not in SPECIALTY_REGISTRY:
        print(f"Error: Specialty '{specialty_name}' not found in registry.", file=sys.stderr)
        return None
        
    memory_file = SPECIALTY_REGISTRY[specialty_name]["memory_file"]
    file_path = os.path.join(SHARED_MEMORY_PATH, memory_file)
    
    if not os.path.exists(file_path):
        print(f"WARNING: Shared memory archive for '{specialty_name}' not found. Starting fresh.", file=sys.stderr)
        return {"logs": [], "created_by": calling_agent_name, "last_agent": calling_agent_name}

    try:
        import json
        with open(file_path, 'r') as f:
            shared_memory = json.load(f)
        
        # Log the access for comparative development analysis
        shared_memory.setdefault("access_history", []).append({
            "agent": calling_agent_name,
            "access_time": os.path.getmtime(file_path) # Example timestamp
        })
        
        return shared_memory
    except Exception as e:
        print(f"ERROR: Failed to load shared memory for '{specialty_name}'. Details: {e}", file=sys.stderr)
        return None


# --- 4. Define Shared Memory Update ---
def update_specialty_memory(specialty_name: str, new_session_log: Dict[str, Any], contributing_agent: str) -> bool:
    """
    Safely merges new session knowledge into the shared specialty memory archive.
    """
    if specialty_name not in SPECIALTY_REGISTRY:
        return False

    current_memory = load_specialty_memory(specialty_name, contributing_agent)
    if current_memory is None:
        current_memory = {"logs": []}

    # Append the new log, tagging it with the contributing agent's POV
    new_session_log["contributing_agent"] = contributing_agent
    current_memory["logs"].append(new_session_log)
    current_memory["last_agent"] = contributing_agent

    memory_file = SPECIALTY_REGISTRY[specialty_name]["memory_file"]
    file_path = os.path.join(SHARED_MEMORY_PATH, memory_file)

    try:
        import json
        with open(file_path, 'w') as f:
            json.dump(current_memory, f, indent=4)
        return True
    except Exception as e:
        print(f"ERROR: Failed to update shared memory for '{specialty_name}'. Details: {e}", file=sys.stderr)
        return False

# Clean up namespace
del os
del sys
del Dict
del Any
del Optional
