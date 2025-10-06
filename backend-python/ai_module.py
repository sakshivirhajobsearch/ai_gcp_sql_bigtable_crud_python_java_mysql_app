# ai_module.py

def process_text(text):
    return {
        "original": text,
        "length": len(text),
        "processed": text.upper()
    }

def analyze_numbers(numbers):
    if not numbers:
        numbers = []
    return {
        "count": len(numbers),
        "sum": sum(numbers) if numbers else 0,
        "max": max(numbers) if numbers else None,
        "min": min(numbers) if numbers else None
    }
