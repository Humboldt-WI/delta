# Deep Learning for Text Analytics

The master module Deep Learning for Text Analytics (DELTA) is offered at the [Humboldt-University of Berlin](htpps://www.hu-berlin.de) 
by the [Chair of Information Systems](https://www.wiwi.hu-berlin.de/de/professuren/bwl/wi). 

DELTA introduces students to deep learning and natural language processing. We discuss algorithmic foundations, several deep learning methodologies, and their applications in business and society. 

The module draws inspiration from several excellent resources including but not limited to:
- [Natural Language Processing with Deep Learning by Stanford University](https://web.stanford.edu/class/cs224n/)
- [Several awesome educational posts in Jay Alammar's blog](http://jalammar.github.io/)
- [The fantastic interactive e-book Dive into Deep Learning](http://d2l.ai/index.html) 

We greatly appreciate the provision of this great content and highlight its contributions to the design of DELTA. 

## Teaching format
The module is offered every summer semester. Weekly sessions split into a two hour lecture session and a two hour tutorial session. The lecture introduces relevant concepts in the scope of the course. Lecture sessions are accompanied by Jupyter notebooks that demonstrate these concepts using the Python programming language and various Python libraries for deep learning and NLP. Providing working examples and executable codes, the Jupyter notebooks are meant for self-study. To deepen their understanding of the covered topics, students receive programming tasks as homework. The tutorial sessions provide a forum to discuss solutions to the homework task as well as general questions. 

While the time and location of lecture and tutorial sessions may be subject to change, we aim at offering lecture/tutorial sessions as follows:
Lecture: Thu, 10.15 - 11.45,<br>
Q&A Session: Tue, 16:15 - 17:45,<br>
Exercise 1: Thu, 12.15 - 13.45,<br>
Exercise 2: Fri, 10.15 - 11.45

## Outline
The outline of the module is as follows:<br>
- Introduction
  - Course organization and logistics
  - (Supervised) Machine learning revisited \[ [Python demo](https://github.com/Humboldt-WI/adams/blob/master/demos/revisit_bads_stuff/Python-Primer.ipynb), [EDA demo](https://github.com/Humboldt-WI/adams/blob/master/demos/revisit_bads_stuff/Pandas-and-EDA.ipynb), [SKlearn demo](https://github.com/Humboldt-WI/adams/blob/master/demos/revisit_bads_stuff/Python_Machine_Learning.ipynb)\] \[[exercise](https://github.com/Humboldt-WI/adams/blob/master/exercises/tut1_recap_bads_student.ipynb)\]
- Foundations of artificial neural networks 
  - The perceptron model
  - Neural network training using backpropagation and gradient descent \[[demo](https://github.com/Humboldt-WI/adams/blob/master/demos/fnn/nn_foundations.ipynb)\] \[[exercise](https://github.com/Humboldt-WI/adams/blob/master/exercises/tut2_graddesc_student.ipynb) \]
  - Tweaking and tuning feedforward neural networks \[[demo](https://github.com/Humboldt-WI/adams/blob/master/demos/fnn/nn_in_keras.ipynb)\] \[[exercise](https://github.com/Humboldt-WI/adams/blob/master/exercises/tut3_intro_keras_student.ipynb)\]
- Foundations of natural language processing (NLP)
  - NLP pre-processing pipeline, bag of words model, and extensions \[[demo](https://github.com/Humboldt-WI/adams/blob/master/demos/nlp/nlp_foundations.ipynb)\] \[[exercise](https://github.com/Humboldt-WI/adams/blob/master/exercises/tut4_NLP_pipeline_student.ipynb)\]
  - Word embeddings and the Word-to-Vec algorithm \[[W2V demo](https://github.com/Humboldt-WI/adams/blob/master/demos/nlp/word-2-vec.ipynb), [W2V from scratch](https://github.com/Humboldt-WI/adams/blob/master/demos/nlp/w2v_from_scratch.ipynb)\] \[[exercise](https://github.com/Humboldt-WI/adams/blob/master/exercises/tut5_embeddings_student.ipynb)\]
- Recurrent neural networks (RNNs)
  - Processing sequential data using auto-regressive and state-space models 
  - Recurrent cells and recurrent neural networks \[[demo](https://github.com/Humboldt-WI/adams/blob/master/demos/rnn/rnn_foundations.ipynb) \] \[[exercise](https://github.com/Humboldt-WI/adams/blob/master/exercises/tut6_LSTM_student.ipynb)\]
  - RNN training using backpropagation through time
  - Modern RNN architectures \[[lstm demo](https://github.com/Humboldt-WI/adams/blob/master/demos/rnn/lstm_foundations.ipynb), [financial forecasting demo](https://github.com/Humboldt-WI/adams/blob/master/demos/rnn/lstm_fin_forecasting.ipynb)\]
- Convolutional neural networks (CNNs)
  - Computer vision primer
  - Foundations of CNNs \[[demo](https://github.com/Humboldt-WI/adams/blob/master/demos/cnn/cnn_foundations.ipynb)\]
  - Using CNNs for text data \[[external demo from MLMastery.com](https://machinelearningmastery.com/best-practices-document-classification-deep-learning/)\]
- Modern NLP
  - (NLP) Transfer learning \[[sentiment analysis demo](https://github.com/Humboldt-WI/adams/blob/master/demos/nlp/sentiment_analysis.ipynb)\]
  - Attention mechanism
  - The transformer architecture \[[BERT demo](https://github.com/Humboldt-WI/adams/blob/master/demos/nlp/sentiment_analysis_bert.ipynb)\]
- Conclusions 


## Repository organization
The repository provides Jupyter notebooks that revisit concepts covered in the lecture and demonstrate their application using Python. The corresponding notebooks are available in the folder **demos**. The folder **exercises** provides another set of Jupyter notebooks, which task students to practice their Python and Deep Learning skills on programming exercises. The exercises relate to lecture chapters and the demo notebooks. The idea of the exercises is that students try to **solve the programming tasks themselves; possibly together with peers in their study group**. 

More detailed information on the coures format, organization, and logistics is available on the [DELTA Moodle page](https://moodle.hu-berlin.de/course/view.php?id=126682). That page also provides slides for lecture sessions and video recordings. 
