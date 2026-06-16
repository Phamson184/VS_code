import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

class TitanicDataPrep:
    def __init__(self, train_file, test_file):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(self.base_dir, 'output_lab4')
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.train_path = os.path.join(self.base_dir, train_file)
        self.test_path = os.path.join(self.base_dir, test_file)
        self.df = None

    def save_plot(self, name):
        file_path = os.path.join(self.output_dir, f'{name}.png')
        plt.savefig(file_path, dpi=150, bbox_inches='tight')
        plt.close()
    
    def load_data(self):
        """1. Tải và xem dữ liệu"""
        df_train = pd.read_csv(self.train_path)
        df_test = pd.read_csv(self.test_path)
        
        df_train['Dataset'] = 'Train'
        df_test['Dataset'] = 'Test'
        
        self.df = pd.concat([df_train, df_test], ignore_index=True)
        print("\n[Phan 1 - Cau 1] 10 dong dau tien cua du lieu:")
        print(self.df.head(10).to_string())
        return self

    def khao_sat_thieu_du_lieu(self, step_name="truoc_xu_ly"):
        print(f"\n[Phan 1 - Cau 2] Thong ke du lieu thieu ({step_name}):")
        print(self.df.isnull().sum())
        
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
        plt.title(f'Bieu do Heat map du lieu thieu ({step_name})')
        self.save_plot(f'p1_c2_heatmap_missing_{step_name}')
        return self

    def xu_ly_name(self):
        self.df[['firstName', 'secondName']] = self.df['Name'].str.split(', ', n=1, expand=True)
        self.df = self.df.drop(columns=['Name'])
        return self

    def chuan_hoa_sex(self):
        self.df['Sex'] = self.df['Sex'].replace({'male': 'M', 'female': 'F'})
        return self

    def xu_ly_age(self):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Pclass', y='Age', data=self.df, palette='Set2')
        plt.title('Phan phoi Tuoi (Age) theo Hang ve (Pclass)')
        self.save_plot('p1_c5_boxplot_age_pclass')
        
        print("\n[Nhận xét Câu 5] Tuổi trung bình theo nhóm Pclass:")
        print(self.df.groupby('Pclass')['Age'].mean().round(1))
        print("-> QUYẾT ĐỊNH: Dùng giá trị trung bình theo từng hạng vé (Pclass) để điền khuyết vì phân phối tuổi ở các hạng vé khác nhau rõ rệt.")
        
        self.df['Age'] = self.df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))
        self.khao_sat_thieu_du_lieu(step_name="sau_khi_xu_ly_Age")
        return self

    def tao_agegroup(self):
        bins = [0, 12, 18, 60, float('inf')]
        labels = ['Kid', 'Teen', 'Adult', 'Older']
        self.df['Agegroup'] = pd.cut(self.df['Age'], bins=bins, labels=labels, right=True)
        return self

    def trich_xuat_nameprefix(self):
        self.df['namePrefix'] = self.df['secondName'].str.extract(r'^([^.]+)\.')
        self.df['secondName'] = self.df['secondName'].str.extract(r'^\S+\.\s*(.*)')
        return self

    def tinh_familysize_va_alone(self):
        self.df['familySize'] = 1 + self.df['SibSp'] + self.df['Parch']
        self.df['Alone'] = np.where(self.df['familySize'] == 1, 1, 0)
        return self

    def xu_ly_cabin(self):
        self.df['typeCabin'] = self.df['Cabin'].fillna('Unknown').astype(str).str[0]
        return self

    def loai_bo_trung_lap(self):
        before_drop = len(self.df)

        self.df['Dataset'] = pd.Categorical(self.df['Dataset'], categories=['Train', 'Test'], ordered=True)
        self.df = self.df.sort_values('Dataset') 
        
        self.df = self.df.drop_duplicates(subset=['firstName', 'secondName', 'Age', 'Sex'], keep='first')
        after_drop = len(self.df)
        print(f"\n[Phan 1 - Cau 11] Đã loại bỏ {before_drop - after_drop} dòng trùng lặp (Ưu tiên giữ Train).")
        return self
    
    def thuc_hien_eda(self):
        print("\n--- BẮT ĐẦU PHẦN 2: EDA (Trực quan hóa) ---")
        df_eda = self.df[self.df['Dataset'] == 'Train'].copy()
        df_eda['Survived'] = df_eda['Survived'].replace({0: 'No', 1: 'Yes'})

        plt.figure()
        sns.countplot(data=df_eda, x='Sex', hue='Survived', palette='Set1')
        plt.title('Tỉ lệ sống sót theo Giới tính')
        self.save_plot('p2_c12_survived_sex')

        plt.figure()
        sns.countplot(data=df_eda, x='Pclass', hue='Survived', palette='Set2')
        plt.title('Tỉ lệ sống sót theo Hạng vé (Pclass)')
        self.save_plot('p2_c13_survived_pclass')

        g14 = sns.catplot(data=df_eda, x='Agegroup', hue='Survived', col='Sex', kind='count', palette='Set1')
        g14.figure.suptitle('Sống sót theo Nhóm tuổi và Giới tính', y=1.05)
        g14.figure.savefig(os.path.join(self.output_dir, 'p2_c14_survived_agegroup_sex.png'), dpi=150, bbox_inches='tight')
        plt.close()

        df_alone = df_eda.copy()
        df_alone['Survived_num'] = (df_alone['Survived'] == 'Yes').astype(int)
        
        plt.figure()
        sns.barplot(data=df_alone, x='Alone', y='Survived_num', palette='Set3')
        plt.title('Xác suất sống sót theo trạng thái đi một mình (Alone)')
        plt.ylabel('Tỉ lệ sống sót')
        plt.xticks([0, 1], ['Đi cùng gia đình (0)', 'Đi một mình (1)'])
        self.save_plot('p2_c15_survived_alone')

        plt.figure()
        sns.histplot(data=df_eda, x='Fare', hue='Survived', kde=True, bins=30, palette='Set1')
        plt.title('Phân phối giá vé (Fare) theo Khả năng sống sót')
        self.save_plot('p2_c16_survived_fare')

        g17 = sns.catplot(data=df_eda, x='Pclass', hue='Survived', col='Embarked', kind='count', palette='Set2')
        g17.figure.suptitle('Sống sót theo Pclass và Cảng cập bến (Embarked)', y=1.05)
        g17.figure.savefig(os.path.join(self.output_dir, 'p2_c17_survived_pclass_embarked.png'), dpi=150, bbox_inches='tight')
        plt.close()

        print("Đã xuất toàn bộ biểu đồ Phần 2 ra thư mục output_lab4!")
        return self

    def chay_chuong_trinh(self):
        (self.load_data()
             .khao_sat_thieu_du_lieu()
             .xu_ly_name()
             .chuan_hoa_sex()
             .xu_ly_age()
             .tao_agegroup()
             .trich_xuat_nameprefix()
             .tinh_familysize_va_alone()
             .xu_ly_cabin()
             .loai_bo_trung_lap()
             .thuc_hien_eda())
        
        clean_path = os.path.join(self.output_dir, 'titanic_cleaned.csv')
        self.df.to_csv(clean_path, index=False)
        print(f"\n[Hoàn thành] Dữ liệu sạch đã được lưu tại: {clean_path}")
        return self

if __name__ == '__main__':
    pipeline = TitanicDataPrep('train.csv', 'test.csv')
    pipeline.chay_chuong_trinh()