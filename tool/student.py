import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rc("font", family='Microsoft YaHei')  # 增加
# Data from your table


import matplotlib.pyplot as plt
import numpy as np

# Data from the table
labels = ['课程目标1', '课程目标2', '课程目标3']
quantitative_eval = [0.78, 0.80, 0.79]
qualitative_eval = [0.86, 0.76, 0.79]
comprehensive_eval = [0.80, 0.79, 0.79]

# Bar width
bar_width = 0.2

# Positions of the bars on the x-axis
r1 = np.arange(len(labels))
r2 = [x + bar_width for x in r1]

# Custom RGB colors
color_blue = (68 / 255, 114 / 255, 196 / 255)
color_orange = (237 / 255, 125 / 255, 49 / 255)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(r1, quantitative_eval, color=color_blue, width=bar_width, edgecolor='grey', label='课程考核')
plt.bar(r2, qualitative_eval, color=color_orange, width=bar_width, edgecolor='grey', label='学生自评')

# Add data labels above the bars
for i in range(len(r1)):
    plt.text(r1[i], quantitative_eval[i] + 0.01, f'{quantitative_eval[i]:.2f}', ha='center', color='black')
    plt.text(r2[i], qualitative_eval[i] + 0.01, f'{qualitative_eval[i]:.2f}', ha='center', color='black')

# General layout
plt.ylabel('达成度', fontweight='bold', fontsize=12)
plt.xticks([r + bar_width / 2 for r in range(len(labels))], labels)
plt.ylim(0, 1)

# Positioning the legend below the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

# Show the plot
plt.title('课程目标达成情况评价结果')
plt.show()



data = np.array([
    [0.78, 0.466666667, 0.685714286],
    [0.705, 0.517777778, 0.685714286],
    [0.723333333, 0.766666667, 0.885714286],
    [0.591666667, 0.855555556, 0.714285714],
    [0.6925, 0.95, 0.628571429],
    [0.8075, 0.772222222, 0.714285714],
    [0.593333333, 0.866666667, 0.542857143],
    [0.91, 0.866666667, 0.914285714],
    [0.805833333, 0.816666667, 0.657142857],
    [0.875833333, 0.772222222, 0.742857143],
    [0.861666667, 0.8, 0.828571429],
    [0.75, 0.666666667, 0.8],
    [0.978333333, 0.911111111, 0.942857143],
    [0.783333333, 0.777777778, 0.8],
    [0.931666667, 0.866666667, 0.942857143],
    [0.86, 0.555555556, 0.685714286],
    [0.893333333, 0.822222222, 0.857142857],
    [0.813333333, 0.866666667, 0.8],
    [0.959166667, 0.861111111, 0.857142857],
    [0.846666667, 0.866666667, 0.685714286],
    [0.928333333, 0.8, 0.914285714],
    [0.915, 0.844444444, 0.885714286],
    [0.983333333, 0.911111111, 0.942857143],
    [0.78, 0.866666667, 0.914285714],
    [0.716666667, 0.711111111, 0.6],
    [0.8575, 0.95, 0.742857143],
    [0.8, 0.711111111, 0.657142857],
    [0.898333333, 0.911111111, 0.942857143],
    [0.766666667, 0.911111111, 0.885714286],
    [0.855, 0.611111111, 0.742857143],
    [0.891666667, 0.911111111, 0.942857143],
    [0.8, 0.844444444, 0.628571429],
    [0.791666667, 0.755555556, 0.828571429],
    [0.8375, 0.883333333, 0.685714286],
    [0.966666667, 0.955555556, 0.857142857],
    [0.358333333, 0.477777778, 0.142857143],
    [0.816666667, 0.866666667, 0.885714286]
])

# Number of students
students = np.arange(1, len(data) + 1)

# Titles and labels
titles = ['课程目标1', '课程目标2', '课程目标3']
y_mean = data.mean(axis=0)

for i in range(3):
    plt.figure(figsize=(10, 5))
    plt.scatter(students, data[:, i], color='blue')
    plt.axhline(y=0.7, color='red', linestyle='-')
    plt.title(titles[i])
    plt.xlabel('学生')
    plt.ylabel('达成度')
    plt.ylim(0, 1)  # Set y-axis range from 0 to 1
    plt.show()