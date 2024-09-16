import json

from pygments import highlight, lexers, formatters


def pretty_print(data):
    # parse JSON
    parsed_json = json.loads(data.replace("'", '"'))

    # pretty print JSON with syntax highlighting
    formatted_json = json.dumps(parsed_json, indent=4)
    colorful_json = highlight(formatted_json,
                          lexers.JsonLexer(),
                          formatters.TerminalFormatter())

    return colorful_json

