import pandas as pd


# Reading CSV Files
df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')

# Mapping Yes or No values as True or False boolean expression
def mappingYesOrNo(value):
    return value in ['Yes', 'True', 'TRUE', 'yes']


df['Hobbyist'] = df['Hobbyist'].apply(mappingYesOrNo)
print(df['Hobbyist'])


# Changing the name of ConvertedComp into Salary
df.rename(columns={'ConvertedComp': 'Salary'}, inplace=True)

# Calculate the mean salary for each country
meanSalary_byCountry = df.groupby('Country')['Salary'].mean()

# Calculate the highest salary with Python
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
mean_salary_by_country_with_python = df.loc[filt].groupby('Country')['Salary'].max()

# Get the top five most popular programming languages and their corresponding average salaries
avg_salary_by_language = df.groupby('LanguageWorkedWith')['Salary'].mean()
top_languages_and_salaries = avg_salary_by_language.sort_values(ascending=False).head(5)

print(top_languages_and_salaries)