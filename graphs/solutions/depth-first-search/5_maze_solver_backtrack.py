from graphs.generate_graph import create_graph


def find_paths_going_to_end(graph, identifier, nodes_visited, depth, backtrack):
    print("Current node: ", identifier)
    nodes_visited.append(identifier)
    depth += 1

    if identifier in graph:
        for node in graph[identifier]:
            if node not in nodes_visited:
                new_identifier = node
                # print(" " * depth + "Next node:", new_identifier, "depth:", depth)
                if new_identifier != 22:
                    find_paths_going_to_end(graph, new_identifier, nodes_visited, depth, backtrack)
                else:
                    print(f"Exit found at node {new_identifier}")

                    backtrack.append(new_identifier)
                    backtrack.append(identifier)
                    return backtrack

    if backtrack:
        backtrack.append(identifier)
    return backtrack


if __name__ == "__main__":
    graph = create_graph()
    backtrack = find_paths_going_to_end(graph, 0, [], 0, [])
    print("Path found:", list(reversed(backtrack)))
