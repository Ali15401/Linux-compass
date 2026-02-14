import logging
import os
import json
from datetime import datetime

# Setup logging configuration
logging.basicConfig(filename='compass.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Compass:
    def __init__(self):
        self.command_history = []
        self.load_config()

    def load_config(self):
        """Load configuration options from a file."""
        config_file = 'config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        else:
            logging.warning("Configuration file not found. Using default settings.")
            self.config = {'default_direction': 'North'}

    def log_command(self, command):
        """Log executed commands."""
        logging.info(f"Executed command: {command}")
        self.command_history.append(command)

    def validate_input(self, user_input):
        """Validate user input."""
        if user_input not in ['North', 'South', 'East', 'West']:
            logging.error("Invalid direction input.")
            raise ValueError("Invalid direction. Please enter North, South, East, or West.")

    def navigate(self, direction):
        """Execute navigation based on direction."""
        self.validate_input(direction)
        self.log_command(f"Navigate {direction}")
        print(f"Navigating {direction}...")

    def show_history(self):
        """Show command history."""
        print("Command History:")
        for command in self.command_history:
            print(command)

if __name__ == "__main__":
    compass = Compass()
    while True:
        user_input = input("Enter a direction (North, South, East, West) or 'history' to view command history: ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'history':
            compass.show_history()
        else:
            try:
                compass.navigate(user_input)
            except ValueError as e:
                print(e)