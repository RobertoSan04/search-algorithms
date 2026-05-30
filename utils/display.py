import sys
import tty
import termios
import os

def clear_console():
    if not sys.stdout.isatty():
        print("\n" + "-" * 40 + "\n")
        return
    os.system("cls" if os.name == "nt" else "clear")

def wait_any_key():
    print("\n  Press any key to continue...")
    # termios/tty raw mode only works on a real TTY; fall back outside one
    # (IDE run console, debugger, piped stdin) to avoid termios.error.
    if not sys.stdin.isatty():
        sys.stdin.readline()
        return
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def _fmt_cost(c):
    return int(c) if c == int(c) else c

def print_graph(graph, start, goal):
    print(f"\nGraph ({len(graph)} nodes)  start: {start}  goal: {goal}")
    print("-" * 40)
    for node, neighbors in graph.items():
        formatted = ", ".join(f"{n}({_fmt_cost(c)})" for n, c in neighbors)
        print(f"  {node} -> {formatted if formatted else '(no edges)'}")

def print_menu(graph, start, goal, algorithms, heuristic=None):
    print("\n" + "=" * 40)
    print("       Search Algorithms Menu")
    print("=" * 40)
    if graph:
        h_tag = "  |  heuristic: yes" if heuristic else ""
        print(f"  Graph: {len(graph)} nodes  |  {start} -> {goal}{h_tag}")
    else:
        print("  Graph: none loaded")
    print("-" * 40)
    print("  g. New graph")
    print("  p. Preloaded graph")
    print("  v. View graph")
    for key, (name, _) in algorithms.items():
        print(f"  {key}. {name}")
    print("  0. Exit")
    print("=" * 40)
