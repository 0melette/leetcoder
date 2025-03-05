#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def get_difficulty():
    while True:
        print("\nSelect difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return ["easy", "medium", "hard"][choice - 1]
            print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number")

def get_method_signature():
    print("\nPaste the method signature:")
    print("Press Enter twice when done:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)

def create_problem_file(difficulty, method_signature):
    method_lines = method_signature.split('\n')
    for line in method_lines:
        if line.strip().startswith('def '):
            problem_name = line.split('(')[0].split()[-1]
            break
    else:
        print("Error: Could not find method definition in signature")
        return False

    problem_dir = Path("problems") / difficulty
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    problem_file = problem_dir / f"{problem_name}.py"
    if problem_file.exists():
        print(f"Warning: {problem_file} already exists")
        if input("Do you want to overwrite it? (y/n): ").lower() != 'y':
            return False
    
    problem_file.write_text(method_signature)
    return problem_name

def create_sample_files(difficulty, problem_name):
    print("\nEnter sample input:")
    print("Press Enter twice when done:")
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line)
    
    input_file = Path("problems") / difficulty / f"{problem_name}_input.txt"
    input_file.write_text("\n".join(input_lines))
    
    print("\nEnter expected output:")
    print("Press Enter twice when done:")
    output_lines = []
    while True:
        line = input()
        if not line:
            break
        output_lines.append(line)
    
    output_file = Path("problems") / difficulty / f"{problem_name}_output.txt"
    output_file.write_text("\n".join(output_lines))

def main():
    print("Welcome to LeetCode Problem Creator!")
    
    difficulty = get_difficulty()
    method_signature = get_method_signature()
    
    problem_name = create_problem_file(difficulty, method_signature)
    if problem_name:
        print(f"\nCreated {problem_name}.py in {difficulty} directory")
        
        create_sample_files(difficulty, problem_name)
        print(f"\nCreated {problem_name}_input.txt and {problem_name}_output.txt in {difficulty} directory")
        
        print("\nProblem setup complete!")
    else:
        print("\nProblem creation cancelled")

if __name__ == "__main__":
    main() 