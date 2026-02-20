# arabic-text-quality-checker
Python NLP tool to detect repetition, mixed language usage, and structural issues in Arabic text.

# Arabic Dialect Classifier

**Author:** BOUZEROUATA Issam Salah Eddine  
**Language:** Python 3  
**Topic:** Arabic NLP — Dialect Detection

---

## What This Project Does

Arabic is not one language — it is a family of spoken dialects layered on top of Modern Standard Arabic (MSA). Egyptian Arabic, Levantine Arabic, Gulf Arabic, and Maghrebi Arabic each have their own vocabulary, grammar patterns, and informal markers that differ significantly from each other and from the formal MSA taught in schools.

This project is a rule-based dialect classifier. Given an Arabic text, it scans for vocabulary markers associated with each major dialect and returns the most likely match along with a breakdown of scores.

The five dialect groups covered are:
- **Egyptian (Masri)**
- **Levantine (Shami)**
- **Gulf (Khaleeji)**
- **Maghrebi (Darija)**
- **Modern Standard Arabic (MSA / Fusha)**

---

## Why Dialect Detection Matters for AI

Most Arabic NLP tools — including many large language models — are trained primarily on MSA. This creates a significant blind spot: when a real user in Cairo types in Egyptian dialect, or a user in Morocco writes in Darija, the model may struggle to understand or respond naturally. 

For AI personalization systems, dialect detection is a valuable preprocessing step. Knowing which dialect the user is writing in allows the system to:
- Route the input to a more appropriate language model or fine-tuned version
- Tag training data with dialect labels for better future training
- Adjust the dialect of the AI's response to match the user's own speech patterns

---

## Approach

This implementation is **keyword-based (rule-based)**, not machine-learning-based. Each dialect has a curated list of vocabulary markers — words or expressions that are distinctive to that dialect. The classifier counts how many of these markers appear in the input text and scores each dialect accordingly.

**Limitations of this approach:**
- Short texts with few dialect markers may not classify well
- Code-switching (mixing dialects) can confuse the scorer
- The marker lists are small — a production system would use a much larger lexicon and a trained ML model (e.g., a fine-tuned AraBERT or CAMeL model)

Despite these limitations, this approach is interpretable, requires no dependencies, and works well as a lightweight pre-filter.

---

## How to Use It

### Requirements
- Python 3.6+
- No external libraries needed

### Run the script
```bash
python arabic_dialect_classifier.py
```

The script runs five built-in test cases — one per dialect — and prints a classification report for each.

### Use it in your own code

```python
from arabic_dialect_classifier import classify_dialect

text = "شو بدك تاكل هلق؟"
dialect, scores = classify_dialect(text)
print(f"Detected dialect: {dialect}")
```

---

## Example Output

```
Arabic Dialect Classification Report
============================================================
Input: شو بدك تاكل هلق؟ روح وين ما بدك بس رجع منيح
------------------------------------------------------------
Keyword match scores:
  Levantine                           | 5 █████
  Egyptian                            | 0
  Gulf                                | 0
  Maghrebi                            | 0
  Modern Standard Arabic (MSA)        | 0
------------------------------------------------------------
Best match: Levantine
```

---

## Future Plans

- Expand the marker lexicons with a larger, community-sourced word list
- Add support for loading custom marker lists from a JSON file
- Experiment with a trained classifier using a labeled Arabic dialect dataset (e.g., MADAR or NADI corpus)
- Add confidence scores

---

## Project Status
Beginner project — rule-based, no ML dependencies. Tested on manual examples.
