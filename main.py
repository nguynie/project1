def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # Tối ưu hóa kiểm tra đến căn bậc 2 của n
        if n % i == 0:
            return False
    return True  # Đã chuyển ra ngoài vòng lặp

def countPrimes(numbers):
    # Đếm số lượng số nguyên tố trong danh sách
    return sum(1 for num in numbers if isPrime(num))

# Nhận một chuỗi các số nguyên từ người dùng, cách nhau bởi dấu cách
input_str = input("Enter a list of numbers separated by space: ")

# Tách chuỗi thành các chuỗi con và chuyển đổi chúng thành số nguyên
numbers = [int(num) for num in input_str.split()]
print("The list of numbers is:", numbers)

# Test hàm isPrime trên số đầu tiên của danh sách nếu có
if numbers:
    num_to_check = numbers[0]
    if isPrime(num_to_check):
        print(f"{num_to_check} is a prime number.")
    else:
        print(f"{num_to_check} is not a prime number.")

# Sử dụng hàm countPrimes để đếm và in ra kết quả
total_primes = countPrimes(numbers)
print(f"Total number of primes in the list: {total_primes}")