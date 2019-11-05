from fastai.vision import*
import sys
vision.defaults.device = vision.torch.device('cpu')

path = vision.Path('.')
learn = vision.load_learner(path)
print(learn.data.batch_size)

imgpath = sys.argv[1]

img = open_image(imgpath)

pred = learn.predict(img)
print(pred)