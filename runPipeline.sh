jupyter nbconvert --ExecutePreprocessor.timeout=600 --execute ./whyYouAlwaysLying.ipynb

mv ./*.html ./reports
