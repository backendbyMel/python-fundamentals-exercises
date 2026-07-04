def detect_data_type(value):
    try:
        int(value)
        return "int"
    except ValueError:
        pass

    try:
        float(value)
        return "float"
    except ValueError:
        pass

    if value.lower() in ("true", "false"):
        return "bool"

    return "str"


def main():
    user_input = input("Enter your data: ")
    print(f"Detected data type: {detect_data_type(user_input)}")


if __name__ == "__main__":
    main()