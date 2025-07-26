# test_summary.py

from climate_agent.summary import generate_summary_from_store

if __name__ == "__main__":
    summary = generate_summary_from_store()
    print("\n🔎 Summary:\n")
    print(summary)
