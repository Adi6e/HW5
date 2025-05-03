import random
import string

def generate_code():
    # Генерируем код в формате "AAAAA-BBBBB-CCCCC-DDDDD-EEEEE"
    segments = []
    for _ in range(5):  # 5 сегментов
        segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        segments.append(segment)
    return '-'.join(segments)

def generate_codes(n):
    return [generate_code() for _ in range(n)]

def save_codes_to_file(codes, filename):
    with open(filename, 'w') as file:
        for code in codes:
            file.write(code + '\n')

if __name__ == "__main__":
    n = int(input("Введите количество кодов для генерации: "))
    codes = generate_codes(n)
    save_codes_to_file(codes, 'codes.txt')
    print(f"{n} кодов успешно сгенерированы и сохранены в 'codes.txt'.")