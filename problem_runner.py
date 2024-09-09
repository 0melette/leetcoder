import os
import textwrap
from typing import List, Optional, Any
from problem_loader import ProblemLoader
from common import *

class ProblemRunner:
    def __init__(self, difficulty, problem_name):
        self.difficulty = difficulty
        self.problem_name = problem_name
        self.input_file = f"problems/{difficulty}/{problem_name}_input.txt"
        self.output_file = f"problems/{difficulty}/{problem_name}_output.txt"
        self.solution = ProblemLoader.load_solution(difficulty, problem_name)
        self.signature = ProblemLoader.get_method_signature(self.solution, problem_name)

    def read_file(self, file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def parse_input(self, input_data):
        inputs = []
        param_types = [param.annotation for param in self.signature.parameters.values()]

        i = 0
        while i < len(input_data):
            parsed_values = []
            for param_type in param_types:
                raw_input = input_data[i].strip().replace('"', '')
                parsed_values.append(self.recursive_parse(raw_input, param_type))
                i += 1
            inputs.append(tuple(parsed_values))
        
        return inputs

    def recursive_parse(self, raw_input: str, expected_type: Any):
        if expected_type == int:
            return int(raw_input)
        elif expected_type == str:
            return raw_input
        elif expected_type == Optional[TreeNode] or expected_type == TreeNode:
            return tree_parser(raw_input)
        elif expected_type == Optional[Node] or expected_type == Node or expected_type == 'Node':
            return nary_tree_parser(raw_input)
        elif expected_type == Optional[ListNode] or expected_type == ListNode:
            return linked_list_parser(raw_input)
        
        elif hasattr(expected_type, '__origin__') and expected_type.__origin__ == list:
            inner_type = expected_type.__args__[0]
        if raw_input.strip() == "[]":
            return [] 
        if raw_input.startswith('[') and raw_input.endswith(']'):
            raw_list = raw_input.strip('[]').split(',')
            if raw_list == ['']:  # the list is empty or malformed
                return []
            return [self.recursive_parse(item.strip(), inner_type) for item in raw_list]
        else:
            raise ValueError(f"Expected a list format for {raw_input}, but got {raw_input}.")
            # TODO: fix for cases where whitespace actually matters later

    def compare_results(self, result, expected):
        formatted_result = str(result).replace(" ", "")
        expected = expected.replace(" ", "")
        return formatted_result == expected, formatted_result

    def run(self):
        inputs = self.read_file(self.input_file)
        expected_outputs = self.read_file(self.output_file)
        parsed_inputs = self.parse_input(inputs)
        print(f"\n{'Input':<35}{'Output':<35}{'Expected':<35}{'Result':<10}")
        print("-" * 120)

        passed_count = 0
        for i, input_set in enumerate(parsed_inputs):
            method = getattr(self.solution, self.problem_name)
            result = method(*input_set)
            expected = expected_outputs[i] if i < len(expected_outputs) else "-----"

            is_correct, formatted_result = self.compare_results(result, expected)
            test_result = "\033[92mPASSED\033[0m" if is_correct else "\033[91mFAILED\033[0m"
            passed_count += is_correct

            self.print_row(inputs[i], formatted_result, expected, test_result)

        all_passed = passed_count == len(expected_outputs)
        print(f"\n\033[96mSummary: {passed_count}/{len(expected_outputs)} test cases passed.\033[0m")
        return all_passed

    def print_row(self, input_data, output, expected, result):
        wrapped_input = textwrap.fill(input_data, 30)
        wrapped_output = textwrap.fill(output, 30)
        wrapped_expected = textwrap.fill(expected, 30)

        input_lines = wrapped_input.splitlines()
        output_lines = wrapped_output.splitlines()
        expected_lines = wrapped_expected.splitlines()

        max_lines = max(len(input_lines), len(output_lines), len(expected_lines))

        for i in range(max_lines):
            input_line = input_lines[i] if i < len(input_lines) else ''
            output_line = output_lines[i] if i < len(output_lines) else ''
            expected_line = expected_lines[i] if i < len(expected_lines) else ''
            result_line = result if i == 0 else ''
            print(f"{input_line:<35}{output_line:<35}{expected_line:<35}{result_line:<10}")