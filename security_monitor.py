from collections import Counter
import json
import re
import time


LOG_FILE = "auth.log"
REPORT_FILE = "security_report.json"
BRUTE_FORCE_THRESHOLD = 3


def analyze_log(filename):
    failed_attempts = Counter()
    total_failed = 0
    total_successful = 0

    with open(filename, "r") as file:
        for line in file:
            if "Failed password" in line:
                total_failed += 1

                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                if match:
                    ip_address = match.group(1)
                    failed_attempts[ip_address] += 1

            elif "Accepted password" in line:
                total_successful += 1

    return failed_attempts, total_failed, total_successful


def generate_report(failed_attempts, total_failed, total_successful):
    suspicious_sources = {
        ip: attempts
        for ip, attempts in failed_attempts.items()
        if attempts >= BRUTE_FORCE_THRESHOLD
    }

    report = {
        "total_failed_logins": total_failed,
        "total_successful_logins": total_successful,
        "unique_failed_sources": len(failed_attempts),
        "potential_brute_force_sources": suspicious_sources
    }

    with open(REPORT_FILE, "w") as file:
        json.dump(report, file, indent=4)

    return report


def print_report(report, elapsed_time):
    print("=" * 50)
    print("Linux Security Monitoring Tool")
    print("=" * 50)

    print("\nSecurity Event Summary")
    print("-" * 50)
    print(f"Failed login attempts: {report['total_failed_logins']}")
    print(f"Successful login attempts: {report['total_successful_logins']}")
    print(f"Unique source addresses: {report['unique_failed_sources']}")

    print("\nPotential Brute-Force Activity")
    print("-" * 50)

    suspicious = report["potential_brute_force_sources"]

    if suspicious:
        for ip, attempts in suspicious.items():
            print(f"{ip}: {attempts} failed attempts")
    else:
        print("No potential brute-force sources detected.")

    print(f"\nAnalysis duration: {elapsed_time:.4f} seconds")
    print(f"JSON report saved to: {REPORT_FILE}")
    print("\nAnalysis complete.")


def main():
    start_time = time.time()

    try:
        failed_attempts, total_failed, total_successful = analyze_log(
            LOG_FILE
        )

        report = generate_report(
            failed_attempts,
            total_failed,
            total_successful
        )

        elapsed_time = time.time() - start_time

        print_report(report, elapsed_time)

    except FileNotFoundError:
        print(f"Error: Could not find {LOG_FILE}")


if __name__ == "__main__":
    main()