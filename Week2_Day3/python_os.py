import os

# print(os.getcwd())


# print(os.listdir())


# os.mkdir("new_dir")

# if os.path.exists("new_dir"):
#     os.rmdir("new_dir")
#     print("Directory created")
# else:
#     print("Directory not created")


# os.rename("new_dir", "new_directory")


# import .env
# #to get a specific env variable
# python_path = os.getenv("SECRET")
# print(python_path)



def load_env_file(file_name):
    with open(file_name) as file:
        for line in file:
            # print(line)
            if line.strip():
                key, value = line.strip().split("=")
                key, value = line.split("=")
                os.environ[key] = value
                # print(value)


load_env_file(".env")

# make sure to type in terminal
# export SECRET=key


secret = os.getenv("SECRET")
print(secret)