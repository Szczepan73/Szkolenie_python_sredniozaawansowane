# pip install click

import os
import click ### https://github.com/pallets/click


# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for _ in range(count):
#         click.echo(f"Hello, {name}!")
#
# if __name__ == '__main__':
#     hello()



# import click
# import time
#
# @click.command()
# @click.option('--count', default=10, help='Number of iterations.')
# def process(count):
#     """Simulate a long-running task."""
#     with click.progressbar(length=count, label='Processing...') as bar:
#         for i in range(count):
#             time.sleep(0.1)  # Simulate some work
#             bar.update(1)
#
# if __name__ == "__main__":
#     process()




# import click
#
# @click.command()
# @click.option('--username', prompt='Your username', help='The username for login.')
# @click.password_option(help='The password for login.')
# def login(username, password):
#     """Login command that prompts for username and password."""
#     click.echo(f'Username: {username}')
#     click.echo(f'Password entered successfully! {password}')
#
# if __name__ == "__main__":
#     login()


# import click
#
# @click.command()
# def colored_text():
#     """Print colored text."""
#     click.echo(click.style('This is a red message!', fg='red'))
#     click.echo(click.style('This is a green message!', fg='green', bold=True))
#     click.echo(click.style('This is a blue message!', fg='blue', bg='yellow'))
#
# if __name__ == "__main__":
#     colored_text()



# import click
# import json
#
# @click.command()
# @click.option('--config', default='config.json', help='Path to the configuration file.')
# def read_config(config):
#     """Read configuration from a file."""
#     try:
#         with open(config, 'r') as f:
#             config_data = json.load(f)
#             click.echo(f"Configuration: {config_data}")
#     except FileNotFoundError:
#         click.echo("Configuration file not found.")
#
# if __name__ == "__main__":
#     read_config()



# Before run export USER_NAME=Alice
# import click
# import os
#
# @click.command()
# @click.option('--username', envvar='USER_NAME', help='Your username.')
# def greet_user(username):
#     """Greet the user with their username."""
#     if username:
#         click.echo(f"Hello, {username}!")
#     else:
#         click.echo("Hello, guest!")
#
# if __name__ == "__main__":
#     greet_user()