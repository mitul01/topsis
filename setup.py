from setuptools import setup

with open("README.md",'r') as fh:
  long_description=fh.read()

setup(
  name = 'TOPSIS_Mitul_101803084',          
  py_modules=['TOPSIS_Mitul_101803084'],
  package_dir={'':'src'},
  version = '0.0.2',     
  license='MIT',      
  description = 'Package for Multiple-criteria decision-making using TOPSIS.Requires input file,weights and impacts. Returns dataframe with score and rank of every label.This package can help improve decision-making.',   # Give a short description about your library
  long_description_content_type='text/markdown',
  long_description=long_description,
  author = 'Mitul Tandon',                
  author_email = 'mitultandon56@gmail.com', 
  url = 'https://github.com/mitul01/topsis',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mitul01/topsis/archive/v0.0.2.tar.gz',    # I explain this later on
  keywords = ['MCDA','TOPSIS','Data Science'],   
  install_requires=[            
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
