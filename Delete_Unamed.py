import pandas as pd
class DEL():
    def del_unamed(self):
        df_play = pd.read_excel('leave.xlsx')
        unamed = list(df_play.columns)
        for i in unamed:
            if i[0:4]=='Unna':
                del df_play[i]
        df_play.to_excel('leave.xlsx')

    def del_unamed2(self):
        df_play = pd.read_excel('emp_ex.xlsx')
        unamed = list(df_play.columns)
        for i in unamed:
            if i[0:4]=='Unna':
                del df_play[i]
        df_play.to_excel('emp_ex.xlsx')