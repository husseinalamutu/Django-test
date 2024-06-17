# Assistant

import subprocess
import sys

def run_command(command):
    # Start a subprocess that runs the shell command.
    # stdout and stderr specify that you want to capture the output and errors, respectively.
    # Setting shell=True allows shell features like wildcards, pipelines etc.
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
        sys.exit(process.returncode)

    return stdout.decode('utf-8')

def check_migration_conflicts(feature_branch, main_branch='main'):
    # Checkout main branch and apply migrations
    run_command(f"git checkout {main_branch}")
    run_command("python manage.py migrate")

    # Checkout feature branch
    run_command(f"git checkout {feature_branch}")

    # Try to apply migrations on the feature branch
    output = run_command("python manage.py migrate --dry-run")
    if "Conflicting migrations detected" in output:
        print("Migration conflict detected.")
        sys.exit(1)
    else:
        print("No migration conflicts detected.")

# This conditional statement ensures that the script is being executed directly
if __name__ == '__main__':
    feature_branch = sys.argv[1]
    main_branch = 'main' if len(sys.argv) < 3 else sys.argv[2]
    check_migration_conflicts(feature_branch, main_branch)