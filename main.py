import random
import string
import pyperclip

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password based on given settings."""
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_strength(length, use_upper, use_digits, use_symbols):
    """Rate the strength of the password configuration."""
    score = 0
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if use_upper:
        score += 1
    if use_digits:
        score += 1
    if use_symbols:
        score += 1

    if score <= 2:
        return "⚠️  Weak"
    elif score <= 3:
        return "🟡 Moderate"
    elif score <= 4:
        return "🟢 Strong"
    else:
        return "🔒 Very Strong"


def print_banner():
    print("=" * 45)
    print("      🔐 Random Password Generator")
    print("=" * 45)


def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Please enter 'y' or 'n'.")


def main():
    print_banner()

    # Get password length
    while True:
        try:
            length = int(input("\nEnter password length (8–64) [default: 16]: ").strip() or 16)
            if 8 <= length <= 64:
                break
            else:
                print("  Please enter a number between 8 and 64.")
        except ValueError:
            print("  Invalid input. Please enter a number.")

    print()
    use_upper   = get_yes_no("Include uppercase letters?")
    use_digits  = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include symbols (!@#$...)?")

    # Generate password
    try:
        password = generate_password(length, use_upper, use_digits, use_symbols)
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return

    strength = get_strength(length, use_upper, use_digits, use_symbols)

    print("\n" + "=" * 45)
    print(f"  Generated Password:\n\n    {password}\n")
    print(f"  Strength : {strength}")
    print(f"  Length   : {length} characters")
    print("=" * 45)

    # Copy to clipboard
    copy = get_yes_no("\nCopy password to clipboard?")
    if copy:
        try:
            pyperclip.copy(password)
            print("  ✅ Password copied to clipboard!")
        except Exception:
            print("  ⚠️  Could not copy (clipboard not available in this environment).")

    print("\nStay safe! 🛡️\n")


if __name__ == "__main__":
    main()
