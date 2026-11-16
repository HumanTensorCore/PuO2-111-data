import dpdata
import matplotlib.pyplot as plt
import numpy as np

training_systems = dpdata.LabeledSystem("/home/zyz/user/zyz/dpgen/3/training_data/training_data_surface", fmt="deepmd/npy")    #训练集
#validation_systems = dpdata.LabeledSystem("/home/zyz/user/zyz/aimd-nom/validation_data", fmt="deepmd/npy")   #对照集

predict_training = training_systems.predict("/home/zyz/user/zyz/dpgen/3/run_pt/iter.000012/00.train/000/frozen_model.pth")
#predict_validation = validation_systems.predict("/home/zyz/user/zyz/dpgen/3/run_pt/iter.000012/00.train.bk000/000/frozen_model.pth")

plt.scatter(training_systems["energies"], predict_training["energies"], s=0.1 ,c='r')
#plt.scatter(validation_systems["energies"], predict_validation["energies"], s=0.1, c='g')


x_range = np.linspace(plt.xlim()[0], plt.xlim()[1])


plt.plot(x_range, x_range, "r--", linewidth=0.25)
plt.xlabel("Energy of DFT")
plt.ylabel("Energy predicted by deep potential")
plt.savefig('test2.png', dpi=300, bbox_inches='tight')
plt.close() 
