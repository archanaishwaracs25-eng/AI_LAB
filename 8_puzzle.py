import heapq


initial = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

print("Initial State:", initial)
print("Goal State:", goal)

open_list = []
heapq.heappush(open_list, (0, 0, initial, [(initial, "Start")]))
g_cost = {initial: 0}
solution = None

while open_list:
    f, g, current, path = heapq.heappop(open_list)
    
    if current == goal:
        solution = path
        break
        
    if g > g_cost.get(current, float('inf')):
        continue
    
    blank = current.index(0)
    r, c = blank // 3, blank % 3
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    
    for dr, dc, move_name in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc
            new_state = list(current)
            new_state[blank], new_state[new_pos] = new_state[new_pos], new_state[blank]
            neighbor = tuple(new_state)
            
            new_g = g + 1
            if new_g < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_g
                h = sum(1 for i in range(9) if neighbor[i] != 0 and neighbor[i] != goal[i])
                new_f = new_g + h
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [(neighbor, move_name)]))

if not solution:
    print("\nNo solution exists.")
else:
    print(f"\nSOLUTION FOUND! Total moves: {len(solution) - 1}\n")
    for step, (state, move) in enumerate(solution):
        h = sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])
        print(f"Step {step} | Move: {move} | g(n)={step}, h(n)={h}, f(n)={step+h}")
        print(" ".join("_" if x == 0 else str(x) for x in state[0:3]))
        print(" ".join("_" if x == 0 else str(x) for x in state[3:6]))
        print(" ".join("_" if x == 0 else str(x) for x in state[6:9]))
        print("-" * 25)
    print("Goal reached!")
