import pandas as pd
import numpy as np
import os 

class XulydulieuLab3:
    def __init__(self, file_name):
        thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))
        
        self.file_path = os.path.join(thu_muc_hien_tai, file_name)
        
        self.df = None
    def load_data(self):
        columns = ["Id", "Name", "Age", "Weight", "m0006", "m0612", "m1218", "f0006", "f0612", "f1218"]
        self.df = pd.read_csv(self.file_path, names=columns, engine='python', usecols=range(10))
        return self

    def tach_ten(self):
        self.df[['Firstname', 'Lastname']] = self.df['Name'].str.split(n=1, expand=True)
        self.df = self.df.drop(columns=['Name'])
        return self

    def loai_bo_non_ascii(self):
        self.df['Firstname'] = self.df['Firstname'].str.replace(r'[^\x00-\x7F]+', '', regex=True)
        self.df['Lastname'] = self.df['Lastname'].str.replace(r'[^\x00-\x7F]+', '', regex=True)
        return self

    def chuan_hoa_can_nang(self):
        def convert_w(w):
            if pd.isna(w): return w
            w = str(w).lower().strip()
            if 'lbs' in w: 
                return round(float(w.replace('lbs', '')) / 2.2, 1)
            if 'kgs' in w: 
                return float(w.replace('kgs', ''))
            return float(w)
        
        self.df['Weight'] = self.df['Weight'].apply(convert_w)
        return self

    def xoa_du_lieu_rong_va_trung(self):
        self.df = self.df.dropna(how='all')
        # Trade-off: Chạy sau loai_bo_non_ascii có thể gộp "Mickéy" và "Mickey" thành 1 người, rủi ro xóa nhầm là có nhưng logic làm sạch đồng nhất hơn.
        self.df = self.df.drop_duplicates(subset=['Firstname', 'Lastname', 'Age', 'Weight'])
        return self

    def xu_ly_thieu_tuoi_can_nang(self):
        self.df = self.df.dropna(subset=['Age', 'Weight'], how='all')
        self.df['Age'] = self.df['Age'].fillna(round(self.df['Age'].mean())).astype(int)
        self.df['Weight'] = self.df['Weight'].fillna(round(self.df['Weight'].mean(), 1))
        return self

    def melt_data(self):
        self.df = pd.melt(
            self.df, 
            id_vars=['Id', 'Firstname', 'Lastname', 'Age', 'Weight'], 
            value_vars=['m0006', 'm0612', 'm1218', 'f0006', 'f0612', 'f1218'], 
            var_name='sex_and_time', 
            value_name='PulseRate'
        )
        self.df['Sex'] = self.df['sex_and_time'].str[0]
        self.df['Time'] = self.df['sex_and_time'].str[1:3] + '-' + self.df['sex_and_time'].str[3:5]
        self.df = self.df.drop(columns=['sex_and_time'])
        return self

    def xu_ly_thieu_nhip_tim(self):
        self.df['PulseRate'] = self.df['PulseRate'].replace('-', np.nan).astype(float)
        
        def fill_pulse(group):
            pulse = group['PulseRate'].copy()
            for i in pulse[pulse.isna()].index:
                pos = group.index.get_loc(i)
                vals = pulse.dropna().values
                
                before = pulse.iloc[pos-1] if pos > 0 else np.nan
                after  = pulse.iloc[pos+1] if pos < len(pulse)-1 else np.nan
                if not np.isnan(before) and not np.isnan(after):
                    pulse.at[i] = round((before + after) / 2, 1)
                    continue
                
                if pos >= 2 and not np.isnan(pulse.iloc[pos-1]) and not np.isnan(pulse.iloc[pos-2]):
                    pulse.at[i] = round((pulse.iloc[pos-1] + pulse.iloc[pos-2]) / 2, 1)
                    continue

                if pos+2 < len(pulse) and not np.isnan(pulse.iloc[pos+1]) and not np.isnan(pulse.iloc[pos+2]):
                    pulse.at[i] = round((pulse.iloc[pos+1] + pulse.iloc[pos+2]) / 2, 1)
                    continue

                if len(vals) > 0:
                    pulse.at[i] = round(vals.mean(), 1)
                    continue
                    
            return pulse
        
        self.df['PulseRate'] = self.df.groupby('Id', group_keys=False).apply(fill_pulse)
        
        sex_mean = self.df.groupby('Sex')['PulseRate'].transform('mean')
        self.df['PulseRate'] = self.df['PulseRate'].fillna(sex_mean.round(1))
        
        global_mean = round(self.df['PulseRate'].mean(), 1)
        self.df['PulseRate'] = self.df['PulseRate'].fillna(global_mean if not np.isnan(global_mean) else 72.0)
        return self

    def luu_du_lieu(self, output_path):
        self.df.to_csv(output_path, index=False)
        return self

    def hien_thi(self):
        print(f"Shape: {self.df.shape}")
        print(f"Missing: {self.df['PulseRate'].isna().sum()} PulseRate NaN")
        print(self.df.to_string(max_rows=15))
        return self

    def chay_chuong_trinh(self):
        (self.load_data()
             .tach_ten()
             .loai_bo_non_ascii()
             .chuan_hoa_can_nang()
             .xoa_du_lieu_rong_va_trung()
             .xu_ly_thieu_tuoi_can_nang()
             .melt_data()
             .xu_ly_thieu_nhip_tim()
             .hien_thi()
             .luu_du_lieu('patient_heart_rate_clean.csv'))
        return self


if __name__ == '__main__':
    pipeline = XulydulieuLab3('patient_heart_rate.csv')
    pipeline.chay_chuong_trinh()