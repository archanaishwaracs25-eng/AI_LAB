stack = [] 
visited = set() 
initial_state = [1, 2, 3, 4, 0, 6, 7, 5, 8] 
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] 

stack.append(initial_state) 


print("Initial State:", initial_state)

while(stack): 
    current = stack.pop() 
    
    if(current == goal_state): 
        print("Goal State Found:", current)
        break 
        
    if tuple(current) in visited: 
        continue
        
    visited.add(tuple(current))
    
    zero_idx = current.index(0)
    row, col = zero_idx // 3, zero_idx % 3
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            neighbor = list(current)
            neighbor[zero_idx], neighbor[new_idx] = neighbor[new_idx], neighbor[zero_idx]
            
            if tuple(neighbor) not in visited:
                stack.append(neighbor)
