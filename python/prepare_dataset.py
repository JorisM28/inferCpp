import os
import shutil
import random
from pathlib import Path


def prepare_mvtec_binary(category_path="bottle", output_path="bottle_custom", split_ratio=0.8):

    src_dir = Path(category_path)
    dst_dir = Path(output_path)

    if not src_dir.exists():
        raise FileNotFoundError(f"Source folder {src_dir} doesn't exist.")

    dirs_to_create = {
        "train_good": dst_dir / "train_custom" / "good",
        "train_def": dst_dir / "train_custom" / "defective",
        "val_good" : dst_dir / "val_custom" / "good",
        "val_def": dst_dir / "val_custom" / "defective"
    }


    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    for p in dirs_to_create.values():
        p.mkdir(parents=True, exist_ok=True)
    

    print(f"Folder Tree created in {dst_dir}/")

    good_imgs = list((src_dir / "train" / "good").glob("*.png")) + \
                list((src_dir / "test" / "good").glob("*.png"))


    def_imgs = []
    test_dir = src_dir / "test"
    for sub_dir in test_dir.iterdir():
        if sub_dir.is_dir() and sub_dir.name != "good":
            def_imgs.extend(list(sub_dir.glob("*.png")))


    random.seed(42)
    random.shuffle(good_imgs)
    random.shuffle(def_imgs)

    good_split = int(len(good_imgs) * split_ratio)
    def_split = int(len(def_imgs) * split_ratio)


    def copy_files(files, dest_folder):

        for f in files:

            parent_name = f.parent.name


            if parent_name == "good":
                parent_name = f"{f.parent.parent.name}_{parent_name}"

            new_name = f"{parent_name}_{f.name}"
            shutil.copy2(f, dest_folder / new_name)



    print("Copy and renaming files...")
    copy_files(good_imgs[:good_split], dirs_to_create["train_good"])
    copy_files(good_imgs[good_split:], dirs_to_create["val_good"])

    copy_files(def_imgs[:def_split], dirs_to_create["train_def"])
    copy_files(def_imgs[def_split:], dirs_to_create["val_def"])


    print("\n Dataset prepared with success")
    print("Final repartition : ")
    print(f"   - Training : {good_split} good | {def_split} defective ")
    print(f"   - Validation : {len(good_imgs) - good_split} good | {len(def_imgs) - def_split} defective") 



if __name__ == "__main__":

    prepare_mvtec_binary(category_path="bottle", output_path="bottle_custom")





    
