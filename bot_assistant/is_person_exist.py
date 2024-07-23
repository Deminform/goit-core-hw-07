def is_person_exist(name: str,  contacts: list) -> bool:
    for person in contacts:
        if person['name'].lower() == name.lower():
            return True
