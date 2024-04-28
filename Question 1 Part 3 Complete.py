import random

def generate_reel():
    reel = []
    # Add 19 A, B, or C symbols
    reel.extend(['A'] * 19)
    reel.extend(['B'] * 19)
    reel.extend(['C'] * 19)
    random.shuffle(reel)
    # Insert 3 consecutive X symbols at a random position
    x_position = random.randint(0, len(reel) - 3)
    reel = reel[:x_position] + ['X', 'X', 'X'] + reel[x_position:]
    return reel
generate_reel()

check_your_work = []

def simulate_attempts(attempts):
    count = 0
    for i in range(attempts):
        reels = [generate_reel() for i in range(3)]
        # Generate 3 separate random reels and add them to a list.
        for j in range(len(reels[0]) - 2):
            k = random.randint(0, 56)
            # Find a random point in the list and save it to a variable to be used as an index.
            total_X = reels[0][k:k+3].count('X')
            total_X += reels[1][k:k+3].count('X')
            total_X += reels[2][k:k+3].count('X')
            # Count the total 'X's shown in the 3 reels.
            if total_X == 8:
                count += 1
                if len(check_your_work) < 1:
                    check_your_work.append(reels[0][k:k+3])
                    check_your_work.append(reels[1][k:k+3])
                    check_your_work.append(reels[2][k:k+3])
                    # Saves the first instance of success to a variable that was used for debugging.
                    # It adds the successful reel combinations to a list.
            break
    return count

if __name__ == "__main__":
    attempts = int(input("Enter the number of attempts: "))
    result = simulate_attempts(attempts)
    print(f"The window shows 8 total X symbols {result} times out of {attempts} attempts.")
    print(check_your_work)

## When testing I used 1,000,000 attempts as the value I calulated for the probability was 1/36000.
