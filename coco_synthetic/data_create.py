import os
import shutil

def util(type):
  temp_list = []
  with open('{}_filter.txt'.format(type)) as f:
    for line in f:
      temp_list.append(line.strip().split(' ')[0])
  return temp_list

def authentic(type, id):
  path = './cocostuff/coco/train2014'
  for filename in util(type):
      img = "COCO_train2014_{:012d}.jpg".format(int(filename.split('_')[id]))
      if img in os.listdir(path):
          filename = os.path.join(path, img)
          shutil.copy(filename, './dataset/{}/Au'.format(type))
      else:
          print("file does not exist: filename")
  print('Data creation complete!')

def tampered(type):
  path = './filter_tamper'
  for filename in os.listdir(path):
      if filename in util(type):
          filename = os.path.join(path, filename)
          shutil.copy(filename, './dataset/{}/Tp'.format(type))
      else:
          print("file does not exist: filename")

#Authentic
# authentic('test')
authentic('train', 1)

##Forged
# tampered('test')
# tampered('train')