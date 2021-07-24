## Image Forgery Detection with a Two-Stream CNN
A novel two-stream CNN built using tensorflow for the purpose of detecting forgery in images. The approach used is inspired by the work of Zhou et al. [Learning Rich Features for Image Manipulation Detection](https://arxiv.org/abs/1805.04953). 
## Network Architecture
The method uses a two-stream architecture to perform forgery classification. Local noise features from the steganalysis rich model (SRM) are used together with error level analysis (ELA) features in a two-stream network. An illustration of this architecture is shown below.

![Two-stream network illustration](https://github.com/emmkay1/forgery-detection/blob/master/2-stream.svg)

Each stream in this two-stream architecture consists of convolutional layers and pooling layers. The two streams are fused and the result is passed through a fully connected layer and then a 2-way softmax classifier. 

For the SRM stream, the first convolution layer is the SRM layer which uses 3 filter kernels with a receptive field—the local area of the input volume connected by each neuron in the convolutional layer—of 5× 5.

The code for this two-stream network can be found in `forgery-project/two_stream.ipynb`.

## Environment
AWS sagemaker was utilized to run the code. AWS allows you to set up your environment quickly. You can easily increase the number of GPU's required for your needs.

The instance was configured with forty-eight high memory CPUs and has a memory of size 192 GB. It is also configured with four NVIDIA Tesla T4 GPUs. **TensorFlow 2.3 gpu**  and **Python 3.7** were used.

To do it locally would require configuring Tensorflow GPU with CUDA. You can find tutorials on how to do so through a quick Google search.

For required packages please run:

    pip install -r requirements.txt

## Datasets
This project uses two datasets. One is a synthetic dataset created using the COCO 2014 dataset. This is a dataset of tampered images. The model is trained on this dataset. First install COCO PythonAPI

    pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"

To create the dataset follow the steps below:
 1. Download the COCO 2014 dataset from ([http://cocodataset.org/#download](http://cocodataset.org/#download)) and place it in a folder named coco_synthetic
 2. Change  `dataDir`  in  `coco_synthetic/demo.py`  to the path of 'train2014' (e.g,  `./cocostuff/coco/train2014`)
 3. Run  `run_demo.sh 1 100`  to choose the first and last COCO category used for creating the tamper synthetic dataset.
 4. Run  `split_train_test.py`  to make train/test split. (making sure that the images used to generate training set do not overlap with the images for testing)

*Instructions on how to do this are taken from [here](https://github.com/pengzhou1108/RGB-N#synthetic-dataset) but a few minor changes are made here.*

***Final step***
Run `data_create` to create a folder of images with tampered images and another with authentic images for both training and testing if required. Uncomment code in the file for what you need.

The other dataset that was used is CASIA v2 which was mainly used for testing. CASIA can be downloaded from [kaggle](https://www.kaggle.com/sophatvathana/casia-dataset).
