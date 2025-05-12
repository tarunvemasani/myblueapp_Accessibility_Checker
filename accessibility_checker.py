# accessibility_checker.py

def check_accessibility_issues(log_file_path):
    issues_found = []

    with open(log_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip().lower()

        # Scenario 1: Button with no label
        if line == "button":
            issues_found.append(f"Issue: Missing button label at line {i + 1}")

        # Scenario 1: Bad button text
        if line == "click" or line == "go":
            issues_found.append(f"Issue: Non-descriptive button text '{line}' at line {i + 1}")

        # Scenario 3: Graphic with no alt
        if line == "graphic":
            issues_found.append(f"Issue: Missing image alternative text at line {i + 1}")

        # Scenario 2: Heading Skipped (H1 to H3 directly)
        if "heading level 1" in line and i + 1 < len(lines):
            next_line = lines[i + 1].strip().lower()
            if "heading level 3" in next_line:
                issues_found.append(f"Issue: Skipped heading level from H1 to H3 at line {i + 2}")

        # Scenario 1: Link not descriptive
        if "link view" in line or "link click here" in line:
            issues_found.append(f"Issue: Non-descriptive link text at line {i + 1}")

    return issues_found


if __name__ == "__main__":
    log_file = "nvda_log.txt"  # Update your NVDA exported file path here
    results = check_accessibility_issues(log_file)

    if results:
        print("\nAccessibility Issues Found:\n")
        for issue in results:
            print(issue)
    else:
        print("✅ No obvious accessibility issues found!")
