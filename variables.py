nodes = ['Season', 'Weather', 'Comfort', 'Time_Zone', 'Subjective_Temperature', 'Indoor_Outdoor', 'Clothing_Color', 'Space_Size', 'Experimental_Location', 'Influence_by_Third_Party', 'Presence_of_Obstacles', 'Color_Temperature', 'Subjective_Brightness', 'Satiety_Level', 'Sleepiness', 'Satisfaction_with_Reward', 'Day_of_Week', 'Before_After_Meals', 'Previous_Night_Sleep_Duration', 'In_Season', 'Type_of_Clothing', 'Health_Status', 'Urge_to_Urinate', 'Subjective_Stress_Level', 'Medication_Use', 'Degree_of_Thirst', 'Long-Term_Stress_Level', 'Supplement_Use', 'Cheating_Indicator', 'Term_Stress_Level']


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
        'next_nodes': ['Cheating_Indicator']
    },  
    'Location': {
        'name': 'Q4',
        'states': 4,
        'next_nodes': ['Cheating_Indicator']
    },  
    'Indoor_outdoor': {
        'name': 'Q5',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
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
        'next_nodes': ['Cheating_Indicator']
    },
    'Others_presence': {
        'name': 'Q10',
        'states': 4,
        'next_nodes': ['Cheating_Indicator']
    },
    'Others_influence ': {
        'name': 'Q11',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Subjective_Temperature': {
        'name': 'Q12',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Brightness': {
        'name': 'Q13',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
    },
    'Color_Temperature': {
        'name': 'Q14',
        'states': 3,
        'next_nodes': ['Cheating_Indicator']
    },
    'Amenity': {
        'name': 'Q15',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Weather': {
        'name': 'Q16',
        'states': 4,
        'next_nodes': ['Cheating_Indicator']
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
        'next_nodes': ['Cheating_Indicator']
    },
    'Medicine': {
        'name': 'Q22',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
    },
    'Supplement': {
        'name': 'Q23',
        'states': 2,
        'next_nodes': ['Cheating_Indicator']
    },
    'Drinking_habits': {
        'name': 'Q24',
        'states': 4,
        'next_nodes': ['Cheating_Indicator']
    },
    'Drunkenness': {
        'name': 'Q25',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Average_sleeping_time': {
        'name': 'Q26',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Sleeping_time': {
        'name': 'Q27',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Sleepiness': {
        'name': 'Q28',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Dinner': {
        'name': 'Q29',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Thirst_degree': {
        'name': 'Q30',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Urge_to_Urinate': {
        'name': 'Q31',
        'states': 3,
        'next_nodes': ['Cheating_Indicator']
    },
    'Full_stomach': {
        'name': 'Q32',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Stress': {
        'name': 'Q33',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Chronic_stress': {
        'name': 'Q34',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Socioeconomic_level': {
        'name': 'Q35',
        'states': 10,
        'next_nodes': ['Cheating_Indicator']
    },
    'Satisfaction_with_Reward': {
        'name': 'Q36',
        'states': 5,
        'next_nodes': ['Cheating_Indicator']
    },
    'Cheating_Indicator': {
        'name': 'diff_coin_resp',
        'states': 40,
        'next_nodes': ['Cheating_Indicator']
    }
}
