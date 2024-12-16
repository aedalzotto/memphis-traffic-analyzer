from argparse import ArgumentParser
from .graph import Graph

def memphis_ta():
    parser = ArgumentParser(description="Memphis Traffic Analyzer")
    parser.add_argument("SCENARIO_PATH", help="Path to scenario")
    parser.add_argument("APP_ID", nargs='+', type=int, help="Application IDs to build the graph")
    parser.add_argument("--start", nargs=1, type=float, metavar=('START_MS'), help="Start plotting only after START_MS (avoid warm up)", default=[0])
    parser.add_argument("--compare", nargs=2, metavar=('SCENARIO_PATH', 'APP_ID'), help="Compare to other scenario", default=[None, None])
    parser.add_argument("--save", nargs=1, metavar=("PATH"), help="Save graph to PATH", default=[None])
    parser.add_argument("--export", action='store_true', help="Export graph points to stdout", default=False)
    args = parser.parse_args()

    scenario = args.SCENARIO_PATH
    app_id   = args.APP_ID
    start_ms = args.start[0]
    plt_file = args.save[0]
    export   = args.export

    comp_path, comp_id = args.compare
    comp_id = [int(x) for x in comp_id] if comp_id is not None else None

    ta = Graph(scenario, app_id, start_ms, comp_path, comp_id, export)

    if plt_file is None:
        ta.show()
    else:
        ta.save(plt_file)
