<h1>Use a Pre-trained Image Classifier to Identify Dog Breeds</h1>

<h2>Guidelines for the Project</h2>

Guidelines for the project 1 can be found below in the attached pdf. All the TODO's have already been completed in this code. Please refer the comments and docstrings for more information regarding the source file.

[Udacity Project _1 Use a Pre-trained Image Classifier to Identify Dog Breeds.pdf](https://github.com/PranavDarshan/Udacity-Projects/files/13260250/Udacity.Project._1.Use.a.Pre-trained.Image.Classifier.to.Identify.Dog.Breeds.pdf)


<h2>Setup and Requirements to Run on Windows</h2>

1. Download all the source files.
2. Download Anaconda Navigator to create a working environment to run the tool by installing pytorch, transformers and torchvision libraries.
 
 ![image](https://github.com/PranavDarshan/Udacity-Projects/assets/65911046/1b4dd7cd-1185-4532-9a4a-e7cafe9d0461)

3. Also ensure that <b>run_models_batch</b> and <b>run_models_uploaded</b> files are in bat extension. If not change it to bat extension.

<h2>Running on Windows</h2>

1. You can directly run the <b>check_images.py</b> to run a single model on VS code by changing your interpreter to Annaconda environment that you have created and downloaded the libraries, base:root in my case. Open a cmd terminal in VS Code and make sure you are in the correct directory.

![image](https://github.com/PranavDarshan/Udacity-Projects/assets/65911046/d08d4a11-73c6-4a62-8f15-5d08e285ade4)


2. While running the code you can give the input arguements
   replace "directory" for directory of pet images, "architecture" for model architecture, and "dogfile" for path of dognames as:
  ```ruby
python check_images.py --dir="directory" --arch="architecture" --dogfile="dogfile" 
```
 3. If you want to run multiple models and store the data in a text file, in the cmd terminal in VS Code, type
  ```ruby
run_models_batch.bat
```

4. To run uploaded images and store the data in a text file, in the cmd terminal in VS Code, type
  ```ruby
run_models_batch_uploaded.bat
```
<h2>Results</h2>

The results can be obtained on the :
1. vgg_pet-images.txt
2. vgg_uploaded-images.txt
3. alexnet_pet-images.txt
4. alexnet_uploaded-images.txt
5. resnet_pet-images.txt
6. resnet_uploaded-images.txt
