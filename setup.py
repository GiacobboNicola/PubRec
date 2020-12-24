from distutils.core import setup

setup(
  name = 'PiubRec',
  version = '1.0',      
  license='MIT',  
  description = 'Simple python module to get the number of citations of a paper (or list of papers)',
  author = 'Nicola Giacobbo',
  author_email = 'giacobbo.nicola@gmail.com', 
  url = 'https://github.com/GiacobboNicola/PubRec',   
  download_url = 'https://github.com/GiacobboNicola/PubRec/archive/v1.0.tar.gz', 
  keywords = ['ADS', 'citations'],   
  install_requires=[        
          'bs4',
          'tqdm',
          'argaparse'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)    