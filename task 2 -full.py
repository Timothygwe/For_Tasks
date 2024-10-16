import pandas as pd

# Загружаем данные
data = pd.read_csv("adult.data.csv")
data.head()

def get_count(dataframe):
    print(dataframe['sex'].value_counts())

def get_count_all(dataframe):
    print(dataframe['sex'].count())

def avg_age(dataframe):
    data_age = dataframe[dataframe['sex'] == 'Male']
    print(data_age['age'].mean())

def us_proportion(dataframe):
    data_us = dataframe[dataframe['native-country'] == 'United-States']
    result = (len(data_us) / len(dataframe)) * 100
    print(str(result) + "%")

def mean_and_std_more_50k(dataframe):
    result = {"mean": 0, "std": 0}
    data_salary = dataframe[dataframe['salary'].isin(['>50K'])]
    result['mean'] = data_salary['age'].mean()
    result['std'] = data_salary['age'].std()
    print(f"Mean age for >50K: {result['mean']}, Std: {result['std']}")

def mean_and_std_less_50k(dataframe):
    result = {"mean": 0, "std": 0}
    data_salary = dataframe[dataframe['salary'].isin(['<=50K'])]
    result['mean'] = data_salary['age'].mean()
    result['std'] = data_salary['age'].std()
    print(f"Mean age for <=50K: {result['mean']}, Std: {result['std']}")

def higher_educ(dataframe):
    data_salary = dataframe[dataframe['salary'].isin(['>50K'])]
    result = data_salary[data_salary['education'].isin(["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"])]
    is_higher_educ = len(result) / len(dataframe) * 100 > 50
    print(f"More than 50% of high earners have higher education: {is_higher_educ}")

def stat_for_sex(dataframe):
    data = dataframe.groupby('sex')['age']
    print(data.describe())

def stat_for_race(dataframe):
    data = dataframe.groupby('race')['age']
    print(data.describe())

# Asian-Pac_Islander == 90
print(stat_for_race(data))

def high_salary_family_status(dataframe):
    male_data = dataframe[dataframe['sex'] == 'Male']
    married_conditions = male_data['marital-status'].str.startswith('Married')
    
    married_men = male_data[married_conditions]
    single_men = male_data[~married_conditions]
    
    high_earners_married = married_men[married_men['salary'] == ">50K"]
    high_earners_single = single_men[single_men['salary'] == ">50K"]
    
    married_percentage = (len(high_earners_married) / len(married_men) * 100) if len(married_men) > 0 else 0
    single_percentage = (len(high_earners_single) / len(single_men) * 100) if len(single_men) > 0 else 0

    print(f"Married high earners percentage: {married_percentage:.2f}%")
    print(f"Single high earners percentage: {single_percentage:.2f}%")

def avg_hours_of_working(dataframe):
     avg_hours = (
        dataframe.groupby(['native-country', 'salary'])['hours-per-week']
        .mean()
        .unstack(fill_value=0)
     )
     avg_hours.columns = ['avg_hours_per_week_low', 'avg_hours_per_week_high']
     print(avg_hours.reset_index())

def max_hours_of_working(dataframe):
     result = {
        'max_hours': int(dataframe['hours-per-week'].max()),
        "count_people": 0,
        "percentage_of_high_salary_people": 0
     }
     count_max_hours = (dataframe['hours-per-week'] == result['max_hours']).sum()
     result['count_people'] = int(count_max_hours)
     
     count_high_salary = ((dataframe['hours-per-week'] == result['max_hours']) & 
                         (dataframe['salary'] == '>50K')).sum()
     
     result["percentage_of_high_salary_people"] = str((count_high_salary / count_max_hours) * 100) + '%'
     
     print(f"Max hours per week: {result['max_hours']}, Count of people: {result['count_people']}, Percentage of high salary people: {result['percentage_of_high_salary_people']}")

def classify_age_group(age):
     if 16 <= age < 36:
         return 'young'
     elif 36 <= age < 71:
         return 'adult'
     elif 71 <= age <= 100:
         return 'retiree'
     else:
         return None  

data["AgeGroup"] = data["age"].apply(classify_age_group)

def age_group_salary(data):
     dataf = data[data['salary'] == '>50K']
     result = dataf.groupby("AgeGroup")['salary'].count()
     most_common_age_group = result.idxmax()
     most_common_count = result.max()
     
     print("Количество людей с зарплатой >50K по возрастным группам:")
     for age_group, count in result.items():
          print(f" - {age_group}: {count}")

     print(f"\nНаиболее часто встречающаяся возрастная группа: '{most_common_age_group}' (количество: {most_common_count})")


print("1. Подсчет количества мужчин и женщин:")
get_count(data)

print("\n2. Общее количество записей по полу:")
get_count_all(data)

print("\n3. Средний возраст мужчин:")
avg_age(data)

print("\n4. Процент людей из США:")
us_proportion(data)

print("\n5. Средний и стандартное отклонение возраста для тех, кто зарабатывает больше 50К:")
mean_and_std_more_50k(data)

print("\n6. Средний и стандартное отклонение возраста для тех, кто зарабатывает меньше или равен 50К:")
mean_and_std_less_50k(data)

print("\n7. Более 50% высокооплачиваемых имеют высшее образование:")
higher_educ(data)

print("\n8. Статистика по возрасту для мужчин и женщин:")
stat_for_sex(data)

print("\n9. Статистика по возрасту для разных рас:")
stat_for_race(data)

print("\n10. Процент высокооплачиваемых среди женатых и холостых мужчин:")
high_salary_family_status(data)

print("\n11. Среднее количество часов работы в неделю по странам и зарплате:")
avg_hours_of_working(data)

print("\n12. Максимальное количество часов работы в неделю и процент высокооплачиваемых людей:")
max_hours_of_working(data)

print("\n13. Количество людей с зарплатой >50K по возрастным группам:")
age_group_salary(data) 