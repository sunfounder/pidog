#!/usr/bin/env python3
"""
Script to extract all documentation from the Pidog project
"""

import os
import ast
import sys
import inspect
import shutil
from pathlib import Path
import importlib.util

# Base directory
BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"

def ensure_docs_dir():
    """Create docs directory structure"""
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "api").mkdir(exist_ok=True)
    (DOCS_DIR / "examples").mkdir(exist_ok=True)
    (DOCS_DIR / "modules").mkdir(exist_ok=True)
    print(f"Created docs directory structure at {DOCS_DIR}")

def extract_module_docstring(file_path):
    """Extract module-level docstring from a Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
            docstring = ast.get_docstring(tree)
            return docstring
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

def extract_class_and_function_docs(file_path):
    """Extract all class and function documentation from a Python file"""
    docs = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content)

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_doc = ast.get_docstring(node)
                if class_doc:
                    docs[f"class_{node.name}"] = {
                        'type': 'class',
                        'name': node.name,
                        'doc': class_doc,
                        'line': node.lineno
                    }

                # Get methods of the class
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_doc = ast.get_docstring(item)
                        if method_doc:
                            docs[f"method_{node.name}.{item.name}"] = {
                                'type': 'method',
                                'class': node.name,
                                'name': item.name,
                                'doc': method_doc,
                                'line': item.lineno
                            }

            elif isinstance(node, ast.FunctionDef):
                # Only top-level functions (not methods)
                if not any(isinstance(parent, ast.ClassDef) for parent in ast.walk(tree)):
                    func_doc = ast.get_docstring(node)
                    if func_doc:
                        docs[f"function_{node.name}"] = {
                            'type': 'function',
                            'name': node.name,
                            'doc': func_doc,
                            'line': node.lineno
                        }

        return docs
    except Exception as e:
        print(f"Error extracting docs from {file_path}: {e}")
        return {}

def generate_module_doc(module_path, relative_path):
    """Generate markdown documentation for a Python module"""
    module_doc = extract_module_docstring(module_path)
    all_docs = extract_class_and_function_docs(module_path)

    module_name = relative_path.stem

    # Build markdown content
    md_content = f"# {module_name}\n\n"
    md_content += f"**File:** `{relative_path}`\n\n"

    if module_doc:
        md_content += f"## Module Description\n\n{module_doc}\n\n"

    # Group by type
    classes = {k: v for k, v in all_docs.items() if v['type'] == 'class'}
    functions = {k: v for k, v in all_docs.items() if v['type'] == 'function'}
    methods = {k: v for k, v in all_docs.items() if v['type'] == 'method'}

    # Classes
    if classes:
        md_content += "## Classes\n\n"
        for key, item in sorted(classes.items(), key=lambda x: x[1]['line']):
            md_content += f"### {item['name']}\n\n"
            md_content += f"**Line:** {item['line']}\n\n"
            md_content += f"{item['doc']}\n\n"

            # Add methods for this class
            class_methods = {k: v for k, v in methods.items() if v['class'] == item['name']}
            if class_methods:
                md_content += f"#### Methods\n\n"
                for mkey, method in sorted(class_methods.items(), key=lambda x: x[1]['line']):
                    md_content += f"##### `{method['name']}`\n\n"
                    md_content += f"**Line:** {method['line']}\n\n"
                    md_content += f"{method['doc']}\n\n"

    # Functions
    if functions:
        md_content += "## Functions\n\n"
        for key, item in sorted(functions.items(), key=lambda x: x[1]['line']):
            md_content += f"### `{item['name']}`\n\n"
            md_content += f"**Line:** {item['line']}\n\n"
            md_content += f"{item['doc']}\n\n"

    return md_content

def copy_readmes():
    """Copy all README files to docs"""
    print("\n=== Copying README files ===")

    readme_files = list(BASE_DIR.rglob("README.md"))

    for readme in readme_files:
        relative = readme.relative_to(BASE_DIR)

        # Skip if it's in docs dir already
        if str(relative).startswith('docs'):
            continue

        # Determine destination
        if readme.parent == BASE_DIR:
            dest = DOCS_DIR / "README.md"
        else:
            # Create a name based on the directory
            dir_name = readme.parent.name
            dest = DOCS_DIR / "examples" / f"{dir_name}_README.md"

        shutil.copy2(readme, dest)
        print(f"Copied: {relative} -> {dest.relative_to(BASE_DIR)}")

def extract_python_docs():
    """Extract documentation from all Python files"""
    print("\n=== Extracting Python module documentation ===")

    # Find all Python files
    py_files = []
    for pattern in ['pidog/**/*.py', 'test/**/*.py', 'examples/**/*.py',
                    'basic_examples/**/*.py', 'gpt_examples/**/*.py',
                    'local_llm_example/**/*.py', 'llm_server_example/**/*.py']:
        py_files.extend(BASE_DIR.glob(pattern))

    for py_file in py_files:
        relative = py_file.relative_to(BASE_DIR)

        # Skip __pycache__ and other unwanted files
        if '__pycache__' in str(relative) or relative.name == 'setup.py':
            continue

        print(f"Processing: {relative}")

        # Generate documentation
        md_content = generate_module_doc(py_file, relative)

        # Determine output location
        if 'pidog' in relative.parts and relative.parts[0] == 'pidog':
            output_dir = DOCS_DIR / "modules"
        else:
            output_dir = DOCS_DIR / "api"

        output_file = output_dir / f"{relative.stem}.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"  -> Generated: {output_file.relative_to(BASE_DIR)}")

def extract_inline_docs():
    """Extract inline documentation and comments from key files"""
    print("\n=== Extracting inline documentation ===")

    # Key files with important inline docs
    key_files = [
        'pidog/pidog.py',
        'pidog/actions_dictionary.py',
    ]

    for file_rel in key_files:
        file_path = BASE_DIR / file_rel
        if not file_path.exists():
            continue

        print(f"Processing: {file_rel}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract significant block comments
        lines = content.split('\n')
        block_comments = []
        current_block = []
        in_docstring = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Multi-line comment blocks
            if stripped.startswith("'''") or stripped.startswith('"""'):
                if in_docstring:
                    current_block.append(line)
                    block_comments.append({
                        'line': i - len(current_block) + 2,
                        'content': '\n'.join(current_block)
                    })
                    current_block = []
                    in_docstring = False
                else:
                    in_docstring = True
                    current_block = [line]
            elif in_docstring:
                current_block.append(line)

            # Significant single-line comments (like the servo diagram)
            elif stripped.startswith('#') and len(stripped) > 2:
                if not current_block or current_block[-1]['type'] != 'comment':
                    current_block = []
                current_block.append({'type': 'comment', 'line': i + 1, 'content': line})
            else:
                if current_block and len(current_block) > 3:  # Only keep significant blocks
                    block_comments.append({
                        'line': current_block[0]['line'],
                        'content': '\n'.join([c['content'] for c in current_block])
                    })
                current_block = []

        # Create inline docs file
        if block_comments:
            output_file = DOCS_DIR / "api" / f"{Path(file_rel).stem}_inline_docs.md"

            md_content = f"# Inline Documentation: {file_rel}\n\n"
            md_content += f"This file contains significant inline documentation and comments extracted from `{file_rel}`.\n\n"

            for block in block_comments:
                md_content += f"## Line {block['line']}\n\n"
                md_content += "```\n"
                md_content += block['content']
                md_content += "\n```\n\n"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(md_content)

            print(f"  -> Generated: {output_file.relative_to(BASE_DIR)}")

def create_index():
    """Create an index file for all documentation"""
    print("\n=== Creating documentation index ===")

    index_content = "# Pidog Documentation Index\n\n"
    index_content += "This documentation was automatically extracted from the Pidog project source code.\n\n"

    # Main README
    if (DOCS_DIR / "README.md").exists():
        index_content += "## Main Documentation\n\n"
        index_content += "- [Project README](README.md)\n\n"

    # Examples
    example_docs = sorted((DOCS_DIR / "examples").glob("*.md"))
    if example_docs:
        index_content += "## Examples Documentation\n\n"
        for doc in example_docs:
            title = doc.stem.replace('_README', '').replace('_', ' ').title()
            index_content += f"- [{title}](examples/{doc.name})\n"
        index_content += "\n"

    # Modules
    module_docs = sorted((DOCS_DIR / "modules").glob("*.md"))
    if module_docs:
        index_content += "## Module Documentation\n\n"
        for doc in module_docs:
            index_content += f"- [{doc.stem}](modules/{doc.name})\n"
        index_content += "\n"

    # API docs
    api_docs = sorted((DOCS_DIR / "api").glob("*.md"))
    if api_docs:
        index_content += "## API Documentation\n\n"
        for doc in api_docs:
            index_content += f"- [{doc.stem}](api/{doc.name})\n"
        index_content += "\n"

    # External documentation
    index_content += "## External Documentation\n\n"
    index_content += "- [Official SunFounder Pidog Documentation](https://docs.sunfounder.com/projects/pidog/en/latest/)\n"
    index_content += "- [Installation Guide](https://docs.sunfounder.com/projects/pidog/en/latest/python/python_start/install_all_modules.html)\n\n"

    with open(DOCS_DIR / "INDEX.md", 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Created: {(DOCS_DIR / 'INDEX.md').relative_to(BASE_DIR)}")

def main():
    print("Starting documentation extraction for Pidog project...")
    print("=" * 60)

    # Create directory structure
    ensure_docs_dir()

    # Extract all documentation
    copy_readmes()
    extract_python_docs()
    extract_inline_docs()
    create_index()

    print("\n" + "=" * 60)
    print("Documentation extraction complete!")
    print(f"All documentation saved to: {DOCS_DIR}")
    print("\nTo view the documentation, start with: docs/INDEX.md")

if __name__ == "__main__":
    main()
