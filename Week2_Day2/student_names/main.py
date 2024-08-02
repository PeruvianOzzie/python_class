# create and activate virtual environment

# python -m venv students_env

# source ./students_env/bin/activate

# for windows
# .\students_env\Scripts\activate


# to take the names in the names.txt file and print them out

# import out read_name_from_file function
import read_name_file
import id_assigner

# get list of names from names.txt file
names = read_name_file.read_name_from_file("names.txt")
# print(names)


#sort the names in alphabetical order
sorted_names = sorted(names)
# print(sorted_names)


# {1: 'John', 2: 'Jane', 3: 'Doe'}
names_dict = id_assigner.id_assigner(sorted_names)
print(names_dict)
print(names_dict[1])