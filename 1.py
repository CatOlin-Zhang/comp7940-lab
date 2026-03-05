def count_vowels(text):
    """
    统计字符串中英文元音的个数（不区分大小写）。
    元音包括：a, e, i, o, u
    """
    # 定义元音集合，包含小写和大写，或者统一转为小写比较
    vowels = "aeiou"
    count = 0

    # 将输入转换为小写以便统一处理
    text_lower = text.lower()

    for char in text_lower:
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    # 获取用户输入
    user_input = input("请输入一个字符串: ")

    # 调用函数
    result = count_vowels(user_input)

    # 输出结果
    print(f"字符串 '{user_input}' 中共有 {result} 个元音字母。")