# Automated Commit GitHub

This project is designed to automate the process of committing changes to a GitHub repository. It simplifies the workflow by automatically detecting changes, staging them, and committing with a predefined message. This can be particularly useful for continuous integration and deployment pipelines.

## Features

- Automatic change detection
- Predefined commit messages
- Integration with CI/CD pipelines
- Easy configuration

## Usage

1. Clone the repository.
2. Configure the bash file
3. Setup your task scheduler

## Setup task Scheduler

1. Open Task Scheduler
Press Win + R, type taskschd.msc, and press Enter.
In the Task Scheduler window, click Create Basic Task on the right-hand side.

2. Set Up the Basic Task
Name the Task: Give your task a name (e.g., "Run Python Script") and optionally add a description.
Trigger: Choose when the task should run:
Daily
Weekly
At startup, etc.
Action: Select Start a Program.

Program/Script:
If using a batch file, browse to path-to-bat-file\run_script_gitpush_automated.bat.

If running the script directly, enter the full path to your Python executable and add the script as an argument, like this:
Program/script: C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\python.exe
Add arguments: "C:\Scripts\script.py"

4. Set Additional Settings
Click Finish, and the task will be created.
Open the task properties and ensure Run with highest privileges is checked if needed (especially for scripts requiring admin access).
Confirm your task is configured correctly by running it manually.
Test the Task
To test the setup:

Select the task in Task Scheduler.
Click Run in the right-hand menu.
If the task runs successfully, your cron job equivalent is ready to go!

## Requirements

- Python 3.x
- Git

## Installation

```bash
git clone https://github.com/yourusername/AutomatedCommitGithub.git
cd AutomatedCommitGithub
pip install -r requirements.txt
```



## License

This project is licensed under the MIT License.
