# Shopping cart project

[Project Description]
https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/README.md#repo-setup

## Prerequisites

+ Python 3.7 or greater

## Installation

Clone or download this repository onto your computer. Then navigate into the project repository:

'''
cd shoppingcart
'''

## Setup

Create a new project-specific virtual environment:

'''
conda create -n shopping-env python=3.8
'''

Activate the virtual environment:

'''
conda activate shopping-env
'''

Install third-party packages, as necessary:

'''
pip-install -r requirements.txt
'''


## Usage

Run the program:

'''py
python shopping_cart.py
'''

To include a custom tax rate, please use the following format in your .env file:

#This is your .env file

TAX_RATE = Your tax rate, ex: 0.1
