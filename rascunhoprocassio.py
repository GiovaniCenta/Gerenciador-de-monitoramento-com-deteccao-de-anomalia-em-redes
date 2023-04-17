
#    COLOCAR NA ML.PY
def print_tree(self, data,model):
    from sklearn.ensemble import IsolationForest
    from sklearn.tree import export_graphviz
    import graphviz
    

    # criar e treinar o modelo Isolation Forest
    X=data

    # imprimir a árvore de decisão
    dot_data = export_graphviz(model.estimators_[0], out_file=None, feature_names=X.columns)
    graph = graphviz.Source(dot_data)
    graph.render("isolation_forest_tree")
    
    
    
# COLOCAR NA APP.PY

ml.print_tree(self.anomaly_data,self.anomaly_model)