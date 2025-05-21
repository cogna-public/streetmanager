#!/usr/bin/env python3
"""
Script to fix swagger client imports by converting absolute imports to relative imports.
This script processes Python files within each 'swagger_client' directory
(e.g., src/streetmanager/work/swagger_client, src/streetmanager/geojson/swagger_client, etc.).

For each Python file, it:
1. Calculates the necessary relative import prefix ('.', '..', etc.) based on the
   file's depth relative to its 'swagger_client' root directory.
2. Provides specific, robust fixes for 'swagger_client/__init__.py' and
   'swagger_client/api/__init__.py' to ensure correct package structure.
3. For all other files, converts absolute imports like 'from swagger_client.module import Name'
   to 'from <prefix>.module import Name', and 'import swagger_client.module' to 'from <prefix> import module'.
"""

import re
from pathlib import Path

def print_debug_info(file_path: Path, content: str, stage: str):
    print(f"--- DEBUG: {stage} for {file_path.name} ---")
    if file_path.name == "__init__.py" or "default_api.py" in file_path.name or "api_client.py" in file_path.name:
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if "DefaultApi" in line or "api_client" in line or "configuration" in line or "models" in line or "swagger_client" in line:
                print(f"  L{i+1}: {line}")
    print(f"--- END DEBUG: {stage} for {file_path.name} ---")

def convert_imports_in_file(file_path: Path, swagger_client_root: Path, project_root: Path):
    """
    Converts absolute 'swagger_client.' imports to relative imports in a single file.
    Prioritizes specific fixes for __init__.py files.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return
    
    original_content = content
    print_debug_info(file_path, original_content, "Before processing")

    current_filename = file_path.name
    current_file_parent_dir_name = file_path.parent.name
    is_in_swagger_client_root = (file_path.parent == swagger_client_root)
    is_in_api_subfolder = (current_file_parent_dir_name == "api" and file_path.parent.parent == swagger_client_root)

    if current_filename == "__init__.py" and is_in_swagger_client_root:
        # Handles src/streetmanager/<module>/swagger_client/__init__.py
        # Target: from .api import DefaultApi
        content = re.sub(r"from\s+(?:swagger_client\.|\.)(?:api\.)?default_api\s+import\s+DefaultApi", "from .api import DefaultApi", content)
        
        # Ensure other direct imports are single-dot relative
        content = re.sub(r'from\s+swagger_client\.api_client', 'from .api_client', content)
        content = re.sub(r'from\s+swagger_client\.configuration', 'from .configuration', content)
        content = re.sub(r'from\s+swagger_client\.models', 'from .models', content) # For model re-exports if any
        
        # Handle 'import swagger_client.module' for re-exports
        content = re.sub(r'import\s+swagger_client\.api_client', 'from . import api_client', content)
        content = re.sub(r'import\s+swagger_client\.configuration', 'from . import configuration', content)
        content = re.sub(r'import\s+swagger_client\.models', 'from . import models', content) # For model package re-export

    elif current_filename == "__init__.py" and is_in_api_subfolder:
        # Handles src/streetmanager/<module>/swagger_client/api/__init__.py
        # Target: from .default_api import DefaultApi
        content = re.sub(r"from\s+(?:swagger_client\.api\.|\.\.api\.|\.)default_api\s+import\s+DefaultApi", "from .default_api import DefaultApi", content)

    elif current_filename == "default_api.py" and is_in_api_subfolder:
        # Handles src/streetmanager/<module>/swagger_client/api/default_api.py
        # Imports in api/default_api.py need to go up one level (..) for models, api_client, configuration
        content = re.sub(r'from\s+swagger_client\.models', 'from ..models', content)
        content = re.sub(r'import\s+swagger_client\.models', 'from .. import models', content)
        content = re.sub(r'from\s+swagger_client\.api_client\s+import\s+ApiClient', 'from ..api_client import ApiClient', content)
        content = re.sub(r'from\s+swagger_client\s+import\s+ApiClient', 'from ..api_client import ApiClient', content)
        content = re.sub(r'from\s+swagger_client\.configuration\s+import\s+Configuration', 'from ..configuration import Configuration', content)
        content = re.sub(r'from\s+swagger_client\s+import\s+Configuration', 'from ..configuration import Configuration', content)


    elif current_filename == "api_client.py" and is_in_swagger_client_root:
        # Handles src/streetmanager/<module>/swagger_client/api_client.py
        # Imports are single-dot relative (.)
        content = re.sub(r'from\s+swagger_client\.models', 'from .models', content)
        content = re.sub(r'import\s+swagger_client\.models', 'from . import models', content) # Corrected
        content = re.sub(r'from\s+swagger_client\.configuration', 'from .configuration', content)
        content = re.sub(r'import\s+swagger_client\.configuration', 'from . import configuration', content) # Corrected
        content = re.sub(r'from\s+swagger_client\s+import\s+rest', 'from . import rest', content) # Added for 'from swagger_client import rest'

    elif current_filename == "configuration.py" and is_in_swagger_client_root:
        # Handles src/streetmanager/<module>/swagger_client/configuration.py
        # Typically, configuration.py has no 'swagger_client.' imports.
        pass 

    elif file_path.parent.name == "models" and file_path.parent.parent == swagger_client_root:
        # Handles files in src/streetmanager/<module>/swagger_client/models/
        # from swagger_client.models.other_model import OtherModel -> from .other_model import OtherModel
        content = re.sub(r'from\s+swagger_client\.models\.([_a-zA-Z0-9]+)\s+import\s+(.+)', r'from .\1 import \2', content)
        # from swagger_client.models import OtherModel -> from . import OtherModel (if importing from models/__init__.py essentially)
        content = re.sub(r'from\s+swagger_client\.models\s+import\s+(.+)', r'from . import \1', content)
        # import swagger_client.models -> from . import models (if a model imports the whole models package, less likely)
        content = re.sub(r'import\s+swagger_client\.models', 'from . import models', content)

        # If models import from top-level (e.g. configuration, api_client - unlikely but possible)
        # These need to go up one level (..)
        content = re.sub(r'from\s+swagger_client\.configuration', 'from ..configuration', content)
        content = re.sub(r'import\s+swagger_client\.configuration', 'from .. import configuration', content)
        content = re.sub(r'from\s+swagger_client\.api_client', 'from ..api_client', content)
        content = re.sub(r'import\s+swagger_client\.api_client', 'from .. import api_client', content)
    
    else: 
        # Fallback for any other files not covered explicitly, using depth-based calculation.
        # This handles files in arbitrary subdirectories of swagger_client_root.
        try:
            # Calculate depth relative to swagger_client_root
            relative_dir_of_file = file_path.parent.relative_to(swagger_client_root)
            depth = len(relative_dir_of_file.parts)
        except ValueError:
            # This can happen if the file is not under swagger_client_root as expected.
            print(f"Warning: File {file_path} is not directly under {swagger_client_root}. Relative path calculation might be incorrect.")
            # Assume it's at the root for safety, or skip. For now, assume root.
            depth = 0 # Default to root if calculation fails.
        
        # Determine the correct dot prefix.
        # Depth 0 (file in swagger_client_root): prefix "."
        # Depth 1 (file in swagger_client_root/subdir/): prefix ".."
        # Depth 2 (file in swagger_client_root/subdir/subsubdir/): prefix "..."
        dot_prefix = "." + "." * depth

        # Replace "from swagger_client.module import Name"
        # Example: from swagger_client.some.deep.module import Name 
        # Becomes: from ...some.deep.module import Name (if depth = 2)
        content = re.sub(r'from\s+swagger_client\.([_a-zA-Z0-9.]+)\s+import\s+(.+)', rf'from {dot_prefix}\1 import \2', content)
        
        # Replace "import swagger_client.module"
        # Example: import swagger_client.some.deep.module
        # Becomes: from ... import some.deep.module (if depth = 2)
        content = re.sub(r'import\s+swagger_client\.([_a-zA-Z0-9.]+)', rf'from {dot_prefix} import \1', content)


    if content != original_content:
        print(f"Updating imports in: {file_path.relative_to(project_root)}")
        print_debug_info(file_path, content, "After processing, changes made")
        try:
            file_path.write_text(content, encoding='utf-8')
        except Exception as e:
            print(f"Error writing file {file_path}: {e}")
    else:
        # print_debug_info(file_path, content, "After processing, no changes") # Can be very noisy
        print(f"No import changes needed for: {file_path.relative_to(project_root)}")

def main():
    # Determine the project root (assuming script is in 'scripts/' subdirectory of project root)
    try:
        project_root = Path(__file__).resolve().parent.parent
    except NameError: # Fallback if __file__ is not defined (e.g. interactive)
        project_root = Path(".").resolve()

    print(f"Project root identified as: {project_root}")
    base_src_dir = project_root / 'src' / 'streetmanager'

    submodule_types = ["work", "geojson", "lookup"]

    for submodule_name in submodule_types:
        swagger_client_root = base_src_dir / submodule_name / "swagger_client"
        if swagger_client_root.is_dir():
            print(f"\nProcessing swagger client module: {swagger_client_root.relative_to(project_root)}")
            
            python_files = list(swagger_client_root.rglob('*.py'))
            if not python_files:
                print(f"No Python files found in {swagger_client_root.relative_to(project_root)}")
                continue
            
            # Sort files to ensure a consistent and logical processing order.
            # This is important for __init__.py files and dependencies.
            def sort_key(p: Path):
                depth = len(p.relative_to(swagger_client_root).parts)
                name_order = 0
                if p.name == "__init__.py":
                    name_order = 0  # __init__.py first
                elif "api_client.py" in p.name:
                    name_order = 1
                elif "configuration.py" in p.name:
                    name_order = 2
                elif "default_api.py" in p.name: # or other specific api files
                    name_order = 3
                elif p.parent.name == "models":
                    if p.name == "__init__.py":
                        name_order = 4 # models/__init__.py
                    else:
                        name_order = 5 # model files
                else:
                    name_order = 6 # Other files
                return (depth, name_order, p.name)

            python_files.sort(key=sort_key)


            for file_path in python_files:
                convert_imports_in_file(file_path, swagger_client_root, project_root)
        else:
            print(f"Directory not found, skipping: {swagger_client_root.relative_to(project_root)}")

    print("\nImport fixing process completed.")

if __name__ == '__main__':
    main()