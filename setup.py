from distutils.core import setup
setup(
  name = 'pyfmp',         
  packages = ['pyfmp'],   
  version = '0.1',      
  license='bsd-3-clause',
  description = 'A wrapper around Financial Modeling Prep\'s api',
  author = 'Dylan E. Holland', 
  author_email = 'salinson1138@gmail.com',
  url = 'https://github.com/DylanEHolland/pyfmp',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz', 
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
  install_requires=[
          'requests',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD 3-clause "New" or "Revised" license', 
    'Programming Language :: Python :: 3',    
  ],
)   