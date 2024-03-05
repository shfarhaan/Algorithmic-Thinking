def analyze_list(num_list):
  """
  This function calculates the sum of squares of even numbers excluding prime indices
  and the product of non-prime odd numbers in a given list.

  Args:
      num_list: A list of integers.

  Returns:
      A tuple containing two integers:
          - Sum of squares of selected even numbers.
          - Product of non-prime odd numbers.
  """
  sum_of_squares = 0
  product_of_non_primes = 1
  prime_indices = [2, 3, 5]  # List of initial prime numbers

  for i, num in enumerate(num_list, start=1):
    if num % 2 == 0 and i not in prime_indices:
      sum_of_squares += num**2
    elif num % 2 != 0 and not is_prime(num):
      product_of_non_primes *= num

    # Efficiently update prime_indices as we encounter new primes
    if is_prime(i) and i not in prime_indices:
      prime_indices.append(i)

  return sum_of_squares, product_of_non_primes

def is_prime(num):
  """
  This function checks if a number is prime (greater than 1 and not divisible by smaller numbers).

  Args:
      num: An integer.

  Returns:
      True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

# Example usage
input_list = [3, 5, 2, 4, 9, 6]
sum_of_squares, product_of_non_primes = analyze_list(input_list)

print("Sum of squares of selected even numbers:", sum_of_squares)
print("Product of non-prime odd numbers:", product_of_non_primes)
