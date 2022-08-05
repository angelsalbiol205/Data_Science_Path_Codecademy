#import library
import csv

#info we have about each patient
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

#import dataset and create list with function
def create_list_from_data(lst, csv_file, column_name):
    with open("insurance.csv", newline = "") as insurance:
        insurance_dataset = csv.DictReader(insurance)
        for row in insurance_dataset:
            lst.append(row[column_name])
        return lst

create_list_from_data(age, "insurance.csv", "age")
create_list_from_data(sex, "insurance.csv", "sex")
create_list_from_data(bmi, "insurance.csv", "bmi")
create_list_from_data(children, "insurance.csv", "children")
create_list_from_data(smoker, "insurance.csv", "smoker")
create_list_from_data(region, "insurance.csv", "region")
create_list_from_data(charges, "insurance.csv", "charges")

#defining class and methods

class Patient:

    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges

    def patient_info(self):
        patient_info = {"Nº of patiens": len(self.age),
                        "Age": self.age,
                        "Sex": self.sex,
                        "Bmi": self.bmi,
                        "Number of children": self.children,
                        "Smoker": self.smoker,
                        "Region": self.region,
                        "Charges": self.charges}
        return patient_info


    def average_age(self):
        ages_float = list(map(float, self.age))
        return "Average patients age: " + str(round(sum(ages_float) / len(ages_float), 2))

    def location(self):
        location = dict()
        for area in region:
            if area not in location:
                location[area] = 1
            if area in location:
                location[area] += 1
        return location

    def female_vs_male(self):
        females = 0
        males = 0
        for person in sex:
            if person == "female":
                females += 1
            else:
                males += 1
        return "Nº of females: " + str(females) + " and Nº of males: " + str(males)

    def smokers(self):
        smokers = {"Smokers": 0, "Non-smokers": 0}
        for patient in smoker:
            if patient == "yes":
                smokers["Smokers"] += 1
            else:
                smokers["Non-smokers"] += 1
        return smokers

    def num_of_children(self):
        num_of_children = dict()
        for num in children:
            if num not in num_of_children:
                num_of_children[num] = 1
            if num in num_of_children:
                num_of_children[num] += 1
        return dict(sorted(num_of_children.items()))

    def average_insurance_cost(self):
        charges_float = list(map(float, self.charges))
        return "Average insurance cost per patient: {}".format(round(sum(charges_float) / len(charges_float), 2))

    def average_cost_if_smoker(self):
        charge_if_smoker = []
        for i in range(0, len(charges)):
            for i in range(0, len(smoker)):
                if smoker[i] == "yes":
                    charge_if_smoker.append(float(charges[i]))
        average_cost_if_smoker = round(sum(charge_if_smoker) / len(charge_if_smoker), 2)
        return "Average cost if patients are smokers: " + str(average_cost_if_smoker)

    def average_cost_sex(self):
        charge_if_female = []
        charge_if_male = []
        for i in range(0, len(sex)):
            for i in range(0, len(charges)):
                if sex[i] == "female":
                    charge_if_female.append(float(charges[i]))
                else:
                    charge_if_male.append(float(charges[i]))
        return "Average cost if patients are female: " + str(round(sum(charge_if_female) / len(charge_if_female), 2))\
               + " and average cost if patients are male: " + str(round(sum(charge_if_male) / len(charge_if_male), 2))

    def above_below_average(self):
        charges_float = list(map(float, self.charges))
        average = {"Above": 0, "Below": 0, "Equal": 0}
        for cost in charges_float:
            if cost > sum(charges_float) / len(charges_float):
                average["Above"] += 1
            elif cost < sum(charges_float) / len(charges_float):
                average["Below"] += 1
            else:
                average["Equal"] += 1
        return average

patient = Patient(age, sex, bmi, children, smoker, region, charges)
#print(patient.patient_info())
print(patient.average_age())
print(patient.location())
print(patient.female_vs_male())
print(patient.smokers())
print(patient.num_of_children())
print(patient.average_insurance_cost())
print(patient.average_cost_if_smoker())
print(patient.average_cost_sex())
print(patient.above_below_average())
