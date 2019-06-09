{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from sklearn.preprocessing import scale\n",
    "from scipy.interpolate import interp1d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Sample:\n",
    "    def __init__(self, acx, acy, acz, gx, gy, gz, a0, a1, a2, a3, a4):\n",
    "        self.acx = acx\n",
    "        self.acy = acy\n",
    "        self.acz = acz\n",
    "        self.gx = gx\n",
    "        self.gy = gy\n",
    "        self.gz = gz\n",
    "        self.a0 = a0\n",
    "        self.a1 = a1\n",
    "        self.a2 = a2\n",
    "        self.a3 = a3\n",
    "        self.a4 = a4\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_linearized(self, reshape = False):\n",
    "    if reshape:\n",
    "        return np.concatenate((self.acx, self.acy, self.acz, self.gx, self.gy, self.gz, self.a0, self.a1, self.a2, self.a3, self.a4)).reshape(1,-1)\n",
    "    else:\n",
    "        return np.concatenate((self.acx, self.acy, self.acz, self.gx, self.gy, self.gz, self.a0, self.a1, self.a2, self.a3, self.a4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_from_file(filename, size_fit = 50):\n",
    "    data_raw = [map(lambda x: int(x), i.split(\" \")[1:-1]) for i in open(filename)]\n",
    "    data = np.array(data_raw).astype(float)\n",
    "    data_norm = scale(data)\n",
    "    acx = data_norm[:,0]\n",
    "    acy = data_norm[:,1]\n",
    "    acz = data_norm[:,2]\n",
    "\n",
    "\t\t#These rapresent the rotation in the 3 axes\n",
    "    gx = data_norm[:,3]\n",
    "    gy = data_norm[:,4]\n",
    "    gz = data_norm[:,5]\n",
    "\n",
    "\t\t#These represent the flex sensor value\n",
    "    a0 = data_norm[:,6]\n",
    "    a1 = data_norm[:,7]\n",
    "    a2 = data_norm[:,8]\n",
    "    a3 = data_norm[:,9]\n",
    "    a4 = data_norm[:,10]\n",
    "\n",
    "\t\t#Create a function for each axe that interpolates the samples\n",
    "    x = np.linspace(0, data.shape[0], data.shape[0])\n",
    "    f_acx = interp1d(x, acx)\n",
    "    f_acy = interp1d(x, acy)\n",
    "    f_acz = interp1d(x, acz)\n",
    "\n",
    "    f_gx = interp1d(x, gx)\n",
    "    f_gy = interp1d(x, gy)\n",
    "    f_gz = interp1d(x, gz)\n",
    "\n",
    "    f_a0 = interp1d(x, a0)\n",
    "    f_a1 = interp1d(x, a1)\n",
    "    f_a2 = interp1d(x, a2)\n",
    "    f_a3 = interp1d(x, a3)\n",
    "    f_a4 = interp1d(x, a4)\n",
    "\n",
    "\n",
    "\t\t#Create a new sample set with the desired sample size by rescaling\n",
    "\t\t#the original one\n",
    "    xnew = np.linspace(0, data.shape[0], size_fit)\n",
    "    acx_stretch = f_acx(xnew)\n",
    "    acy_stretch = f_acy(xnew)\n",
    "    acz_stretch = f_acz(xnew)\n",
    "\n",
    "    gx_stretch = f_gx(xnew)\n",
    "    gy_stretch = f_gy(xnew)\n",
    "    gz_stretch = f_gz(xnew)\n",
    "\n",
    "    a0_stretch = f_a0(xnew)\n",
    "    a1_stretch = f_a1(xnew)\n",
    "    a2_stretch = f_a2(xnew)\n",
    "    a3_stretch = f_a3(xnew)\n",
    "    a4_stretch = f_a4(xnew)\n",
    "\t\t#Returns a Sample with the calculated values\n",
    "    return Sample(acx_stretch, acy_stretch, acz_stretch, gx_stretch, gy_stretch, gz_stretch, a0_stretch, a1_stretch, a2_stretch, a3_stretch, a4_stretch)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "null",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": "null",
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
