from typing import List

def solution(H: List) -> int:
    blocks: int = 0
    stack: List = []
    for height in H:
        while stack and (height < stack[-1]):
            stack.pop()
        if not stack or (height > stack[-1]):
            blocks += 1
            stack.append(height)
    return blocks
