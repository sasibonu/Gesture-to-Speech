{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import svm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy as sp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os, signals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.externals import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Loading the dataset from 'C:\\Users\\DELL\\Documents\\Data'...\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "module 'signals' has no attribute 'Sample'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-81-8b16a30d9d39>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     18\u001b[0m             \u001b[0mfilename\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m             \u001b[1;31m#Load the sample from file\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 20\u001b[1;33m             \u001b[0msample\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msignals\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSample\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_from_file\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     21\u001b[0m             \u001b[1;31m#Linearize the sample and then add it to the x_data list\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m             \u001b[0mx_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msample\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_linearized\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'signals' has no attribute 'Sample'"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    #List of parameters\n",
    "    SHOW_CONFUSION_MATRIX = False\n",
    "\n",
    "    x_data = []\n",
    "    y_data = []\n",
    "\n",
    "    classes = {}\n",
    "\n",
    "    root=r\"C:\\Users\\DELL\\Documents\\Data\" #Default directory containing the dataset\n",
    "\n",
    "    print (\"Loading the dataset from '{directory}'...\".format(directory=root),)\n",
    "\n",
    "    #Fetch all the data files from the root directory of the dataset\n",
    "    for path, subdirs, files in os.walk(root):\n",
    "        for name in files:\n",
    "            #Get the filename\n",
    "            filename = os.path.join(path, name)\n",
    "            #Load the sample from file\n",
    "            sample = signals.Sample.load_from_file(filename)\n",
    "            #Linearize the sample and then add it to the x_data list\n",
    "            x_data.append(sample.get_linearized())\n",
    "            #Extract the category from the file name\n",
    "            #For example, the file \"a_sample_0.txt\" will be considered as \"a\"\n",
    "            category = name.split(\"_\")[0]\n",
    "            #Get a number for the category, as an offset from the category\n",
    "            #to the a char in Ascii\n",
    "            number = ord(category) - ord(\"a\")\n",
    "            #Add the category to the y_data list\n",
    "            y_data.append(number)\n",
    "            #Include the category and the corresponding number into a dictionary\n",
    "            #for easy access and referencing\n",
    "            classes[number] = category\n",
    "\n",
    "    print (\"DONE\")\n",
    "\n",
    "    #Parameters used in the cross-validated training process\n",
    "    #The library automatically tries every possible combination to\n",
    "    #find the best scoring one.\n",
    "    params = {'C':[0.001,0.01,0.1,1], 'kernel':['linear']}\n",
    "\n",
    "    #Inizialize the model\n",
    "    svc = svm.SVC(probability = True)\n",
    "    #Inizialize the GridSearchCV with 8 processing cores and maximum verbosity\n",
    "    clf = GridSearchCV(svc, params,verbose =10, n_jobs=8)\n",
    "\n",
    "    #Split the dataset into two subset, one used for training and one for testing\n",
    "    X_train, X_test, Y_train, Y_test = train_test_split(x_data, \n",
    "                y_data, test_size=0.35, random_state=0)\n",
    "\n",
    "    print (\"Starting the training process...\")\n",
    "\n",
    "    #Start the training process\n",
    "    clf.fit(X_train, Y_train)\n",
    "\n",
    "    #If SHOW_CONFUSION_MATRIX is true, prints the confusion matrix\n",
    "    if SHOW_CONFUSION_MATRIX:\n",
    "            print (\"Confusion Matrix:\")\n",
    "            Y_predicted = clf.predict(X_test)\n",
    "            print (confusion_matrix(Y_test, Y_predicted), end = '\\n')\n",
    "\n",
    "    print (\"Best estimator parameters: \")\n",
    "    print (clf.best_estimator_)\n",
    "\n",
    "    #Calculates the score of the best estimator found.\n",
    "    score = clf.score(X_test, Y_test)\n",
    "\n",
    "    print (\"\\nSCORE: {score}\\n\".format(score = score))\n",
    "\n",
    "    print (\"Saving the model...\",)\n",
    "\n",
    "    #Saves the model to the \"model.pkl\" file\n",
    "    joblib.dump(clf, 'model.pkl') \n",
    "    #Saves the classes to the \"classes.pkl\" file\n",
    "    joblib.dump(classes, 'classes.pkl') \n",
    "\n",
    "    print (\"DONE\")"
   ]
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
