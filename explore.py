import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats


def get_swarmplot(train):
    '''
    Function takes in a split of the dataset and returns a swarmplot to compare telco customer churn to monthly charges.
    '''
    # Create a swarm plot
    target = 'churn'
    sns.set(style="whitegrid")  # Set the style of the plot
    plt.figure(figsize=(8, 6))

    sns.swarmplot(y='monthly_charges', x=target, data=train)

    # Add labels and title
    plt.ylabel('Monthly Charges')
    plt.xlabel('Churn')
    plt.title('Swarm Plot of Churn by Monthly Charges')

    # Calculate y-tick positions and labels
    tick_positions = range(20, 121, 10)
    tick_labels = ['${:.2f}'.format(tick) for tick in tick_positions]

    # Set y-tick positions and labels
    plt.yticks(ticks=tick_positions, labels=tick_labels)

    # Limit y-axis range
    plt.ylim(10, 120)

    # Show the plot
    return plt.show()

def get_countplot_contract_type(train):
    '''
    Function takes in a split of the dataset and returns a countplot of churn by Contract Type.
    '''
    # Set style of plot
    sns.set(style="whitegrid")
    data = train
    # Create plot
    sns.countplot(x="contract_type", hue="churn", data=data)
    # Labels and title
    plt.ylabel('Count')
    plt.xlabel('Contract Type')
    plt.title("Churn Count by Contract Type")
    return plt.show()

def get_countplot_IST(train):
    '''
    Function takes in a split of the dataset and returns a countplot of churn by Internet Service Type.
    '''
    # Set style of plot
    sns.set(style="whitegrid")
    data = train
    # Create plot
    sns.countplot(x="internet_service_type", hue="churn", data=data)
    # Labels and title
    plt.ylabel('Count')
    plt.xlabel('Internet Service Type')
    plt.title("Churn Count by Internet Service Type")
    return plt.show()

def get_countplot_pmnt(train):
    '''
    Function takes in a split of the dataset and returns a countplot of churn by Payment Type.    
    '''
    # Set style of plot
    sns.set(style="whitegrid")
    data = train
    # Create count plot
    sns.countplot(x="mapped_payment_type", hue="churn", data=data)
    plt.ylabel('Count')
    plt.xlabel('Payment Type')   
    plt.title("Churn Count by Payment Type(Auto v Manual)")
    return plt.show()

def get_countplot_fiber_techsupport(train):
    '''
    Function takes in a split of the dataset and returns a countplot of Fiber optic customer churn by whether or not they have tech support.
    '''
    # create subset for only fiber optic customers
    fiber_subset = train[train['internet_service_type'] == 'Fiber optic']
    # Create count plot
    sns.countplot(x="tech_support", hue="churn", data=fiber_subset)
    # Labels and title
    plt.ylabel('Count')
    plt.xlabel('Tech Support')    
    plt.title("Churn Count of Fiber optic Customers w/ Tech Support")
    return plt.show()
