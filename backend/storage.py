# Write file
def save_to_file(filename: str, data: str) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
        return True
    except Exception:
        return False

#Read file
def load_from_file(filename: str) -> str | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception:
        return None