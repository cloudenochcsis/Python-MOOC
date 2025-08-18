#!/usr/bin/env python3
"""
App Scaffolding Script

This script creates a new app based on the current repo structure,
replacing all instances of the template app name with the new app name.
"""

import os
import shutil
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple


class AppScaffolder:
    def __init__(self, template_dir: str):
        self.template_dir = Path(template_dir)
        self.template_name_snake = "demo_app22_67948"
        self.template_name_kebab = "demo-app22-67948"
        self.template_name_display = "Demo App22"
        
        # Files and directories to exclude from copying
        self.exclude_patterns = {
            '.git', '__pycache__', 'node_modules', '.DS_Store',
            'scaffold_app.py', '*.pyc', '.env', 'README.md'
        }
        
        # Binary file extensions that shouldn't have text replacement
        self.binary_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.zip',
            '.tar', '.gz', '.bz2', '.xz', '.7z', '.rar', '.dmg',
            '.exe', '.dll', '.so', '.dylib', '.a', '.o', '.class',
            '.jar', '.war', '.ear', '.dex', '.apk', '.ipa',
            '.keystore', '.p12', '.pem', '.crt', '.key'
        }

    def get_new_app_names(self, app_name: str) -> Dict[str, str]:
        """Generate different name formats from the input app name."""
        # Clean the input name
        clean_name = re.sub(r'[^a-zA-Z0-9\s]', '', app_name.strip())
        
        # Generate snake_case (for Python modules, etc.)
        snake_case = re.sub(r'\s+', '_', clean_name.lower())
        
        # Generate kebab-case (for URLs, project names, etc.)
        kebab_case = re.sub(r'\s+', '-', clean_name.lower())
        
        # Keep display name as provided (with proper spacing)
        display_name = re.sub(r'\s+', ' ', clean_name).title()
        
        return {
            'snake': snake_case,
            'kebab': kebab_case,
            'display': display_name
        }

    def should_exclude(self, path: Path) -> bool:
        """Check if a path should be excluded from copying."""
        name = path.name
        for pattern in self.exclude_patterns:
            if pattern.startswith('*'):
                if name.endswith(pattern[1:]):
                    return True
            elif name == pattern:
                return True
        return False

    def is_binary_file(self, file_path: Path) -> bool:
        """Check if a file is binary and shouldn't have text replacement."""
        return file_path.suffix.lower() in self.binary_extensions

    def replace_in_content(self, content: str, new_names: Dict[str, str]) -> str:
        """Replace template names with new names in file content."""
        # Replace in order of specificity (most specific first)
        content = content.replace(self.template_name_snake, new_names['snake'])
        content = content.replace(self.template_name_kebab, new_names['kebab'])
        content = content.replace(self.template_name_display, new_names['display'])
        
        return content

    def replace_in_filename(self, filename: str, new_names: Dict[str, str]) -> str:
        """Replace template names in filenames and directory names."""
        new_filename = filename
        new_filename = new_filename.replace(self.template_name_snake, new_names['snake'])
        new_filename = new_filename.replace(self.template_name_kebab, new_names['kebab'])
        return new_filename

    def copy_and_transform_directory(self, src_dir: Path, dest_dir: Path, new_names: Dict[str, str]):
        """Recursively copy directory structure with name replacements."""
        if not dest_dir.exists():
            dest_dir.mkdir(parents=True, exist_ok=True)

        for item in src_dir.iterdir():
            if self.should_exclude(item):
                continue

            # Transform the item name
            new_item_name = self.replace_in_filename(item.name, new_names)
            dest_item = dest_dir / new_item_name

            if item.is_dir():
                # Recursively copy directory
                self.copy_and_transform_directory(item, dest_item, new_names)
            else:
                # Copy and transform file
                self.copy_and_transform_file(item, dest_item, new_names)

    def copy_and_transform_file(self, src_file: Path, dest_file: Path, new_names: Dict[str, str]):
        """Copy a file and replace template names in its content if it's a text file."""
        try:
            # Ensure parent directory exists
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            
            if self.is_binary_file(src_file):
                # Just copy binary files without modification
                shutil.copy2(src_file, dest_file)
            else:
                # Read, transform, and write text files
                with open(src_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                transformed_content = self.replace_in_content(content, new_names)
                
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(transformed_content)
                
                # Copy file permissions
                shutil.copystat(src_file, dest_file)
                
        except Exception as e:
            print(f"Warning: Could not process file {src_file}: {e}")
            # Fallback to simple copy
            try:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dest_file)
            except Exception as e2:
                print(f"Error: Could not copy file {src_file}: {e2}")

    def validate_app_name(self, app_name: str) -> bool:
        """Validate the provided app name."""
        if not app_name or not app_name.strip():
            return False
        
        # Check for valid characters (letters, numbers, spaces)
        if not re.match(r'^[a-zA-Z0-9\s]+$', app_name.strip()):
            return False
            
        return True

    def scaffold_app(self, app_name: str, output_dir: str = None) -> bool:
        """Main method to scaffold a new app."""
        if not self.validate_app_name(app_name):
            print("❌ Invalid app name. Please use only letters, numbers, and spaces.")
            return False

        new_names = self.get_new_app_names(app_name)
        
        # Default to Morton-Xperts-Apps on Desktop if no output directory specified
        if output_dir is None:
            desktop_path = Path.home() / "Desktop"
            morton_apps_dir = desktop_path / "Morton-Xperts-Apps"
            # Create the Morton-Xperts-Apps directory if it doesn't exist
            morton_apps_dir.mkdir(exist_ok=True)
            output_dir = morton_apps_dir / new_names['kebab']
        else:
            output_dir = Path(output_dir)
        
        output_path = output_dir.resolve()
        
        if output_path.exists():
            response = input(f"Directory {output_path} already exists. Overwrite? (y/N): ")
            if response.lower() != 'y':
                print("❌ Scaffolding cancelled.")
                return False
            shutil.rmtree(output_path)

        print(f"🚀 Creating new app: {new_names['display']}")
        print(f"📁 Output directory: {output_path}")
        print(f"🔄 Transforming names:")
        print(f"   • Snake case: {new_names['snake']}")
        print(f"   • Kebab case: {new_names['kebab']}")
        print(f"   • Display name: {new_names['display']}")
        print()

        try:
            # Copy and transform the entire directory structure
            # Copy contents of template directory to output path, not the directory itself
            for item in self.template_dir.iterdir():
                if self.should_exclude(item):
                    continue
                
                # Transform the item name
                new_item_name = self.replace_in_filename(item.name, new_names)
                dest_item = output_path / new_item_name
                
                if item.is_dir():
                    self.copy_and_transform_directory(item, dest_item, new_names)
                else:
                    self.copy_and_transform_file(item, dest_item, new_names)
            
            print("✅ App scaffolding completed successfully!")
            print(f"📍 Your new app is ready at: {output_path}")
            print()
            print("🔧 Next steps:")
            print("   1. Navigate to your new app directory")
            print("   2. Install dependencies (npm install, pip install -r requirements.txt)")
            print("   3. Update any environment-specific configurations")
            print("   4. Initialize git repository if needed")
            
            return True
            
        except Exception as e:
            print(f"❌ Error during scaffolding: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main function to run the scaffolding script."""
    print("🏗️  App Scaffolding Tool")
    print("=" * 50)
    print()
    
    # Get the current directory (template directory)
    template_dir = Path(__file__).parent.resolve()
    
    print(f"📂 Template directory: {template_dir}")
    print(f"📁 Default output location: ~/Desktop/Morton-Xperts-Apps")
    print()
    
    # Get app name from user
    while True:
        app_name = input("Enter the name for your new app: ").strip()
        
        if not app_name:
            print("❌ App name cannot be empty. Please try again.")
            continue
            
        scaffolder = AppScaffolder(template_dir)
        if scaffolder.validate_app_name(app_name):
            break
        else:
            print("❌ Invalid app name. Please use only letters, numbers, and spaces.")
    
    # Optional: Get custom output directory
    output_dir = input("Enter output directory (press Enter for ~/Desktop/Morton-Xperts-Apps): ").strip()
    if not output_dir:
        output_dir = None
    
    print()
    
    # Create the scaffolder and run
    scaffolder = AppScaffolder(template_dir)
    success = scaffolder.scaffold_app(app_name, output_dir)
    
    if success:
        print("\n🎉 Happy coding!")
    else:
        print("\n💔 Scaffolding failed. Please check the errors above.")


if __name__ == "__main__":
    main()
