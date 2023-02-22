from app import App


def main():
    print("BEGIN")
    app: App = App()
    try:
        app.run()
    finally:
        app.close()
    print("END")


if __name__ == "__main__":
    main()
