import subprocess
import sys
def run_shell_command():
    try:
        # Example shell command to run if the condition is met
        result = subprocess.run(['ls','-l'],check=True)  # Replace with your command
        print(result)  # Optional: to see the output of the command
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}. Exiting...")
        sys.exit(1)  # Exit with code 1 if the command fails
def check_counter_and_run_command(counter):
    if counter > 1:
        print(f"Counter is greater than 1: {counter}")
        run_shell_command()  # Run the shell command if condition is met
    else:
        print(f"Counter is less than or equal to 1: {counter}")
if __name__ == "__main__":
    counter_value = 2  # Replace with the actual counter value
    check_counter_and_run_command(counter_value)
