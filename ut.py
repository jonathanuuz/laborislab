def generate_detail_desc(name, occupation, age):
    detail_desc = ''
    if name:
        detail_desc += f"Name: {name}\n"
    if occupation:
        detail_desc += f"Occupation: {occupation}\n"
    if age:
        detail_desc += f"Age: {age}\n"
    return detail_desc

# Call the function and print the result
print(generate_detail_desc('Jane Doe', 'Doctor', 28))
