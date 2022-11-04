
re_columns_names = [
    'age',
    'how_long',
    'duration',
    'time_for_learn',
    'grade_exist_services',
    'amount_money',
    'Investments',
    'x',
    'change_job',
    'Interesting',
    'Career',
    'Learn_a_language',
    'Income_growth',
    'brain',
    'XXXXXX',
    'Nothing',
    'No_Plan',
    'Little_Practice',
    'Procrastination',
    'Fatigue',
    'Sloth',
    'Not_enough_time',
    'Lack_of_discipline',
    'Absence_of_a_teacher',
    'No_verification_center',
    'Copyright',
    'Expensive',
    'Spam',
    'No_like-minded_people',
    'Lack_of_convenience',
    'Bad_time_management',
    'Lack_of_motivation',
    'c',
    'exact_sciences',
    'humanitarian_sciences',
    'chemestry_biology',
    'psychology',
    'creativity',
    'IT',
    'business',
    'english_or_other',
    'email',
]

def rename_columns(df, rename_list):
    src_columns_names = df.columns.values.tolist()

    columns_dict = dict(zip(src_columns_names, rename_list))
    columns_dict_names = dict(zip(rename_list, src_columns_names))
    df.rename(columns = columns_dict, inplace=True)

    return df
