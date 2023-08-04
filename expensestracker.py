items_list = []
file_path = "expenses.txt"
#========================================================
def remove_alphabets(input_string):
    return ''.join(char for char in input_string if not char.isalpha())
#========================================================
def save_data_to_file(file_path, data):
  while True:
   with open(file_path) as file:
      existing_data = file.read()
      if data not in existing_data:
        with open(file_path, "a") as file:
            file.write(data)
            print("Data added successfully.")
            break
      else:
        print("Data already exists in the file.")
        ask_for_items()
#========================================================
def save_price_to_file(data):
    with open("expenses.txt", "a") as file:
        file.write(str(data) + '\n')
#------------------------------------------------------  
def load_data_from_file(item):
    try:
        with open(file_path) as source:
            for line in source:
                if item in line:
                    global result
                    result = remove_alphabets(line).strip()
                    return
            else:
                print(f'Item "{item}" not found in the file.')
                result = None
    except FileNotFoundError:
        result = None
    except Exception as e:
        print(e)
        result = None

#========================================================
def main():
  print('Welcome to ExpenseTracker!')
  while True:
    prompt = input('Are you retrieving or adding data? (r / a): ')
    if prompt == 'a':
      ask_for_items()
    elif prompt == "r":
      retrieving_item = input('What is the name of this item?: ')
      load_data_from_file(retrieving_item)
      print(f'The price of {retrieving_item} is ${result}')
    else:
      print('Invalid, try again.')
#=======================================================
def ask_for_items():
  while True:
    items = input('What are the items? (q to quit): ')
    if items == 'q':
      break
    else:
      items_list.append(items)
      save_data_to_file("expenses.txt", items)
      price()
#========================================================
def price():
  for item in items_list:
    price = input('What is the price of this item? $')
    if price.isalpha == True:
      print('Text is rejected, please enter a valid number.')
    else:
      save_price_to_file(price)
if __name__ == '__main__':
  main()