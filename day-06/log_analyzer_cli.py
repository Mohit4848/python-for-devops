import argparse
from collections import Counter


def parse_logs(file_path, level=None):
    counts = Counter()

    with open(file_path, "r") as file:
        for line in file:
            if "INFO" in line:
                counts["INFO"] += 1
            elif "ERROR" in line:
                counts["ERROR"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1

    if level:
        return {level: counts.get(level, 0)}

    return dict(counts)


def write_output(out_file, summary):
    with open(out_file, "w") as file:
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Log Analyzer CLI Tool (DevOps Style)"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file"
    )

    parser.add_argument(
        "--out",
        required=True,
        help="Path to output summary file"
    )

    parser.add_argument(
        "--level",
        choices=["INFO", "ERROR", "WARNING"],
        help="Filter logs by level"
    )

    args = parser.parse_args()

    summary = parse_logs(args.file, args.level)

    print("\nLog Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    write_output(args.out, summary)


if __name__ == "__main__":
    main()
