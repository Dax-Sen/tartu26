#!/usr/bin/env python3
import os
import re
import subprocess
import sys

def extract_code(qmd_path, output_path, lang):
    if not os.path.exists(qmd_path):
        print(f"File not found: {qmd_path}")
        return
    
    print(f"Extracting {lang} code from {qmd_path} -> {output_path}")
    with open(qmd_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match code blocks of the specified language: ```{lang} ... ```
    pattern = rf"```+\s*\{{{lang}(?:,\s*.*)?\}}(.*?)\n```+"
    matches = re.findall(pattern, content, re.DOTALL)
    
    code_blocks = []
    for match in matches:
        lines = match.strip('\n').split('\n')
        # Filter out Quarto cell options (lines starting with #|)
        filtered_lines = [line for line in lines if not line.strip().startswith('#|')]
        code_blocks.append('\n'.join(filtered_lines))
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(code_blocks).strip() + '\n')

def run_quarto_convert(qmd_path):
    if not os.path.exists(qmd_path):
        return
    print(f"Converting {qmd_path} to ipynb...")
    try:
        subprocess.run(["quarto", "convert", qmd_path], check=True)
    except Exception as e:
        print(f"Error converting {qmd_path} to ipynb: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Define files to process
    python_qmds = ["od-data-python.qmd", "demo-py.qmd"]
    r_qmds = ["workbook.qmd", "workbook_basic_routing.qmd", "demo.qmd", "prerequisites.qmd"]
    
    # 1. Convert python qmds to ipynb and extract python scripts
    for qmd in python_qmds:
        run_quarto_convert(qmd)
        py_name = qmd.replace(".qmd", ".py")
        extract_code(qmd, os.path.join("code", py_name), "python")
        
    # 2. Extract R scripts
    for qmd in r_qmds:
        r_name = qmd.replace(".qmd", ".R")
        extract_code(qmd, os.path.join("code", r_name), "r")
        
    print("Code extraction and conversion complete!")
