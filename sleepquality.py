import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Load
file_path = "sleepdata.csv"
df = pd.read_csv(file_path, sep=';')

#Cleaning the data
df['Sleep Notes'] = df['Sleep Notes'].fillna('')
df['Wake up'] = df['Wake up'].replace({':|': 'Moderate', ':)': 'Happy'})
df['Drank tea'] = df['Sleep Notes'].str.contains('Drank tea')
df['Drank coffee'] = df['Sleep Notes'].str.contains('Drank coffee')
df['Worked out'] = df['Sleep Notes'].str.contains('Worked out')
df['Ate late'] = df['Sleep Notes'].str.contains('Ate late')
df['Stressful day'] = df['Sleep Notes'].str.contains('Stressful day')
df.drop(['Activity (steps)', 'Sleep Notes'], axis=1, inplace=True)
df['Sleep quality'] = df['Sleep quality'].str.replace('%', '', regex=True).astype(float)
time_in_bed_split = df['Time in bed'].str.split(':', expand=True)
df['Time in bed (hours)'] = (time_in_bed_split[0].astype(float) * 60 + time_in_bed_split[1].astype(float)) / 60
df.drop('Time in bed', axis=1, inplace=True)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Month'] = df['Start'].dt.month
df['Day of week'] = df['Start'].dt.day_name()
df['Time in bed (hours)'] = pd.to_numeric(df['Time in bed (hours)'], errors='coerce')
df['Sleep quality'] = pd.to_numeric(df['Sleep quality'], errors='coerce')
workout_df = df.groupby(['Worked out'])[['Sleep quality', 'Time in bed (hours)', 'Drank tea', 'Drank coffee']].mean()
plt.figure(figsize=(10, 6))
workout_df[['Sleep quality', 'Time in bed (hours)']].plot(
    kind='bar',
    figsize=(10, 6),
    alpha=0.8,
    rot=0,
    title='Effect of Working Out on Sleep Quality and Duration'
)
plt.ylabel('Average')
plt.xlabel('Worked Out (True/False)')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.legend(["Sleep Quality (%)", "Time in Bed (Hours)"])
plt.show()
#Correlation Matrix
numeric_columns = df.select_dtypes(include=['number'])
df_corr = numeric_columns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()
caffeine_df = df.groupby(['Drank tea', 'Drank coffee'])[['Sleep quality', 'Time in bed (hours)']].mean()
print("Average Sleep Scores by Caffeine Intake:")
print(caffeine_df)
plt.figure(figsize=(10, 6))
sns.countplot(x='Day of week', hue='Worked out', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Workout Days by Weekday')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
sns.countplot(x='Day of week', hue='Drank coffee', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Coffee Consumption by Weekday')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
sns.countplot(x='Day of week', hue='Drank tea', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Tea Consumption by Weekday')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Conclusion:")
print("1.onger sleep durations and higher sleep quality are observed on days caffeine is consumed.")
print("2.Workout days align with caffeine consumption.")
print("3.Sunday is a popular day for coffee but not for workouts.")
