from operator import xor
import shutil, os


# Common Prefix & Suffix name of all images along with source path 
prefix_0s='/Users/faizan/Desktop/zeeshan/album/stage/DSC0'
prefix_1s='/Users/faizan/Desktop/zeeshan/album/candid/DSC01'
prefix_2s='/Users/faizan/Desktop/zeeshan/album/candid/DSC02'
suffix='.JPG'
suffix2='.ARW'


# Shortlisted last 3/4 characters images from source folders
folder1_0s = '0001,8472,8475,8497,8511,8518,8523,8541,8550,8553,8556,8558,8565,8566,8567,8572,8574,8576,8580,8612,8618,8624,8625,8627,8629,8633,8663,8691,8718,8752,8753,8762,8808,8849,8866,8891,8896,8899,8927,8960,8969,8979,8987,8990,9008,9010,9054,9060,9075,9112,9146,9158,9169,9187,9236,9339,9367,9369,9373,9407,9423,9432,9433,9500,9509,9517,9523,9538,9582,9636,9667,9672,9704,9697,9710,9716,9724,9740,9748,9755,9780,9782,9785,9787,9810,9822,9857,9858,9864,9879,9880,9884,9948,9966,9969,9972,9992'
folder2_1s = '598,605,606,611,613,623,629,638,645,647,651,659,668,670,705,710,711,715,720,721,732,735,744,747,749,786,800,802,809,816,818,820,825,832,834,837,841,844,846,847,860,865,867,873,878,883,908,919,920,926,927,933,956,972,982,986,992'
folder3_2s = '000,003,006,021,035,045,060,061,072,098,099,113,113,118,148,171,207,214,234,332,344,348,369,380,382,389,396,402,461,465,470,474,476,482,486,487,492,495,497,504,506,508,511,521,525,527,534,538,540,542,550,553,560,566,570,574,583,586,589,593,595,603,604,606,616,619,622,630,647,656,683,847,861,887,906,912,917,928,935,937,948,954,955,966,967,987,993'
list1 = folder1_0s.split(',')
list2 = folder2_1s.split(',')
list3 = folder3_2s.split(',')


# To get Count of Original Folder1 after adding all shortlisted full image name into new_list 
new_list1=[]
for i in range(len(list1)):
    try:
        temp1=prefix_0s+list1[i]+suffix
        new_list1.append(temp1)
    except:
        continue
print("Count of Folder1=",len(new_list1))


# To get Count of Original Folder2
new_list2=[]
for i in range(len(list2)):
    try:
        temp2=prefix_1s+list2[i]+suffix2
        new_list2.append(temp2)
    except:
        continue

new_list3=[]
for i in range(len(list3)):
    try:
        temp3=prefix_2s+list3[i]+suffix2
        new_list3.append(temp3)
    except:
        continue
print("Count of Folder2=",len(new_list2)+len(new_list3))


# Copy Folder1 Files to a destination folder named 'stage_final'
for f1 in new_list1:
    shutil.copy(f1, '/Users/faizan/Desktop/zeeshan/album/stage_final')

# Copy Folder1 Files to a destination folder named 'candid_final'
for f2 in new_list2:
    shutil.copy(f2, '/Users/faizan/Desktop/zeeshan/album/candid_final')

for f3 in new_list3:
    shutil.copy(f3, '/Users/faizan/Desktop/zeeshan/album/candid_final')


# Get destination stage_final folder count
Folderpath1 = '/Users/faizan/Desktop/zeeshan/album/stage_final'   
size1 = len(os.listdir(Folderpath1)) -1
print("Stage_final Folder: ",size1,len(files1))

# Get destination candid_final folder count
Folderpath2 = '/Users/faizan/Desktop/zeeshan/album/candid_final'   
size2 = len(os.listdir(Folderpath2)) -1
print("Candid_final Folder: ",size2,len(files2)+len(files3))

print("Final Folder Count", len(files1)+len(files2)+len(files3))
