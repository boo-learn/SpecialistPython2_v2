def goto(num:int):
    if visited[num]:
        return "Сan go to the"
    else:
        return "Can't go to the"


home = 0
bank = 7
shop = 2

visited = dfs(graph, start_vertex=home)
# print(visited)
print(f"{goto(bank)} bank")
print(f"{goto(shop)} shop")
