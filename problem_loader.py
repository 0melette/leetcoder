import importlib.util
import inspect
from common import *
class ProblemLoader:
    @staticmethod
    def load_solution(difficulty, problem_name):
        problem_file = f"problems/{difficulty}/{problem_name}.py"
        spec = importlib.util.spec_from_file_location("Solution", problem_file)
        problem_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(problem_module)
        return problem_module.Solution()

    @staticmethod
    def get_method_signature(solution, method_name):
        method = getattr(solution, method_name)
        signature = inspect.signature(method)
        print(signature)
        return signature