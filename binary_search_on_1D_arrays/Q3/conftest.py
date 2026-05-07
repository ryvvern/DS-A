# conftest.py
import pytest

PASS = "🦄"
FAIL = "🫏"
results = []

def pytest_runtest_logreport(report):
    if report.when == "call":
        name = report.nodeid.split("::")[-1].replace("test_", "").replace("_", " ")
        if report.passed:
            results.append(f"  {PASS}  {name}")
        elif report.failed:
            results.append(f"  {FAIL}  {name}")

def pytest_sessionfinish(session, exitstatus):
    passed = sum(1 for r in results if "🦄" in r)
    failed = sum(1 for r in results if "🫏" in r)
    total = passed + failed

    print("\n")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("   search element in rotated sorted array — test run")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for r in results:
        print(r)
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"   {passed}/{total} passed", "🎉" if failed == 0 else "💀")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")