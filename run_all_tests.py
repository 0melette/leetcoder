import os
import time
from problem_runner import ProblemRunner

def run_all_tests():
    problems_dir = "problems"
    difficulties = ["easy", "medium", "hard"]
    all_passed = True
    failed_problems = []

    for difficulty in difficulties:
        difficulty_dir = os.path.join(problems_dir, difficulty)
        if os.path.exists(difficulty_dir):
            for problem_file in os.listdir(difficulty_dir):
                if problem_file.endswith(".py"):
                    problem_name = problem_file.replace(".py", "")
                    print(f"\nRunning tests for {problem_name} ({difficulty})")
                    runner = ProblemRunner(difficulty, problem_name)
                    try:
                        if not runner.run():
                            all_passed = False
                            failed_problems.append(f"{problem_name} ({difficulty})")
                    except Exception as e:
                        print(f"Error running tests for {problem_name}: {e}")
                        all_passed = False
                        failed_problems.append(f"{problem_name} ({difficulty})")

    if all_passed:
        i_am_cool()
    else:
        print("\nYOU BROKE SOMETHING!!!!!!!!!.")
        print(r"""     .
       ':'
   ___:____     |""/""||
 ,'  /      `.    \  /
 |  o        \___/  |
 ~^~^~^~^~^~^~^~^~^~^~^~^~""")
        print("\nFailed Problems:")
        for problem in failed_problems:
            print(f"\033[91m- {problem}\033[0m")  # Display in red

def i_am_cool():
    print("\nAll tests passed successfully!")
    print("\n🎉🎉🎉 YIPPPEEE!!! 🎉🎉🎉")
    print(r"""
          .
       ':'
   ___:____     |""/""||
 ,'        `.    \  /
 |  O        \___/  |
 ~^~^~^~^~^~^~^~^~^~^~^~^~
    """)

if __name__ == "__main__":
    run_all_tests()