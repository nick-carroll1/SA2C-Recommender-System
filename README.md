# SA2C-Recommender-System

This is a recommender system developed as a homework assignment for Duke AIPI 531 - Deep Reinforcement Learning Applications.  It is designed to compare model performance between recommenders that use and do not use item features.  The recommender system is based upon the research paper: Supervised Advantage Actor-Critic for Recommender Systems by Xin Xin et al, which can be found here (https://arxiv.org/abs/2111.03474) and the original source code for this type of recommender system can be found here (https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F185KB520pBLgwmiuEe7JO78kUwUL_F45t%2Fview%3Fusp%3Dsharing).

The source code has been modified to add item feature information based upon the research paper Temporal-Contextual Recommendation in Real-Time by Yifei Ma et al, which can be found here (https://assets.amazon.science/96/71/d1f25754497681133c7aa2b7eb05/temporal-contextual-recommendation-in-real-time.pdf).

This repository has: the original source code for the Supervised Advantage Actor-Critic Recommender System in SA2C.py, a slightly modified version of this (for use with Tensorflow v2 and easy of use in the comparison notebook) is in SA2C_new.py, and the code modified to add item feature information based on Yifei Ma et al is in SA2C_v2.py.
