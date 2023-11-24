# Attribute_extraction_app

To understand schema of dataset, please have look at seed.csv and test.csv files.

I have used ETHOS dataset(partial) to extract attribute values for the given keys:
1. directed_vs_generalized
2. gender
3. violence

To have a detailed look for their description, please look at config_ethos.json

To try out the app, please follow the below steps:
1. Clone this repo
2. Edit your OpenAI's API key in main.py
3. pip install -r requirements.txt
4. python config_converter.py(in case config_ethos.json is not converted into testop.json)
5. python main.py

For exact steps and outputs, you can have a look at my colab notebook here: https://colab.research.google.com/drive/125Mzz83MYQumDOZPetRFpGZfwjE_2wz1?usp=sharing