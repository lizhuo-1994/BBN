from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.independencies import Independencies
from pgmpy.inference.EliminationOrder import WeightedMinFill
from random_data import node_values
from network import model
import pandas as pd


data = pd.DataFrame(data=node_values)
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu") # default equivalent_sample_size=5
for cpd in model.get_cpds():
    print(cpd)

print(model.check_model())


############# inference ################
infer = VariableElimination(model)
query = infer.query(variables=['Cheating_Indicator'], evidence={'Satisfaction_with_Reward': 1, 'Subjective_Stress_Level': 2})
print(query)


############# Variables Estimation ################
print(WeightedMinFill(model).get_elimination_order(model.nodes))