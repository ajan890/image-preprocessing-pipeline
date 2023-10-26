from numpy import nonzero
import csv

def get_points(stack, threshold):
    points = []
    for i in range(stack.shape[0]):
        raw_img = stack[i]
        a, b = nonzero(raw_img > threshold)
        points.append(list(zip(a, b, [i] * stack.shape[0])))
    return points


def aruns_method_alignment(reference: ndarray, subject: ndarray):
    pass


img1 = TifStack(Path("./tempData/cha1"))
img2 = TifStack(Path("./tempData/cha2"))

img1_points = get_points(img1, 0.5)
print(img1_points)
# img2_points = get_points(img2)

print("writing")
with open('tempData/testing.csv','wb') as out:
    csv_out=csv.writer(out)
    # csv_out.writerow(['name','num'])
    for row in img1_points:
        csv_out.writerow(row)

print("done")
