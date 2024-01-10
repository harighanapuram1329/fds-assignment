import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def load_data(file_path):
    """
        Load salary data from a CSV file.

        Parameters:
        - file_path (str): The path to the CSV file.

        Returns:
        - pd.DataFrame: A DataFrame containing the salary data.
        """
    return pd.read_csv(file_path , header = None , names = ['Salary'])

def calculate_statistics(data):
    """
        Calculate mean and standard deviation of the salary data.

        Parameters:
        - data (pd.DataFrame): A DataFrame containing the salary data.

        Returns:
        - tuple: A tuple containing mean salary and standard deviation.
        """
    mean_salary = np.mean(data['Salary'])
    std_dev = np.std(data['Salary'])
    return mean_salary , std_dev

def create_histogram(data , mean_salary , std_dev):
    """
       Create a histogram of the salary data and overlay a normal distribution.

       Parameters:
       - data (pd.DataFrame): A DataFrame containing the salary data.
       - mean_salary (float): Mean salary of the data.
       - std_dev (float): Standard deviation of the data.
       """
    plt.hist(data['Salary'] , bins = 30 , density = True , alpha = 0.6 , color = 'orange')
    xmin , xmax = plt.xlim()
    x = np.linspace(xmin , xmax , 100)
    p = norm.pdf(x , mean_salary , std_dev)
    print(x , p)
    plt.plot(x ,  p , 'k' , linewidth = 2)

def calculate_x_percentile(data , percentile):
    """
        Calculate the Xth percentile of the salary data.

        Parameters:
        - data (pd.DataFrame): A DataFrame containing the salary data.
        - percentile (int): The desired percentile.

        Returns:
        - float: The Xth percentile value.
        """
    return np.percentile(data['Salary'] , percentile)


def add_lines_to_plot(mean_salary , X_percentile):
    """
        Add vertical lines to the plot representing mean salary and Xth percentile.

        Parameters:
        - mean_salary (float): Mean salary of the data.
        - X_percentile (float): The Xth percentile value.
        """
    plt.axvline(mean_salary , color = 'r' , linestyle = 'dashed' , linewidth = 2 ,
                label = f'Mean Salary: {mean_salary:.2f} Euros')
    plt.axvline(X_percentile , color = 'g' , linestyle = 'dashed' , linewidth = 2 ,
                label = f'X (25th Percentile): {X_percentile:.2f} Euros')

def show_plot():
    """
        Display the salary distribution plot.
        """
    plt.xlabel('Annual Salary (Euros)')
    plt.ylabel('Probability Density')
    plt.title('Salary Distribution and Statistics')
    plt.legend()
    plt.show()


def print_results(mean_salary , X_percentile):
    """
        Print the calculated statistics.

        Parameters:
        - mean_salary (float): Mean salary of the data.
        - X_percentile (float): The Xth percentile value.
        """
    print(f"Mean Salary (W̃): {mean_salary:.2f} Euros")
    print(f"X (25th Percentile): {X_percentile:.2f} Euros")


def main():
    """
        Main function to execute the salary analysis.
        """
    file_path = "data0-1.csv"
    data = load_data(file_path)

    mean_salary , std_dev = calculate_statistics(data)
    create_histogram(data , mean_salary , std_dev)

    X_percentile = calculate_x_percentile(data , 25)
    add_lines_to_plot(mean_salary , X_percentile)

    show_plot()
    print_results(mean_salary , X_percentile)


if __name__ == "__main__":
    main()
