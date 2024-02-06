import pandas as pd

def parse_df(df):
    """
    INPUT 
        - df: crime counts/rates data frame with columns "FeatureCode", "FeatureName", "DateCode", "Crime or Offence".
    OUTPUT: 
        - crimes_ratios_df: crime rates data frame containing ratios values only, excluding for 'Scotland' LAD.
    """
    try:
        # I will rename columns here, so they are more clear
        df.rename(columns={"FeatureCode": "LAD Code", "FeatureName": "LAD", "DateCode": "Date", "Crime or Offence": "Crime"}, inplace=True)
    except KeyError:
        print("Columns 'FeatureCode', 'FeatureName', 'DataCode' and 'Crime or Offence' are required.")

    #  The df dataset, contains different types of Crimes & Offenses, measured as ratios or counts. I will:
    #      - Focus only on crimes (and not offences) 
    #      - Focus only on ratios (and not on counts)
    #      - Removen redundant string "Crimes: " from Crime variable
    #      - Remove 'Scotland' from LAD column

    # Focus on ratios
    crimes_ratios_df = df[df["Measurement"]=="Ratio"]
    # Focus on crimes
    crimes_ratios_df = crimes_ratios_df[crimes_ratios_df["Crime"].str.contains("Crimes")]
    # Remove redundant string "Crimes: " in Crime column, as it'll look better when plotting
    crimes_ratios_df["Crime"] = crimes_ratios_df["Crime"].str.removeprefix("Crimes: ")
    # Remove Scotland
    crimes_ratios_df = crimes_ratios_df[crimes_ratios_df["LAD"]!="Scotland"]

    # Here I am creating ordered categorical variables, so they are plotted correctly on graphs
    ordered_date = ['1996/1997', '1997/1998', '1998/1999', '1999/2000', '2000/2001',
                    '2001/2002', '2002/2003', '2003/2004', '2004/2005', '2005/2006',
                    '2006/2007', '2007/2008', '2008/2009', '2009/2010', '2010/2011',
                    '2011/2012', '2012/2013', '2013/2014', '2014/2015', '2015/2016',
                    '2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021',
                    '2021/2022', '2022/2023']

    crimes_ratios_df["Date"] = pd.Categorical(crimes_ratios_df["Date"], categories=ordered_date, ordered=True)

    ordered_crimes = ['All Crimes', 'All Group 3: Crimes of dishonesty','All Group 5: Crimes against society',
                    'Coronavirus Restrictions',
                    'Group 1: Common assault',
                    'Group 1: Death by dangerous driving',
                    'Group 1: Domestic Abuse (Scotland) Act 2018',
                    'Group 1: Murder and culpable homicide',
                    'Group 1: Other non-sexual violence',
                    'Group 1: Robbery',
                    'Group 1: Serious assault and attempted murder',
                    'Group 2: Causing to view sexual activity or images',
                    'Group 2: Communicating indecently',
                    'Group 2: Crimes associated with prostitution',
                    'Group 2: Indecent photos of children',
                    'Group 2: Other sexual crimes',
                    'Group 2: Rape & attempted rape',
                    'Group 2: Sexual assault',
                    'Group 2: Threatening to or disclosing intimate images',
                    'Group 3: Fraud', 
                    'Group 3: Housebreaking',
                    'Group 3: Other dishonesty',
                    'Group 3: Other theft', 
                    'Group 3: Shoplifting',
                    'Group 3: Theft by opening lockfast places',
                    'Group 3: Theft from a motor vehicle',
                    'Group 3: Theft of a motor vehicle',
                    'Group 4: Fire-raising',
                    'Group 4: Reckless conduct',
                    'Group 4: Vandalism',
                    'Group 5: Crimes against public justice',
                    'Group 5: Drugs - Possession',
                    'Group 5: Drugs - Supply',
                    'Group 5: Other crimes against society',
                    'Group 5: Weapons possession (not used)',
                    'Group 5: Weapons possession (used)']

    crimes_ratios_df["Crime"] = pd.Categorical(crimes_ratios_df["Crime"], categories=ordered_crimes, ordered=True)

    return crimes_ratios_df, ordered_crimes