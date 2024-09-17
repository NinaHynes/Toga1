import toga


def button_handler(widget):
    print("hello, wow, you're looking good today")


def build(app):
    box = toga.Box()

    button = toga.Button("Hello world", on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App("First App", "org.beeware.toga.tutorial", startup=build)


if __name__ == "__main__":
    main().main_loop()