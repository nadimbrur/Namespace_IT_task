from PIL import Image
import random
import shutil
import os

def resize(inp, out):
    os.makedirs(out, exist_ok=True)
    cnt=0
    for filename in os.listdir(inp):
        x=str(cnt+1)+'.'+filename.split('.')[-1]
        inp_path = os.path.join(inp, filename)
        out_path = os.path.join(out, x)
        img = Image.open(inp_path)
        img_resized = img.resize((224, 224))
        img_resized.save(out_path)
        cnt=cnt+1

def split_dataset(input_folder, train_folder, test_folder):
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    length = len(os.listdir(input_folder))
    train_samples = int(length * .8)
    my_array = list(range(1, length+1))
    random.shuffle(my_array)
    train_set = my_array[:train_samples]

    for i in os.listdir(input_folder):
        x=int(i.split('.')[0])
        print(x, type(x))
        if x in train_set:
            shutil.move(os.path.join(input_folder, i), os.path.join(input_folder, train_folder))
        else:
            shutil.move(os.path.join(input_folder, i), os.path.join(input_folder, test_folder))

if __name__ == "__main__":
    inp= "F:\\Namespace IT\\files\\orginal_data"
    out= "F:\\Namespace IT\\files\\orginal_resize_data"
    # resize(inp, out)
    train_folder="F:\\Namespace IT\\files\\orginal_resize_train"
    test_folder="F:\\Namespace IT\\files\\orginal_resize_test"
    split_dataset(out, train_folder,test_folder)
