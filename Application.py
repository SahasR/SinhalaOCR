from PIL import Image
import pytesseract
import os
import time
import getpass


while True:
    username = getpass.getuser()
    text_file_name = input("Write the Output File Name: ")
    if not os.path.exists(f"C:/Users/{username}/Pictures/Translate"):
        os.makedirs(f"C:/Users/{username}/Pictures/Translate/Output") #Change these directories dependant on your OS
        os.makedirs(f"C:/Users/{username}/Pictures/Translate/Input")
        print("Directory was not found I have created one for you...")
        time.sleep(5)
        print("Restart Application and Put your stuff in the relevant folders in Pictures/Translate.......")
        time.sleep(5)
        exit()

    items_exist = False
    text_file = open(rf"C:\Users\{username}\Pictures\Translate\Output\{text_file_name}.txt", "w+",
                     encoding="utf-8")  # Edit the place where you want to store it
    translated_text = ""
    for file in os.listdir(rf"C:\Users\{username}\Pictures\Translate\Input"):  # Edit the place at which Translations will be edited
        if file.endswith(".JPG"):
            items_exist = True
            image_path = os.path.join(rf"C:\Users\{username}\Pictures\Translate\Input", file)
            print("---------------Translating------------------")
            print(image_path)
            im = Image.open(image_path)
            new_size = tuple(1 * x for x in
                             im.size)  # Increasing this 1*x part to different integer values may increase the accuracy sometimes
            im = im.resize(new_size, Image.ANTIALIAS)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            translated_text += pytesseract.image_to_string(im, lang='sin')
    if items_exist == True:
        print("Cleaning up the translation.......")
        translated_text = translated_text.replace("\n\n", "new_para")
        translated_text = translated_text.rstrip("\n")
        translated_text = translated_text.replace("\n", " ")
        translated_text = translated_text.replace("\u200c", " ")
        translated_text = translated_text.replace("\u200d", "")
        translated_text = translated_text.replace("new_para", "\n\n")
        print("Text is completely translated and is saved in Pictures/Translate/Output......")
        time.sleep(5)
        text_file.write(translated_text)
        exit()
    else:
        print("Items not found inside the Translation Folder....... Please Check Pictures/Translations")
        time.sleep(5)
        exit()
