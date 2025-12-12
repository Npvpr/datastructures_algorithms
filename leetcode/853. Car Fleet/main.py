def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    # We want to iterate from right to left(highest to lowest position) because cars on the right side of your current car might not go with same speed till target,
    # they might have to slow down when collided with the further cars
    # The right side cars are not trying to catch with left side cars, the left side cars the ones trying to catch up
    pair.sort(reverse=True)

    stack = []

    for p, s in pair:
        # Time required to arrive the target
        t = (target - p) / s

        # If left car catch up with right car before or at the target, it means right car is slower than the left car
        # Only rightmost car with same positon should be left in stack (the fleet travels with the minimum speed)
        if not stack or t > stack[-1]:
            stack.append(t)

    return len(stack)


assert carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
assert carFleet(10, [3], [3]) == 1
assert carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
print("All tests passed!")
