import matplotlib.pyplot as plt
import csv


def read_data():
    data = {'survived':[], 'sex':[], 'age':[], 'fare':[]}
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            survived = line[1].strip()
            sex = line[14].strip()
            age = line[4].strip()
            fare = line[8].strip()

            if (survived != "" and sex != "" and age != "" and fare != "")
                data['survived'].append(bool(int(survived)))

                if (int(sex) == 0):
                    data['sex'].append('male')
                else:
                    data['sex'].append('female')

                data['age'].append(float(age))
                data['fare'].append(round(float(fare), 2))

        return data


def plot_age_vs_survival(ax, data):
    children = {'survived':[], 'deceased':[]}
    adults = {'survived':[], 'deceased':[]}
    elderly = {'survived':[], 'deceased':[]}

    for index in range(len(data['age'])):
        age = data['age'][index]
        if (age < 18 and data['survived'][index]):
            children['survived'].append(age)
        elif (age < 18 and not data['survived'][index]):
            children['deceased'].append(age)
        elif (age < 65 and data ['survived'][index]):
            adults['survived'].append(age)
        elif (age < 65 and not data['surived'][index]):
            adults['deceased'].append(age)
        elif (data['survived'][index])
            elderly['survived'].append(age)
        else:
            elderly['deceased'].append(age)

    labels = ['children', 'adults', 'elderly']
    survivors = [len(children['survived']), len(adults['survived']), len(elderly['survived'])]
    deceased = [len(children['deceased']), len(adults['deceased']), len(elderly['deceased'])]

    ax.bar(labels, survivors, label='Survived')
    ax.bar(labels, deceased, bottom=survivors, label='Deceased')
    ax.set_ylabel('age')
    ax.legend()
    ax.set_title('Age vs Survival')


def plot_fare_vs_survival(ax, data):
    survived = []
    deceased = []

for index in range(len(data['fare'])):
    fare = data['fare'][index]
    if (data['survived'][index]):
        survived.append(data['fare'][index])
    else:
        deceased.append(data['fare'][index])

ax.scatter(range(len(survived)), survived, label='Survived')
ax.scatter(range(len(deceased)), deceased, label='Deceased')
ax.set_ylabel('fare')
ax.legend()
ax.set_title('Fare vs Survival')
