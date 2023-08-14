from pgmpy.models import BayesianNetwork
node_states = {
    'Weekday': {
        'name': 'Q1',
        'states': 7,
        'next_nodes': ['Cheating_indicator']
    }, 
    'Period': {
        'name': 'Q2',
        'states': 3,
        'next_nodes': ['Cheating_indicator']
    }, 
    'Time_zone': {
        'name': 'Q3',
        'states': 8,
        'next_nodes': ['Subjective_temperature']
    },  
    'Location': {
        'name': 'Q4',
        'states': 4,
        'next_nodes': ['Indoor_outdoor', 'Location_familiarity', 'Others_presence', 'Brightness']
    },  
    'Indoor_outdoor': {
        'name': 'Q5',
        'states': 2,
        'next_nodes': ['Location_nature', 'Space_size']
    },   
    'Location_nature': {
        'name': 'Q6',
        'states': 2,
        'next_nodes': ['Cheating_indicator']
    },  
    'Space_size': {
        'name': 'Q7',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    }, 
    'Shelter': {
        'name': 'Q8',
        'states': 4,
        'next_nodes': ['Cheating_indicator']
    },
    'Location_familiarity': {
        'name': 'Q9',
        'states': 5,
        'next_nodes': ['Others_influence']
    },
    'Others_presence': {
        'name': 'Q10',
        'states': 4,
        'next_nodes': ['Others_influence']
    },
    'Others_influence': {
        'name': 'Q11',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Subjective_temperature': {
        'name': 'Q12',
        'states': 5,
        'next_nodes': ['Amenity']
    },
    'Brightness': {
        'name': 'Q13',
        'states': 2,
        'next_nodes': ['Sleepiness']
    },
    'Color_Temperature': {
        'name': 'Q14',
        'states': 3,
        'next_nodes': ['Sleepiness']
    },
    'Amenity': {
        'name': 'Q15',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Weather': {
        'name': 'Q16',
        'states': 4,
        'next_nodes': ['Subjective_temperature']
    },
    'Clothing_type': {
        'name': 'Q17',
        'states': 2,
        'next_nodes': ['Cheating_indicator']
    },
    'Clothing_color': {
        'name': 'Q18',
        'states': 4,
        'next_nodes': ['Cheating_indicator']
    },
    'Exposure_degree': {
        'name': 'Q19',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Accessory': {
        'name': 'Q20',
        'states': 2,
        'next_nodes': ['Cheating_indicator']
    },
    'Health_Status': {
        'name': 'Q21',
        'states': 4,
        'next_nodes': ['Chronic_stress']
    },
    'Medicine': {
        'name': 'Q22',
        'states': 2,
        'next_nodes': ['Chronic_stress']
    },
    'Supplement': {
        'name': 'Q23',
        'states': 2,
        'next_nodes': ['Chronic_stress']
    },
    'Drinking_habits': {
        'name': 'Q24',
        'states': 4,
        'next_nodes': ['Accessory', 'Drunkenness']
    },
    'Drunkenness': {
        'name': 'Q25',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Average_sleeping_time': {
        'name': 'Q26',
        'states': 5,
        'next_nodes': ['Sleeping_time']
    },
    'Sleeping_time': {
        'name': 'Q27',
        'states': 5,
        'next_nodes': ['Sleepiness']
    },
    'Sleepiness': {
        'name': 'Q28',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Dinner': {
        'name': 'Q29',
        'states': 5,
        'next_nodes': ['Thirst_degree', 'Full_stomach']
    },
    'Thirst_degree': {
        'name': 'Q30',
        'states': 5,
        'next_nodes': ['Stress']
    },
    'Urge_to_urinate': {
        'name': 'Q31',
        'states': 3,
        'next_nodes': ['Amenity', 'Stress']
    },
    'Full_stomach': {
        'name': 'Q32',
        'states': 5,
        'next_nodes': ['Amenity', 'Stress']
    },
    'Stress': {
        'name': 'Q33',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Chronic_stress': {
        'name': 'Q34',
        'states': 5,
        'next_nodes': ['Stress']
    },
    'Socioeconomic_level': {
        'name': 'Q35',
        'states': 10,
        'next_nodes': ['Satisfaction_with_reward']
    },
    'Satisfaction_with_reward': {
        'name': 'Q36',
        'states': 5,
        'next_nodes': ['Cheating_indicator']
    },
    'Cheating_indicator': {
        'name': 'diff_coin_resp',
        'states': 40,
        'next_nodes': []
    }
}



# Create a BayesianModel object
model = BayesianNetwork()

# Define the variables, Define the dependence

for node in node_states.keys():
    model.add_node(node)    
    for next_node in node_states[node]['next_nodes']:
        # print(node, next_node)
        model.add_edge(node, next_node)

