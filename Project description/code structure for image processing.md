MODULES:
- numpy
- pandas
- matplotlib / seaborn
- tensorflow
- opencv
- scipy
- scikit-learn
- Pillow
- Natural Language Toolkit (NLTK)
- Beautiful Soup


------------------------------------------------------------------------------

IMAGE ACQUISITION

- Function Definition: 
The acquire_xray_images function is defined to handle the image acquisition process. It takes one argument, directory, which represents the path to the directory containing X-ray images.

- Image Retrieval:
Within the function, we iterate over each file in the specified directory using the os.listdir function. We check if the file ends with .jpg or .png extensions, indicating it's an image file.

- Reading Images:
For each image file found, we construct the full path to the image using os.path.join and then use OpenCV's cv2.imread function to read the image file as a NumPy array representing the image.

- Validation: 
We check if the image is successfully read (i.e., not None) to ensure that the image file is valid. If it is valid, we append the image array to the images list.

- Return:
Finally, we return the list of image arrays (images), representing the X-ray images acquired from the specified directory.

Example Usage: 

An example usage of the acquire_xray_images function is provided at the end, where we specify the directory path containing the X-ray images (xray_image_directory) and call the function to acquire the images.


------------------------------------------------------------------------------
IMAGE PREPROCESSING


------------------------------------------------------------------------------
IMAGE SEGMENTATION


------------------------------------------------------------------------------
FEATURE EXTRACTION


------------------------------------------------------------------------------
DEEP LEARNING MODELS: CNN & NLP


------------------------------------------------------------------------------
PROBLEMS IDENTIFICATION


------------------------------------------------------------------------------
MEDICINE INFORMATION


------------------------------------------------------------------------------
CLINICAL RECOMMENDATION


------------------------------------------------------------------------------
INTEGRATION WITH EHR


------------------------------------------------------------------------------
