nodes = ['Season', 'Weather', 'Comfort', 'Time_Zone', 'Subjective_Temperature', 'Indoor_Outdoor', 'Clothing_Color', 'Space_Size', 'Experimental_Location', 'Influence_by_Third_Party', 'Presence_of_Obstacles', 'Color_Temperature', 'Subjective_Brightness', 'Satiety_Level', 'Sleepiness', 'Satisfaction_with_Reward', 'Day_of_Week', 'Before_After_Meals', 'Previous_Night_Sleep_Duration', 'In_Season', 'Type_of_Clothing', 'Health_Status', 'Urge_to_Urinate', 'Subjective_Stress_Level', 'Medication_Use', 'Degree_of_Thirst', 'Long-Term_Stress_Level', 'Supplement_Use', 'Cheating_Indicator', 'Term_Stress_Level']


<<<<<<< HEAD
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
=======
# node_states = {
#     'Season': 2, 
#     'Weather': 4, 
#     'Comfort': 7, 
#     'Time_Zone': 3, 
#     'Subjective_Temperature': 7, 
#     'Indoor_Outdoor': 2, 
#     'Clothing_Color': 7, 
#     'Space_Size': 7, 
#     'Experimental_Location': 7, 
#     'Influence_by_Third_Party': 7, 
#     'Presence_of_Obstacles': 2, 
#     'Color_Temperature': 3, 
#     'Subjective_Brightness': 7, 
#     'Satiety_Level': 7, 
#     'Sleepiness': 7, 
#     'Satisfaction_with_Reward': 7, 
#     'Day_of_Week': 5, 
#     'Before_After_Meals': 5, 
#     'Previous_Night_Sleep_Duration': 4, 
#     'In_Season': 3, 
#     'Type_of_Clothing': 2, 
#     'Health_Status': 3, 
#     'Urge_to_Urinate': 7, 
#     'Subjective_Stress_Level': 7, 
#     'Medication_Use': 2, 
#     'Degree_of_Thirst': 7, 
#     'Long-Term_Stress_Level': 7, 
#     'Supplement_Use': 2,
#     'Cheating_Indicator': 10
#     }

node_states = {
    'Season': 2, 
    'Weather': 2, 
    'Comfort': 2, 
    'Time_Zone': 2, 
    'Subjective_Temperature': 2, 
    'Indoor_Outdoor': 2, 
    'Clothing_Color': 2, 
    'Space_Size': 2, 
    'Experimental_Location': 2, 
    'Influence_by_Third_Party': 2, 
    'Presence_of_Obstacles': 2, 
    'Color_Temperature': 2, 
    'Subjective_Brightness': 2, 
    'Satiety_Level': 2, 
    'Sleepiness': 2, 
    'Satisfaction_with_Reward': 2, 
    'Day_of_Week': 2, 
    'Before_After_Meals': 2, 
    'Previous_Night_Sleep_Duration': 2, 
    'In_Season': 2, 
    'Type_of_Clothing': 2, 
    'Health_Status': 2, 
    'Urge_to_Urinate': 2, 
    'Subjective_Stress_Level': 2, 
    'Medication_Use': 2, 
    'Degree_of_Thirst': 2, 
    'Long-Term_Stress_Level': 2, 
    'Supplement_Use': 2,
    'Cheating_Indicator': 5
    }
>>>>>>> 7d67a96702289f5f12da3682697068e22ada4e16
