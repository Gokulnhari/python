{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b0e8ba7a-24dd-4398-8440-01e0dd111aca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Exercise 10. Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar($)'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Exercise 10. Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar($)'''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "42c38e27-4456-4fe2-9cdc-5a7e44f383fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the amount in pounds (£):  57\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The amount in dollars is: $77.52\n"
     ]
    }
   ],
   "source": [
    "# To enter an amount in pounds\n",
    "pounds = float(input(\"Please enter the amount in pounds (£): \"))\n",
    "\n",
    "# Conversion rate from pounds to dollars\n",
    "conversion_rate = 1.36  \n",
    "\n",
    "# Amount in dollars\n",
    "dollars = pounds * conversion_rate\n",
    "\n",
    "# The converted amount\n",
    "print(f\"The amount in dollars is: ${dollars:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83a7ca0e-a687-46f9-8d0a-c10fbf361b86",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
