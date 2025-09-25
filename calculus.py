import pandas as pd

def report(c, ai1, p1, ai2, p2, aar) :
    """
    Generate a pandas dataframe with columns: 'Year', 'Capital', 'Cumulative', 'Yeld', 'Annual Income'
    
    Parameters:
    c = initial capital 
    ai1 = initial annual saving 
    p1 = period for first annual saving (Years)
    ai2 = second annual saving 
    p2 = period for second annual saving (Years)
    aar = average annual return (%)
    """
    df = pd.DataFrame(columns=['Year', 'Capital', 'Cumulative', 'Yeld', 'Annual Income'])
    cumulative = c
    year = 0
    start = {'Year': year, 'Capital': c, 'Annual Income':c, 'Cumulative':c, 'Yeld':0}
    df.loc[0] = start
    for i in range(1, p1+1) :
        year += 1
        investment = ai1 + (df.iloc[-1,1]*(1+aar/100)).round(2)
        cumulative = cumulative + ai1
        yeld = investment - cumulative
        
        n = {'Year': year, 'Capital': investment, 'Cumulative':cumulative, 'Yeld': yeld, 'Annual Income':ai1}
        df.loc[len(df)] = n

    if(p2 != 0):
        for i in range(1, p2+1) :
            year += 1
            investment = ai2 + (df.iloc[-1,1]*(1+aar/100)).round(2)
            cumulative = cumulative + ai2
            yeld = investment - cumulative
            
            n = {'Year': year, 'Capital': investment, 'Cumulative':cumulative, 'Yeld': yeld, 'Annual Income':ai2}
            df.loc[len(df)] = n

    return df


def insert_input(message, complete, flag_float):
    """
    Insert a float number and return it
    """
    complete = False
    while not complete:
        try:
            value = float(input(message)) if flag_float else int(input(message))
            complete = True
            return value
        except ValueError:
            print("Sorry, Not a valid Number, please, retry.")

def interesting_calculus():
    """
    Start input request to generate a report about compound interest
    """
    complete = False
    while not complete:
        start_capital = insert_input('Insert initial capital', complete, True)
        annual_investment1 = insert_input('Insert annual investment', complete, True)
        investment_period1 = insert_input('Insert investment period (Years)', complete, False)
        average_annual_return = insert_input('Insert average annual return (%)', complete, True)
        flag = input('Prevision to change after? (Y/N)').upper()
        if (flag == 'Y'):
            annual_investment2 = insert_input('Insert annual investment (2nd)', complete, True)
            investment_period2 = insert_input('Insert investment period (Years) (2nd)', complete, False)
        else:
            annual_investment2 = 0
            investment_period2 = 0
        complete=True
    
    return report( start_capital, annual_investment1, investment_period1, annual_investment2, investment_period2, average_annual_return )

interesting_calculus()