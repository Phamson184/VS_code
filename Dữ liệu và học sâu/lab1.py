import pandas as pd
import numpy as np

class Xulydulieu:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        return self

    def dien_kh(self):
        self.df['DT'] = self.df['DT'].fillna(0)
        cotd = [col for col in self.df.columns if col[0] in ['T','L','H','S','V','X','D','N'] and col[1].isdigit()]
        cotd += ['DH1','DH2','DH3']
        for col in cotd:
            if col in self.df.columns:
                self.df[col] = self.df[col].fillna(self.df[col].mean())
        return self

    def diem_tb(self):
        nam_hoc = {1: '1', 2: '2', 3: '6'}
        for i, suffix in nam_hoc.items():
            self.df[f'TBM{i}'] = (self.df[f'T{suffix}']*2 + self.df[f'L{suffix}'] + self.df[f'H{suffix}'] + \
                                  self.df[f'S{suffix}'] + self.df[f'V{suffix}']*2 + self.df[f'X{suffix}'] + \
                                  self.df[f'D{suffix}'] + self.df[f'N{suffix}']) / 10
        return self

    def xet(self, d):
        if d < 5.0: return 'Y'
        if d < 6.5: return 'TB'
        if d < 8.0: return 'K'
        if d < 9.0: return 'G'
        return 'XS'

    def ham_xet_tb(self):
        for i in [1, 2, 3]:
            self.df[f'XL{i}'] = self.df[f'TBM{i}'].apply(self.xet)
        return self

    def thangd4(self):
        for i in [1, 2, 3]:
            be = self.df[f'TBM{i}'].min()
            lon = self.df[f'TBM{i}'].max()
            self.df[f'US_TBM{i}'] = ((self.df[f'TBM{i}'] - be) / (lon - be)) * 4
        return self

    def xet_tuyen(self, row):
        kt = str(row['KT']).strip().upper()
        if kt in ['A','A1']:
            d = (row['DH1']*2 + row['DH2'] + row['DH3']) / 4
        elif kt == 'B':
            d = (row['DH1'] + row['DH2']*2 + row['DH3']) / 4
        else:
            d = (row['DH1'] + row['DH2'] + row['DH3']) / 3
        return 1 if d >= 5.0 else 0

    def ketqua_xt(self):
        self.df['KQXT'] = self.df.apply(self.xet_tuyen, axis=1)
        return self

    def luu(self, output_path):
        self.df.to_csv(output_path, index=False)
        return self

    def chay_chuong_trinh(self, output_path):
        self.load_data()\
            .dien_kh()\
            .diem_tb()\
            .ham_xet_tb()\
            .thangd4()\
            .ketqua_xt()\
            .luu(output_path)
        return self

if __name__ == "__main__":
    processor = Xulydulieu('dulieuxettuyendaihoc.csv')
    processor.chay_chuong_trinh('processed_dulieuxettuyendaihoc.csv')