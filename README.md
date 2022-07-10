# Zeiny_UI
- In this repo the built Covid-19_detector UI will be described

## Content
- [Prerequisites](#prerequisites)
- [Descrition](#description)

## Prerequisites
- Just install the libraries in the [requirements.txt](requirements.txt) file.

## Description
- This UI was build using [streamlit cloud](https://share.streamlit.io/), where it will be linked to this repo and continuos deployment will be done between them using this [Webhook](https://github.com/Zeiny96/Zeiny_MLOPS/settings/hooks/366762329).
- Then to be continuosly integrated [Test.yaml](.github/workflows/Test_CI.yaml) was created to run [test_model.py](test/test_model.py) to assert that the model is running properly.
- The main UI code can be found at [app.py](app.py).
- To use this UI just go to the [UI link](https://zeiny96-zeiny-mlops-app-ui-36ebwy.streamlitapp.com/) and follow the instructions there.
