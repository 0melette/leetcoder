import os

class ProblemMenu:
    @staticmethod
    def list_problems():
        problems = []
        for difficulty in ["easy", "medium", "hard"]:
            problem_files = [
                f.replace(".py", "") 
                for f in os.listdir(f"problems/{difficulty}") 
                if f.endswith(".py")
            ]
            problems.extend([(difficulty, prob) for prob in problem_files])
        return problems
    
    @staticmethod
    def display_menu(problems):
        os.system('clear' if os.name == 'posix' else 'cls')  # if windows use cls

        counts = {"easy": 0, "medium": 0, "hard": 0}
        for difficulty, _ in problems:
            counts[difficulty] += 1

        print("\nSelect a problem to run:")
        for i, (difficulty, problem) in enumerate(problems, 1):
            if difficulty == "easy":
                color = "\033[92m"  # Green
            elif difficulty == "medium":
                color = "\033[93m"  # Yellow
            elif difficulty == "hard":
                color = "\033[91m"  # Red
            else:
                color = "\033[0m"   # Default 

            print(f"{i}. {problem} ({color}{difficulty}\033[0m)")

        print(f"\nTotal Problems: {len(problems)}")
        print(f"Easy: \033[92m{counts['easy']}\033[0m, Medium: \033[93m{counts['medium']}\033[0m, Hard: \033[91m{counts['hard']}\033[0m")
