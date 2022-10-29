import os
import secrets
import string

def generate_random_string(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    directory = os.getcwd()

    for filename in os.listdir(directory):
        _, extension = os.path.splitext(filename)

        if extension == ".jpg" or extension == ".png":
            random_string = generate_random_string()
            random_filename = random_string + extension

            os.rename(filename, random_filename)
            print("Changed \"{}\" to \"{}\"".format(filename, random_filename))
