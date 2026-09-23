BW_COST = 0.10
COLOR_COST = 0.50
BINDING_COST = 2.00
RUSH_ORDER_COST = 0.25
STUDENT_DISCOUNT = 0.20

def get_job_details():
    # return job details
    bw_prints = int(input("Enter BW prints: "))
    color_prints = int(input("Enter color prints: "))
    binding = input("Require binding (Y/N)? ")
    job_detail = dict(bw_prints=bw_prints, color_prints=color_prints, binding=binding)
    return job_detail

def calculate_printing_costs(job_details):
    #compute printing costs
    return job_details["bw_prints"]*BW_COST + job_details["color_prints"]*COLOR_COST

def calculate_binding_cost(binding):
    if binding in "Yy":
        return BINDING_COST
    else:
        return 0

def calculate_rush_charge(rush, printing_cost):
    if rush == "Yes":
        return RUSH_ORDER_COST*printing_cost
    else:
        return 0.0
    
def calculate_total(printing_cost, binding_cost, rush_charge):
    return printing_cost+binding_cost+rush_charge
    
def calculate_discount(total, discount):
    if discount == "Yes":
        return STUDENT_DISCOUNT*total
    else:
        return 0

def main():
    job_details = get_job_details()
    #print(job_details)
    printing_cost = calculate_printing_costs(job_details)
    binding_cost = calculate_binding_cost(job_details["binding"])
    print(binding_cost)
    #for now hard code the order information
    order = dict(rush = "No", student_discount = "Yes", jobs=job_details)
    order["rush_charge"] = calculate_rush_charge(order["rush"], printing_cost)
    #print(order)
    total = calculate_total(printing_cost,binding_cost,order["rush_charge"])
    discount = calculate_discount(total,order["student_discount"])
    
    order["printing_cost"] = printing_cost
    order["binding_cost"] = binding_cost
    order["total"] = total
    order["discount"] = discount
    order["final_total"] = total - discount
    print(order)



main()
