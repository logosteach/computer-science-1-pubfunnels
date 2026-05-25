#!/usr/bin/env python3
"""
create_unit_desc.py
Generates lesson description HTML files from a template.
"""

from pathlib import Path


def main():
    # === PATH SETUP ===
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent  # templates/python/
    templates_dir = script_dir.parent  # templates/

    # Template is in the 'templates' folder
    template_path = templates_dir / "pub_funnels_description.html"
    output_dir = script_dir / "output"  # Output: templates/python/output

    # === DEBUG PRINTS ===
    DEBUG_PATHS = True
    if DEBUG_PATHS:
        print("=" * 80)
        print("PATH DEBUG INFORMATION")
        print("=" * 80)
        print(f"Script path          : {script_path}")
        print(f"script_dir           : {script_dir}")
        print(f"templates_dir        : {templates_dir}")
        print(f"template_path        : {template_path}")
        print(f"output_dir           : {output_dir}")
        print("-" * 80)
        print(f"template exists      : {template_path.exists()}")
        print(f"output_dir exists    : {output_dir.exists()}")
        print("=" * 80)

    # ==================== LESSONS ====================
    lessons = [
        ("1", "Boolean Values and Variables"),
        ("2", "Comparator Operators"),
        ("3A", "Compound Conditional Expressions"),
        ("3B", "Short-Circuit Evaluation"),
        ("4A", "IF, ELIF, and ELSE blocks"),
        ("4B", "Nested IF Blocks"),
        ("5", "Truthy and False"),
        ("6", "Common Pitfalls and Best Practices"),
        ("7", "Ternary Conditional Expressions"),
        ("8", "Practical, Real World Problems"),
    ]
    # ================================================

    if not template_path.exists():
        print(f"❌ Error: Template not found at:\n   {template_path}")
        print("\nFiles in templates folder:")
        for f in templates_dir.glob("*.html"):
            print(f"   - {f.name}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    print(f"✅ Template loaded: {template_path.name}")
    print(f"📁 Output directory: {output_dir}\n")

    for lesson_num, lesson_title in lessons:
        # Fixed filename generation for both numbers and "3A", "4B", etc.
        clean_num = lesson_num.replace("A", "").replace("B", "").zfill(2)
        filename = f"lesson_{clean_num}_{lesson_num}_desc.html"

        output_path = output_dir / filename

        # Replace placeholder in template
        content = template_content.replace("LESSON_TITLE_HERE", lesson_title)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Created: {filename}  →  {lesson_title}")

    print("\n🎉 All lesson files generated successfully in 'python/output'!")


if __name__ == "__main__":
    main()
