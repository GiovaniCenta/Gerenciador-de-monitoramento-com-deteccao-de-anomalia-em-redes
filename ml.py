from sklearn.ensemble import IsolationForest
import numpy as np
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class ML(): 
    def __init__(self, model,  cv=5, scoring='accuracy', n_jobs=-1, verbose=1, random_state=0):
        
        self.model = model
        self.cv = cv
        self.scoring = scoring
        self.n_jobs = n_jobs
        self.verbose = verbose
        self.random_state = random_state
        self.best_estimator_ = None
        self.best_score_ = None
        self.best_params_ = None
        self.best_index_ = None
        self.grid_scores_ = None
        self.grid_search_ = None
        self.cv_results_ = None
        self.cv_results_df_ = None
        self.y_pred_ = None
        self.y_pred_proba_ = None
        self.y_pred_proba_df_ = None
        self.fig, self.ax = plt.subplots(4, 1, sharex=True)
        self.fig.suptitle("Monitoramento em tempo real")
        self.ax[0].set_ylabel("Largura de banda")
        self.ax[1].set_ylabel("Uso de memória")
        self.ax[2].set_ylabel("Uso de CPU")
        self.ax[3].set_ylabel("Uso de disco")
        self.ax[3].set_xlabel("Tempo")
    
    def train_anomaly_detector(self,data):
        #escalarizar os dados
        scaler = StandardScaler()
        data = scaler.fit_transform(data)
        #treinar o modelo
        self.model.fit(data)
        return self.model
    
    def update_realtime_chart(self, data):
        data_np = np.array(data)
        time_axis = range(data_np.shape[0])

        # Atualizar os dados dos gráficos
        for i in range(4):
            self.ax[i].clear()

        self.ax[0].plot(time_axis, data_np[:, 18], label="Largura de banda")
        self.ax[1].plot(time_axis, data_np[:, 5], label="Uso de memória")
        self.ax[2].plot(time_axis, data_np[:, 1], label="Uso de CPU")
        self.ax[3].plot(time_axis, data_np[:, 9], label="Uso de disco")

        # Redesenhar os gráficos
        plt.pause(0.01)
        plt.draw()

    def feature_importance(self,feature_names):
        feature_importances = self.anomaly_model.feature_importances_
        important_features = np.argsort(feature_importances)[-3:]
        print("As 3 métricas mais importantes na detecção de anomalias são:", [feature_names[i] for i in important_features])

    def anomaly_per_time(self,timestamps,predictions):
        import matplotlib.pyplot as plt

        anomaly_timestamps = [timestamp for timestamp, prediction in zip(timestamps, predictions) if prediction == -1]
        plt.scatter(anomaly_timestamps, [-1] * len(anomaly_timestamps), color='red', marker='x', label='Anomalias detectadas')
        plt.xlabel('Tempo')
        plt.ylabel('Anomalia')
        plt.legend()
        plt.show()
            

