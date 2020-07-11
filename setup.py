from distutils.core import setup
setup(
  name = 'pyfmp',         
  packages = ['pyfmp'],   
  version = '0.11',      
  license='bsd-3-clause',
  description = 'A wrapper around Financial Modeling Prep\'s api',
  author = 'Dylan E. Holland', 
  author_email = 'salinson1138@gmail.com',
  url = 'https://github.com/DylanEHolland/pyfmp',
  download_url = 'https://github.com/DylanEHolland/pyfmp/archive/0.12.tar.gz', 
  keywords = ['FINANCIAL', 'MODELING', 'PREP', 'API'],
  install_requires=[
          'requests',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',    
  ],
)   