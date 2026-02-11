import pandas as pd
import matplotlib.pyplot as plt

csv_path = "D:\\train.csv"
df = pd.read_csv(csv_path)
print('\nMissing value statistics')
print(df.isnull().sum())
#处理缺值
df['Age'] = df['Age'].fillna(df['Age'].median())
#创建大画板
fig,axes=plt.subplots(1,3,figsize=(18,6))
#SEX
#不同性别生还率
female_survived=df[df['Sex']=='female']['Survived'].mean()
male_survived=df[df['Sex']=='male']['Survived'].mean()
#性别饼状图
size=[female_survived*100,male_survived*100]
labels=['female','male']
colors=['green','blue']
axes[0].pie(size,labels=labels,colors=colors,autopct='%1.1f%%')
axes[0].set_title('Survival Rate by Sex')

#PCLASS
#不同船舱等级幸存人数
pclass_1_survived = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]['Survived'].sum()
pclass_2_survived = df[(df['Pclass'] == 2) & (df['Survived'] == 1)]['Survived'].sum()
pclass_3_survived = df[(df['Pclass'] == 3) & (df['Survived'] == 1)]['Survived'].sum()
#船舱等级条形图
categories=['Pclass1','Pclass2','Pclass3']
pclass_survived=[pclass_1_survived,pclass_2_survived,pclass_3_survived]
axes[1].bar(categories,pclass_survived,color='pink')
axes[1].set_title('Survival Count by Pclass')
axes[1].set_xlabel('Pclass Group')
axes[1].set_ylabel('Number Of Survival')

#AGE
#各年龄段幸存人数
survived_df=df[df['Survived']==1].copy()                 #筛选活人
bins=[0,12,18,30,50,100]                                 #年龄分组
labels=['child','teen','young','middle','senior']        #各年龄段设置标签
survived_df['AgeGroup']=pd.cut(survived_df['Age'],bins=bins,labels=labels,right=False)
#按标签统计各分组人数
age_counts=survived_df['AgeGroup'].value_counts().sort_index()
#画图
bars=axes[2].bar(age_counts.index,age_counts.values,color='purple')
#标人数
for bar in bars:
    axes[2].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+1,
        f'{int(bar.get_height())}ppl',
        ha='center', fontsize=11
    )


axes[2].set_title('Survival Count By Age',fontsize=14,fontweight='bold')
axes[2].set_xlabel('Age Group')
axes[2].set_ylabel('Number Of Survival')
plt.tight_layout()
plt.savefig('titanic_chart.png')
plt.show()


print('Running completed! Generated chart file: titanic_chart.pngs')
