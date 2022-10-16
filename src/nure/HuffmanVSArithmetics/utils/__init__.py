from pyfiglet import Figlet


def beautiful_print(text: str, font='standard'):
    preview = Figlet(font=font)
    rendered_text = preview.renderText(text)
    print("\033[01m\033[31m{} \033[0m" .format(rendered_text))
