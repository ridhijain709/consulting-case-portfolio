import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import numpy as np

def calculate_swiggy_ebitda(orders_per_day, aov=450, margin_pct=0.15, delivery_cost=40, fixed_cost=300000):
    '''Calculate monthly EBITDA for a Swiggy Instamart dark store.'''
    days_in_month = 30
    monthly_orders = orders_per_day * days_in_month
    revenue = monthly_orders * aov * margin_pct
    variable_costs = monthly_orders * delivery_cost
    ebitda = revenue - variable_costs - fixed_cost
    return ebitda

# Monte Carlo Simulation
np.random.seed(42)
simulated_orders = np.random.normal(loc=320, scale=30, size=1000)
results = [calculate_swiggy_ebitda(order) for order in simulated_orders]
break_even_prob = np.mean(np.array(results) > 0) * 100

print(f'Swiggy Dark Store Unit Economics')
print(f'EBITDA at 320 orders/day: ₹{calculate_swiggy_ebitda(320):,.0f}')
print(f'Monte Carlo Break-even Probability: {break_even_prob:.1f}%')
