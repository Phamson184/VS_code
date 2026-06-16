import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output_lab2')
CSV_PATH = os.path.join(BASE_DIR, 'processed_dulieuxettuyendaihoc.csv')

os.makedirs(OUTPUT_DIR, exist_ok=True)
def save(name):
    # Luôn ghép tên file với thư mục output tuyệt đối
    file_path = os.path.join(OUTPUT_DIR, f'{name}.png')
    plt.savefig(file_path, dpi=150, bbox_inches='tight')
    plt.close()
    
df = pd.read_csv(CSV_PATH)

df_sort_dh1 = df.sort_values(by='DH1', ascending=True).reset_index(drop=True)
print("\n[Phan 1 - Cau 1] Sap xep DH1 tang dan:")
print(df_sort_dh1[['DH1']].to_string())

df_sort_dh2_gt = df.sort_values(by=['GT', 'DH2'], ascending=[True, True]).reset_index(drop=True)
print("\n[Phan 1 - Cau 2] Sap xep DH2 tang dan theo GT:")
print(df_sort_dh2_gt[['GT', 'DH2']].to_string())

def Q1(x): return x.quantile(0.25)
def Q2(x): return x.quantile(0.50)
def Q3(x): return x.quantile(0.75)
agg_funcs = ['count', 'sum', 'mean', 'median', 'min', 'max', 'std', Q1, Q2, Q3]

pivot_kt = pd.pivot_table(df, values='DH1', index='KT', aggfunc=agg_funcs)
print("\n[Phan 1 - Cau 3] Pivot DH1 theo KT:")
print(pivot_kt.to_string())

pivot_kt_kv = pd.pivot_table(df, values='DH1', index=['KT', 'KV'], aggfunc=agg_funcs)
print("\n[Phan 1 - Cau 4] Pivot DH1 theo KT va KV:")
print(pivot_kt_kv.to_string())

pivot_kt_kv_dt = pd.pivot_table(df, values='DH1', index=['KT', 'KV', 'DT'], aggfunc=agg_funcs)
print("\n[Phan 1 - Cau 5] Pivot DH1 theo KT, KV va DT:")
print(pivot_kt_kv_dt.to_string())

tan_so_gt = df['GT'].value_counts()
tan_suat_gt = df['GT'].value_counts(normalize=True) * 100
df_gt = pd.DataFrame({'Tan so': tan_so_gt, 'Tan suat (%)': tan_suat_gt.round(2)})
print("\n[Phan 2 - Cau 1] Bang tan so/tan suat bien GT:")
print(df_gt.to_string())

plt.figure()
tan_so_gt.plot(kind='bar', color=['#66b3ff', '#ff9999'])
plt.title('Bieu do tan so - Gioi tinh')
plt.xlabel('Gioi tinh')
plt.ylabel('So luong')
plt.xticks(rotation=0)
save('p2_c1_bar_gt')

plt.figure()
tan_so_gt.plot(kind='pie', autopct='%1.1f%%', startangle=90,
               colors=['#66b3ff', '#ff9999'], title='Bieu do tan suat - Gioi tinh')
plt.ylabel('')
save('p2_c1_pie_gt')

for i in [1, 2, 3]:
    col = f'US_TBM{i}'
    print(f"\n[Phan 2 - Cau 2] Mo ta {col}:")
    print(df[col].describe().round(4).to_string())
    plt.figure()
    sns.histplot(df[col], kde=True, color='steelblue')
    plt.title(f'Phan phoi {col}')
    plt.xlabel(col)
    save(f'p2_c2_{col.lower()}')

df_nam = df[df['GT'] == 'M']
ts_dt_nam = df_nam['DT'].value_counts()
tsuat_dt_nam = df_nam['DT'].value_counts(normalize=True) * 100
df_dt_nam = pd.DataFrame({'Tan so': ts_dt_nam, 'Tan suat (%)': tsuat_dt_nam.round(2)})
print("\n[Phan 2 - Cau 3] Bang tan so bien DT voi hoc sinh nam:")
print(df_dt_nam.to_string())
plt.figure()
ts_dt_nam.plot(kind='bar', color='steelblue')
plt.title('Dan toc - Hoc sinh Nam')
plt.xlabel('Dan toc')
plt.ylabel('So luong')
plt.xticks(rotation=0)
save('p2_c3_dt_nam')

nam_kinh_dat_chuan = df[
    (df['GT'] == 'M') & (df['DT'] == 0) &
    (df['DH1'] >= 5.0) & (df['DH2'] >= 4.0) & (df['DH3'] >= 4.0)
]
ts_kv = nam_kinh_dat_chuan['KV'].value_counts()
tsuat_kv = nam_kinh_dat_chuan['KV'].value_counts(normalize=True) * 100
df_kv = pd.DataFrame({'Tan so': ts_kv, 'Tan suat (%)': tsuat_kv.round(2)})
print("\n[Phan 2 - Cau 4] Bang tan so bien KV - Nam Kinh dat chuan:")
print(df_kv.to_string())
plt.figure()
ts_kv.plot(kind='bar', color='coral')
plt.title('Khu vuc - Nam Kinh dat diem san')
plt.xlabel('Khu vuc')
plt.ylabel('So luong')
plt.xticks(rotation=0)
save('p2_c4_kv_nam_kinh')

kv2nt = df[(df['KV'] == '2NT') & (df['DH1'] >= 5.0) & (df['DH2'] >= 5.0) & (df['DH3'] >= 5.0)]
print("\n[Phan 2 - Cau 5] DH1, DH2, DH3 >= 5.0 tai KV 2NT:")
print(kv2nt[['DH1', 'DH2', 'DH3']].describe().round(4).to_string())

df_nu = df[df['GT'] == 'F']
xl_counts = df_nu[['XL1', 'XL2', 'XL3']].apply(pd.Series.value_counts).fillna(0)
order_xl = ['Y', 'TB', 'K', 'G', 'XS']
xl_counts = xl_counts.reindex(order_xl).dropna(how='all')
xl_counts.T.plot(kind='bar', width=0.8)
plt.title('Hoc luc hoc sinh Nu theo tung nam')
plt.xlabel('Nhom xep loai')
plt.ylabel('So luong hoc sinh')
plt.xticks(rotation=0)
plt.legend(title='Xep loai')
save('p3_c1_xl_nu')

df_khoi_kv = df[df['KT'].isin(['A', 'A1', 'B']) & df['KV'].isin(['1', '2'])]
plt.figure()
sns.countplot(data=df_khoi_kv, x='KT', hue='KQXT', palette='Set2')
plt.title('KQXT theo khoi thi A, A1, B tai KV1 & KV2')
save('p3_c2_kqxt_khoi_kv')

plt.figure()
sns.countplot(data=df, x='KV', hue='KT', palette='tab10')
plt.title('So luong thi sinh tung khu vuc theo khoi thi')
save('p3_c3_kv_theo_kt')

plt.figure()
sns.countplot(data=df, x='KT', hue='KQXT', palette='Set2')
plt.title('So luong thi sinh dau/rot tren tung khoi thi')
save('p3_c4_kqxt_theo_kt')

plt.figure()
sns.countplot(data=df, x='KV', hue='KQXT', palette='Set2')
plt.title('So luong thi sinh dau/rot tren tung khu vuc')
save('p3_c5_kqxt_theo_kv')

plt.figure()
sns.countplot(data=df, x='DT', hue='KQXT', palette='Set2')
plt.title('So luong thi sinh dau/rot theo dan toc')
save('p3_c6_kqxt_theo_dt')

plt.figure()
sns.countplot(data=df, x='GT', hue='KQXT', palette='Set2')
plt.title('So luong thi sinh dau/rot theo gioi tinh')
save('p3_c7_kqxt_theo_gt')

plt.figure()
plt.plot(df['T1'].sort_values().values, label='Diem T1', color='purple')
plt.title('Bieu do Simple Line - T1 sap xep tang dan')
plt.ylabel('Diem so')
plt.legend()
save('p4_c1_line_t1')

def phan_loai_t1(d):
    if d < 5.0: return 'k'
    if d < 7.0: return 'tb'
    if d < 8.0: return 'kh'
    return 'g'

df['phanlopt1'] = df['T1'].apply(phan_loai_t1)
ts_pl = df['phanlopt1'].value_counts()
tsuat_pl = df['phanlopt1'].value_counts(normalize=True) * 100
df_pl = pd.DataFrame({'Tan so': ts_pl, 'Tan suat (%)': tsuat_pl.round(2)})
print("\n[Phan 4 - Cau 3] Bang tan so bien phanlopt1:")
print(df_pl.to_string())

order_pl = ['k', 'tb', 'kh', 'g']
df_line = df.groupby('phanlopt1')[['DH1', 'DH2', 'DH3']].mean().reindex(order_pl)
plt.figure()
for col in df_line.columns:
    plt.plot(df_line.index, df_line[col], marker='o', label=f'TB {col}')
plt.title('Multiple Line: Diem thi DH trung binh theo phanlopt1')
plt.xlabel('Phan loai Toan lop 10')
plt.ylabel('Diem trung binh')
plt.legend()
save('p4_c4_multiline_dh')

plt.figure()
for col in df_line.columns:
    plt.vlines(df_line.index, 0, df_line[col], linestyle='dotted', alpha=0.5)
    plt.plot(df_line.index, df_line[col], marker='o', label=f'TB {col}')
plt.title('Drop-line: Diem thi DH trung binh theo phanlopt1')
plt.xlabel('Phan loai Toan lop 10')
plt.ylabel('Diem trung binh')
plt.legend()
save('p4_c5_dropline_dh')

print("\n[Phan 5 - Cau 1] Mo ta phan phoi T1:")
print(df['T1'].describe().round(4).to_string())
print(f"Skewness : {df['T1'].skew():.4f}")
print(f"Kurtosis : {df['T1'].kurt():.4f}")

plt.figure()
sns.boxplot(data=df, y='T1', color='steelblue')
plt.title('Box-Plot bien T1')
save('p5_c1_boxplot_t1')

plt.figure()
sns.histplot(data=df, x='T1', kde=True, color='teal')
plt.title('Histogram + KDE cua T1')
save('p5_c1_hist_t1')

plt.figure()
stats.probplot(df['T1'], dist='norm', plot=plt)
plt.title('Q-Q Plot kiem dinh phan phoi chuan - T1')
save('p5_c1_qq_t1')

for pl in order_pl:
    sub = df[df['phanlopt1'] == pl]['T1']
    plt.figure()
    sns.histplot(sub, kde=True, color='teal')
    plt.title(f'Histogram T1 - nhom {pl}')
    save(f'p5_c2_hist_{pl}')

    plt.figure()
    stats.probplot(sub, dist='norm', plot=plt)
    plt.title(f'Q-Q Plot T1 - nhom {pl}')
    save(f'p5_c2_qq_{pl}')

fig, axes = plt.subplots(1, len(order_pl), figsize=(16, 5))
for ax, pl in zip(axes, order_pl):
    sns.boxplot(data=df[df['phanlopt1'] == pl], y='T1', ax=ax, color='steelblue')
    ax.set_title(f'Box-Plot nhom {pl}')
plt.tight_layout()
save('p5_c2_boxplot_nhom')

cov = df['DH1'].cov(df['T1'])
corr = df['DH1'].corr(df['T1'])
print(f"\n[Phan 5 - Cau 3] Hiep bien DH1-T1  : {cov:.4f}")
print(f"He so tuong quan DH1-T1 : {corr:.4f}")

plt.figure()
sns.scatterplot(data=df, x='T1', y='DH1', color='steelblue')
plt.title('Scatter DH1 vs T1')
save('p5_c3_scatter_dh1_t1')

plt.figure()
sns.scatterplot(data=df, x='T1', y='DH1', hue='KV', palette='Dark2')
plt.title('Scatter DH1 vs T1 theo Khu vuc')
save('p5_c4_scatter_dh1_t1_kv')

cov_matrix = df[['DH1', 'DH2', 'DH3']].cov()
corr_matrix = df[['DH1', 'DH2', 'DH3']].corr()
print("\n[Phan 5 - Cau 5] Ma tran hiep phuong sai:")
print(cov_matrix.round(4).to_string())
print("\nMa tran tuong quan:")
print(corr_matrix.round(4).to_string())

plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.4f', vmin=-1, vmax=1)
plt.title('Ma tran he so tuong quan DH1 / DH2 / DH3')
save('p5_c5_heatmap_corr')

sns.pairplot(df[['DH1', 'DH2', 'DH3']])
plt.suptitle('Scatter Matrix DH1 / DH2 / DH3', y=1.02)
save('p5_c5_scatter_matrix')

print("\nHoan thanh. Bieu do luu tai: output_lab2/")
