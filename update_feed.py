#!/usr/bin/env python3
"""
يسحب بيانات بورصة الكويت، يحولها لـ JSON، ويحفظها في stocks.json
عدّل رابط الـ API وأسماء الحقول حسب الحاجة.
"""

import requests, json, pathlib, datetime

API_URL = "https://example.com/boursa_api"   # ← عدّلها

def main():
    data = requests.get(API_URL, timeout=10).json()
    # لو API يرجّع CSV أو XML، عالج هنا...
    pathlib.Path("stocks.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    )
    print("✅ stocks.json updated", datetime.datetime.now())

if __name__ == "__main__":
    main()
