# 簡単な計算機プログラム
def add(a, b):
    """二つの数値を足し算する関数"""
    return a + b

def multiply(a, b):
    """二つの数値を掛け算する関数"""
    return a * b

def main():
    """メイン関数"""
    print("簡単な計算機です")
    result1 = add(5, 3)
    result2 = multiply(4, 6)
    print(f"5 + 3 = {result1}")
    print(f"4 × 6 = {result2}")

if __name__ == "__main__":
    main()
