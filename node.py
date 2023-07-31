node_states = {
    'Weekday': {
        'name': 'Q1',
        'states': 7,
        'next_nodes': ['Cheating_Indicator']
    }, 
    'Period': {
        'name': 'Q2',
        'states': 3,
        'next_nodes': ['Cheating_Indicator']
    }, 
    'Time_zone': {
        'name': 'Q3',
        'states': 8,
        'next_nodes': ['Subjective_Temperature']
    },  
    'Location': {
        'name': 'Q4',
        'states': 4,
        'next_nodes': ['Indoor_outdoor', 'location_familiarity', 'Others_presence', 'Brightness']
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
        'next_nodes': ['Cheating_Indicator']
    }, 
    'Shelter': {
        'name': 'Q8',
        'states': 4,
        'next_nodes': ['Cheating_Indicator']
    },
    'location_familiarity': {
        'name': 'Q9',
        'states': 5,
        'next_nodes': ['Others_influence']
    },
    'Others_presence': {
        'name': 'Q10',
        'states': 4,
        'next_nodes': ['Others_influence']
    },
    'Others_influence ': {
        'name': 'Q11',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Subjective_Temperature': {
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
        'next_nodes': ['Cheating_Indicator']
    },
    'Weather': {
        'name': 'Q16',
        'states': 4,
        'next_nodes': ['Subjective_Temperature']
    },
    'Clothing_type': {
        'name': 'Q17',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
    },
    'Clothing_color': {
        'name': 'Q18',
        'states': 4,
        'next_nodes': ['Cheating_Indicator']
    },
    'Clothing_color': {
        'name': 'Q18',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Exposure_degree': {
        'name': 'Q19',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
    },
    'Accessory': {
        'name': 'Q20',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
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
        'next_nodes': ['Cheating_Indicator']
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
        'next_nodes': ['Cheating_Indicator']
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
    'Urge_to_Urinate': {
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
        'next_nodes': ['Cheating_Indicator']
    },
    'Chronic_stress': {
        'name': 'Q34',
        'states': 5,
        'next_nodes': ['Stress']
    },
    'Socioeconomic_level': {
        'name': 'Q35',
        'states': 10,
        'next_nodes': ['Satisfaction_with_Reward']
    },
    'Satisfaction_with_Reward': {
        'name': 'Q36',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Cheating_Indicator': {
        'name': 'diff_coin_resp',
        'states': 40,
        'next_nodes': []
    }
}
