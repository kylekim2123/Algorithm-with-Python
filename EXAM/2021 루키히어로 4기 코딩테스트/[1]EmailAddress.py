from typing import Dict, List


def get_lower_front_of_email(name: str) -> str:
    HYPHEN: str = '-'
    EMPTY: str = ''
    COUNT_OF_TRUNCATED_LAST_NAME: int = 8

    name_parts: List[str] = name.split()
    first: str = name_parts[0]
    last: str = name_parts[-1].replace(HYPHEN, EMPTY)[:COUNT_OF_TRUNCATED_LAST_NAME]
    front_of_email: str = f'{first}.{last}'
    return front_of_email.lower()


def check_duplication(front: str, fronts: Dict[str, int]) -> str:
    if front in fronts:
        fronts[front] += 1
        front += str(fronts[front])
    else:
        fronts[front] = 1
    return front


def solution(S: str, C: str) -> str:
    SPLIT_STANDARD: str = '; '
    
    C = C.lower()
    names: List[str] = S.split(SPLIT_STANDARD)
    fronts: Dict[str, int] = {}
    result: List[str] = []

    for name in names:
        front: str = get_lower_front_of_email(name)
        front = check_duplication(front, fronts)
        email_address: str = f'{front}@{C}.com'
        form: str = f'{name} <{email_address}>'
        result.append(form)

    return SPLIT_STANDARD.join(result)
