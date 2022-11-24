from taipy import Gui

# not no empty spaces at the beginning of the markdown
# markdown must start from the baseline

page = """
### Hello world
"""
# Gui(page=page).run(dark_mode=False)

# you can specify the port number in the run(port=xxxx)
# its by default 5000
Gui(page="Intro to Taipy").run(dark_mode=True)

