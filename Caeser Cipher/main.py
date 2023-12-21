alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    if cipher_direction == "decode" or cipher_direction == "encode":
      for char in start_text:
          #TODO-3: What happens if the user enters a number/symbol/space?
          #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
          #e.g. start_text = "meet me at 3"
          #end_text = "•••• •• •• 3"
          if char.isalpha():
              position = alphabet.index(char)
              new_position = position + shift_amount
              end_text += alphabet[new_position]
          else:
              end_text += char
      print(f"Here's the {cipher_direction}d result: {end_text}")
    else:
      print("Wrong Direction!")
import art

print(art.logo)

start = True
while start == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice = input(
        "Do you want to restart the game? Type 'Yes' or 'No': ").lower()
    if choice == "no":
      start = False