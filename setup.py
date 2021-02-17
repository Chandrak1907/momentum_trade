from setuptools import setup,setuptools

setup(name='momentum_trade',
      version='0.1',
      description='Package for trading using AI techniques',
      url='https://github.com/Chandrak1907/momentum_trade',
      author='Chandrashekar Konda',
      author_email='chandrak1907@gmail.com',
      license='',
      packages=setuptools.find_packages(),
    include_package_data=True,
      install_requires=['pandas','datetime', 'pathlib', 'bs4','requests','scipy','numpy','pandas_datareader','gspread_pandas','jupyter-book', 'nsepy', 'timeboard', 'hurst'],
      python_requires='>=3.6',
      zip_safe=False)