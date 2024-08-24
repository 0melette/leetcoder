import os
from problem_loader import ProblemLoader

class ProblemRunner:
    def __init__(self, difficulty, problem_name):
        self.difficulty = difficulty
        self.problem_name = problem_name
        self.input_file = f"problems/{difficulty}/{problem_name}_input.txt"
        self.output_file = f"problems/{difficulty}/{problem_name}_output.txt"
        self.solution = ProblemLoader.load_solution(difficulty, problem_name)
    
    def read_inputs(self):
        inputs = []
        with open(self.input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    inputs.append(line)
        return inputs

    def read_expected_outputs(self):
        if not os.path.exists(self.output_file):
            return None
        
        expected_outputs = []
        with open(self.output_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    expected_outputs.append(line)
        return expected_outputs
    
    def run(self):
        inputs = self.read_inputs()
        expected_outputs = self.read_expected_outputs()
        passed_count = 0

        print(f"\n{'Input':<30}{'Output':<30}{'Expected':<30}{'Result':<10}")
        print(f"{'-'*100}")
        
        for i, input_data in enumerate(inputs):
            result = getattr(self.solution, self.problem_name)(input_data)
            expected_output = expected_outputs[i] if expected_outputs else "-----"
            if str(result) == expected_output:
                test_result = "\033[92mPASSED\033[0m"  
                passed_count += 1
            else:
                test_result = "\033[91mFAILED\033[0m" if expected_outputs else "-----"  
            
            print(f"{input_data:<30}{str(result):<30}{expected_output:<30}{test_result:<10}")

        total_tests = len(inputs)
        print(f"\n\033[96mSummary: {passed_count}/{total_tests} test cases passed.\033[0m")