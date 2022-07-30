from PIL import Image
import random, string

export_file_path = '/Users/bilibala/Desktop/work/wozy_film/json_converter/tmp_0.jsonl'
image_input_folder_path = '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1/'
image_cropped_output_folder_path = '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1_cropped_vertex/'
#
image_merged_output_folder_path = '/home/bilibala/Desktop/work/dataset/jsw/wozy_merged_3003/'
#

#Function integrated all the logical process in order to crop the image for batch processing
#optionK:
# 0 - only the biggest area is cropped
# 1 - merging cropping
# 2 - crop all the labeled area
def processBatchCropping(optionK=0, export_path=export_file_path):
    with open(export_path) as f:
        lines = f.readlines()
        for i in range(1,len(lines)+1):
            processSingleCropping(i, optionK)

#Function integreted all the logical process in order to crop the image
#optionK:
# 0 - only the biggest area is cropped
# 1 - merging cropping
# 2 - crop all the labeled area
def processSingleCropping(lineInFile, optionK=0):
    print("Cropping image")
    crop_list = prepareCropList(lineInFile-1)
    print(crop_list)
    sorted_crop_list = Sort(crop_list)
    print("Select first two or first element from the list")
    selected_crop_list = SelectFirstTwoOrFirst(sorted_crop_list)
    print(SelectFirstTwoOrFirst(sorted_crop_list))
    print("CalculateArea")
    area_list = CalculateArea(selected_crop_list)
    print(area_list)
    print("Compariong biggest area")
    biggestArea = getBiggestArea(area_list)
    print(biggestArea)
    if optionK == 0:
        print("Image is cropping")
        cropBiggestImage(biggestArea)
        print("Image Cropped")
    elif optionK == 1:
        print("Image is cropping")
        cropBiggestImageandMerge(biggestArea)
        print("Image Cropped")
    elif optionK == 2:
        print("Image is cropping")
        cropAllImages(crop_list)
        print("Image Cropped")


# outout:
# [image_name, displayName, xMin, xMax, yMin, yMax]
def prepareCropList(line_number, export_path=export_file_path):
    crop_list = []
    with open(export_path) as f:
        lines = f.readlines()
        line = lines[line_number]
        if line.find("displayName")>0:
            print(line)
            print("yes")
            # for line in f:
            image_name = line.strip('{"imageGcsUri":"gs://wozy_wagon_object_detection/vertex/').split('","', 1)[0]
            truck_json = \
                line.strip('{"imageGcsUri":"gs://wozy_wagon_object_detection/vertex/' + image_name + '","boundingBoxAnnotations":').split("]", 1)[
                    0] + ']'
            truck_json = truck_json.split("}" + "}")
            for i in range(len(truck_json)):
                if truck_json[i][0] == ",":
                    truck_json[i] = truck_json[i][1:]
                truck_json[i] = truck_json[i].split(',')
                # print(truck_json[i])
                for element in truck_json[i]:
                    if element.count("displayName") == 1:
                        displayName = element.strip('[{"displayName":')
                    elif element.count("xMin") == 1:
                        xMin = element.strip('"xMin":')
                    elif element.count("xMax") == 1:
                        xMax = element.strip('"xMax":')
                    elif element.count("yMin") == 1:
                        yMin = element.strip('"yMin":')
                    elif element.count("yMax") == 1:
                        yMax = element.strip('"yMax:')
                # Fixed bug
                if truck_json[i] != [']']:
                    crop_list.append([image_name, displayName, xMin, xMax, yMin, yMax])
    return crop_list


# sort function for xMax in the crop_list: [image_name, displayName, xMin, xMax, yMin, yMax]
# input # [image_name, displayName, xMin, xMax, yMin, yMax]
def Sort(sub_li):
    return (sorted(sub_li, key=lambda x: x[3], reverse=True))


# input
# output
# [image_name, displayName, xMin, xMax, yMin, yMax]
def SelectFirstTwoOrFirst(sorted_list):
    if len(sorted_list) > 1:
        tmp1 = float(sorted_list[0][2])
        tmp2 = float(sorted_list[1][2])
        if float(sorted_list[0][2]) == float(sorted_list[1][2]):
            if len(sorted_list) > 2:
                return sorted_list[1:3]
            else:
                return sorted_list[0:2]
        else:
            return sorted_list[0:2]
    elif len(sorted_list) == 1:
        return sorted_list
    else:
        print("error with the list length")
    return 0


# output
# [imageName, displayName, area, xMin, xMax, yMin, yMax]
def CalculateArea(list):
    area_list = []
    for element in list:
        imageName = element[0]
        displayName = element[1]
        xMin = element[2]
        xMax = element[3]
        yMin = element[4]
        yMax = element[5]
        x_length = float(xMax) - float(xMin)
        y_length = float(yMax) - float(yMin)
        area = x_length * y_length
        area_list.append([imageName, displayName, area, xMin, xMax, yMin, yMax])
    return area_list


# output:
# [imageName, displayName, area, xMin, xMax, yMin, yMax]
def getBiggestArea(list):
    biggestArea = []
    if len(list) >= 2:
        if list[0][2] > list[1][2]:
            biggestArea.append(list[0])
        elif list[1][2] > list[0][2]:
            biggestArea.append(list[1])
        elif list[1][2] == list[0][2]:
            biggestArea.append(list[1])
        return biggestArea
    elif len(list) == 1:
        biggestArea.append(list[0])
        return biggestArea
    else:
        print("biggest error: len of list <= 0")
    return 0

#kOptions = 0: save to the local and return the cropped img variable
#kOptions = 1: return the tuple of orignal image and cropped img variable
# input from getBiggestArea(list): [imageName, displayName, area, xMin, xMax, yMin, yMax]
def cropBiggestImage(biggestarea, image_input_folder_path=image_input_folder_path,
                     cropped_output_folder_path=image_cropped_output_folder_path, kOptions=0):
    truck = biggestarea[0]
    imageOrgName = truck[0]
    displayName = truck[1]
    xMin = truck[3]
    xMax = truck[4]
    yMin = truck[5]
    yMax = truck[6]
    im = Image.open(image_input_folder_path + imageOrgName)
    width, height = im.size
    left = width * float(truck[3])
    right = width * float(truck[4])
    top = height * float(truck[5])
    bottom = height * float(truck[6])
    cropped_im = im.crop((left, top, right, bottom))
    # (replace the path below with a path to folder where all cropped images will be stored)
    xMin = 0
    xMax = 1
    yMin = 0
    yMax = 1
    if kOptions == 0:
        #  = imageOrgName.strip('.png') + '_' + displayName + '_' + '.png'
        newName = imageOrgName
        saveName = cropped_output_folder_path + newName
        cropped_im.save(saveName)
        # write records to jsonl
        with open(cropped_output_folder_path+'cropped.jsonl', 'a+') as f:
            # string1 + newName
            string1 = '{"imageGcsUri":"gs://wozy_cropped_3003/'
            string2 = '","boundingBoxAnnotations":[{"displayName":"'
            string3 = '","xMin":'
            string4 = ',"xMax":'
            string5 = ',"yMin":'
            string6 = ',"yMax":'
            string7 = ',"annotationResourceLabels":{"aiplatform.googleapis.com/annotation_set_name":"3245204171334352896"}}'
            string8 = '],"dataItemResourceLabels":{}}'
            f.write(f'''{string1}{newName}{string2}{displayName}{string3}{xMin}{string4}{xMax}{string5}{yMin}{string6}{yMax}{string7}{string8}''')
            f.write("\n")
        #
        return cropped_im
    elif kOptions == 1:
        return im, cropped_im

def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst
# img_list input from getBiggestArea(list): [imageName, displayName, area, xMin, xMax, yMin, yMax]
def cropBiggestImageandMerge(img_list, image_input_folder_path=image_input_folder_path,
               cropped_output_folder_path=image_cropped_output_folder_path,
               merged_output_folder_path=image_merged_output_folder_path):
    image = img_list[0]
    imageOrgName = image[0]
    displayName = image[1]
    processedImages = cropBiggestImage(img_list, image_input_folder_path, cropped_output_folder_path, 1)
    imgOrg = processedImages[0]
    imgCropped = processedImages[1]
    imgMerged = get_concat_h_blank(imgOrg, imgCropped)
    imgMerged.show()
    imgMerged.save(merged_output_folder_path + imageOrgName.strip('.png') + '_merged_' + displayName + '_' + '.png')


#[imageName, displayName, area, xMin, xMax, yMin, yMax]
def cropAllImages(crop_list, image_input_folder_path=image_input_folder_path,
                  cropped_output_folder_path=image_cropped_output_folder_path):
    for truck in crop_list:
        im = Image.open(image_input_folder_path + truck[0])
        width, height = im.size
        left = width * float(truck[2])
        right = width * float(truck[3])
        top = height * float(truck[4])
        bottom = height * float(truck[5])
        cropped_im = im.crop((left, top, right, bottom))
        # (replace the path below with a path to folder where all cropped images will be stored)
        cropped_im.save(cropped_output_folder_path + truck[0].strip('.png') + '_' + truck[3]+'_'+ \
                        ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in
                                range(5)) + '.png')
