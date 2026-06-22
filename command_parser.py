from commands import COMMAND_MAP

def parse_command(text):

    text = text.lower().strip()

    return COMMAND_MAP.get(text, None)