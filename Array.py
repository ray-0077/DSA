{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def subArray(arr,n):\n",
    "    n= len(arr)\n",
    " \n",
    "    \n",
    "    for i in range(0,n):\n",
    "        for j in range(i,n):\n",
    "            for k in range(i,j+1):\n",
    "                print(arr[k],end=\" \")\n",
    "            print (\"\\n\",end=\"\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 \n",
      "2 7 \n",
      "2 7 5 \n",
      "7 \n",
      "7 5 \n",
      "5 \n"
     ]
    }
   ],
   "source": [
    "subArray([2, 7, 5],3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
