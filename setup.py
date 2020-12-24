import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'PubRec',
  version = '1.0',      
  license ='MIT',  
  description = 'Simple python module to get the number of citations of a paper (or list of papers)',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Nicola Giacobbo',
  author_email = 'giacobbo.nicola@gmail.com', 
  url = 'https://github.com/GiacobboNicola/PubRec',   
  download_url = 'https://github.com/GiacobboNicola/PubRec/archive/v1.0.tar.gz', 
  keywords = ['ADS', 'citations'],
  packages=setuptools.find_packages(),
  install_requires=[        
          'bs4',
          'tqdm',
          'argaparse'
      ],
  classifiers = [
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)