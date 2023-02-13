from graphs.generate_graph import create_graph


def find_paths_going_to_end(graph, identifier):
    print(f"Node: {identifier}")
    for node in graph[identifier]:
        identifier = node
        if identifier != 22:
            find_paths_going_to_end(graph, identifier)
        else:
            print("Exit found")
            return


if __name__ == "__main__":
    graph = create_graph()
    find_paths_going_to_end(graph, 0)

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
