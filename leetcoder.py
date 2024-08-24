from problem_menu import ProblemMenu
from problem_runner import ProblemRunner

def main():
    try:
        while True:
            problems = ProblemMenu.list_problems()
            ProblemMenu.display_menu(problems)
            
            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= len(problems):
                difficulty, problem_name = problems[choice - 1]
                runner = ProblemRunner(difficulty, problem_name)
                runner.run()
                input("\nPress Enter to return to the menu...")  
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nBye 🥺...")

if __name__ == "__main__":
    main()