# arabic_quality_checker.py
# Author: BOUTEROUATA Issam Salah Eddine
# Description: A simple tool to check the quality of Arabic text for AI training data.
# This script checks for common issues like mixed language, missing diacritics, 
# repeated words, and very short sentences.

import re

def check_language_mixing(text):
    """Check if the text mixes Arabic with other scripts (e.g., Latin characters)."""
    latin_chars = re.findall(r'[a-zA-Z]', text)
    arabic_chars = re.findall(r'[\u0600-\u06FF]', text)
    
    if len(arabic_chars) == 0:
        return {"issue": "no_arabic", "message": "No Arabic characters found in the text."}
    
    mixing_ratio = len(latin_chars) / (len(arabic_chars) + len(latin_chars))
    
    if mixing_ratio > 0.2:
        return {"issue": "high_mixing", "message": f"High language mixing detected. {round(mixing_ratio*100)}% non-Arabic characters."}
    elif mixing_ratio > 0.05:
        return {"issue": "moderate_mixing", "message": f"Some language mixing detected ({round(mixing_ratio*100)}% non-Arabic)."}
    else:
        return {"issue": "none", "message": "Language consistency looks good."}


def check_repeated_words(text):
    """Check for consecutive repeated words, which is a common annotation error."""
    words = text.split()
    repeated = []
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            repeated.append(words[i])
    
    if repeated:
        return {"issue": "repeated_words", "message": f"Repeated words found: {set(repeated)}"}
    return {"issue": "none", "message": "No repeated consecutive words found."}


def check_text_length(text, min_words=5, max_words=200):
    """Check if the text is within an acceptable length for AI training."""
    word_count = len(text.split())
    
    if word_count < min_words:
        return {"issue": "too_short", "message": f"Text is too short ({word_count} words). Minimum is {min_words}."}
    elif word_count > max_words:
        return {"issue": "too_long", "message": f"Text is very long ({word_count} words). Consider splitting it."}
    else:
        return {"issue": "none", "message": f"Text length is acceptable ({word_count} words)."}


def check_special_characters(text):
    """Flag unusual special characters that shouldn't appear in clean Arabic text."""
    unusual = re.findall(r'[^\u0600-\u06FF\u0020-\u007E\u060C\u061B\u061F\u0640]', text)
    unusual = [c for c in unusual if c not in ['\n', '\t', ' ']]
    
    if unusual:
        return {"issue": "unusual_chars", "message": f"Unusual characters found: {list(set(unusual))}"}
    return {"issue": "none", "message": "No unusual special characters found."}


def run_quality_check(text):
    """Run all quality checks on a given Arabic text and return a report."""
    print("=" * 60)
    print("Arabic Text Quality Report")
    print("=" * 60)
    print(f"Input text: {text[:80]}{'...' if len(text) > 80 else ''}")
    print("-" * 60)

    checks = [
        ("Language Mixing", check_language_mixing(text)),
        ("Repeated Words", check_repeated_words(text)),
        ("Text Length", check_text_length(text)),
        ("Special Characters", check_special_characters(text)),
    ]
    
    issues_found = 0
    for check_name, result in checks:
        status = "✅ OK" if result["issue"] == "none" else "⚠️  ISSUE"
        if result["issue"] != "none":
            issues_found += 1
        print(f"{check_name:25} | {status} | {result['message']}")
    
    print("-" * 60)
    if issues_found == 0:
        print("Overall: Text passed all quality checks.")
    else:
        print(f"Overall: {issues_found} issue(s) detected. Review before using in AI training.")
    print("=" * 60)


# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Clean Arabic text
    sample_text_1 = "الذكاء الاصطناعي يغير العالم بسرعة كبيرة وسوف يستمر في التطور في السنوات القادمة"
    
    # Example 2: Text with issues (mixed language, repeated word)
    sample_text_2 = "هذا النص النص يحتوي على على كلمات مكررة وأيضا some English words mixed in"
    
    # Example 3: Very short text
    sample_text_3 = "مرحبا"

    print("\n--- Test 1: Clean Text ---")
    run_quality_check(sample_text_1)
    
    print("\n--- Test 2: Text with Issues ---")
    run_quality_check(sample_text_2)
    
    print("\n--- Test 3: Short Text ---")
    run_quality_check(sample_text_3)
