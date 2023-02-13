from graphs.generate_graph import create_graph


def find_paths_going_to_end(graph, identifier, nodes_visited, depth):
    print("Current node: ", identifier)
    nodes_visited.append(identifier)
    depth += 1

    if identifier in graph:
        for node in graph[identifier]:
            if node not in nodes_visited:
                new_identifier = node
                print(" " * depth + "Next node:", new_identifier, "depth:", depth)
                if new_identifier != 22:
                    find_paths_going_to_end(graph, new_identifier, nodes_visited, depth)
                else:
                    print(f"Exit found at node {new_identifier}")
                    return
            else:
                print(f"Already passed by {node}, so moving on")
    else:
        print("That's a end")


if __name__ == "__main__":
    graph = create_graph()
    find_paths_going_to_end(graph, 0, [], 0)

    """
    Traceback (most recent call last):
        File "maze_solver_step_3.py", line 74, in <module>
        find_paths_going_to_end(graph, 0)
        File "maze_solver_step_3.py", line 69, in find_paths_going_to_end
        find_paths_going_to_end(graph, identifier)
        File "maze_solver_step_3.py", line 69, in find_paths_going_to_end
        find_paths_going_to_end(graph, identifier)
        File "maze_solver_step_3.py", line 69, in find_paths_going_to_end
        find_paths_going_to_end(graph, identifier)
        [Previous line repeated 995 more times]
        File "maze_solver_step_3.py", line 68, in find_paths_going_to_end
        if identifier != 22:
        RecursionError: maximum recursion depth exceeded in comparison
    """
