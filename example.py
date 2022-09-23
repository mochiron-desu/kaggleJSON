import urllib
testfile = urllib.request.urlretrieve("https://raw.githubusercontent.com/mochiron-desu/kaggleJSON/main/kaggle.json", "kaggle.json")
! pip install kaggle
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets download -d <>
! unzip <>
