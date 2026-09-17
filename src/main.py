import os
import sys
from src.logic import DataPipeline
from src.utils import save_summary_json

def main():
    print("=" * 60)
    print("      Data Analytics & Automation Pipeline")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "sample_evidence.csv")
    json_output = os.path.join(base_dir, "data", "summary_report.json")
    chart_output = os.path.join(base_dir, "data", "events_chart.png")

    pipeline = DataPipeline(csv_path)

    print("\n[+] Loading & Cleaning Data using Pandas...")
    if not pipeline.load_and_clean_data():
        print("[-] Pipeline failed at data loading stage.")
        sys.exit(1)

    print("[+] Extracting Summary Statistics...")
    stats = pipeline.generate_summary_stats()
    print(f"\n--- Summary Results ---")
    print(f"Total Log Entries Processed: {stats.get('total_records')}")
    print(f"Event Distribution: {stats.get('event_distribution')}")
    print(f"Top Frequent Paths: {stats.get('top_frequent_paths')}")

    print("\n[+] Saving Analysis Report to JSON...")
    if save_summary_json(stats, json_output):
        print(f" [✓] Report saved to: {json_output}")

    print("[+] Generating Visual Analytics Plot...")
    if pipeline.generate_visual_report(chart_output):
        print(f" [✓] Visual Chart saved to: {chart_output}")

    print("\n[✓] Pipeline Process Completed Successfully!")

if __name__ == "__main__":
    main()