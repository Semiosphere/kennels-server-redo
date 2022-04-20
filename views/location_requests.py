LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    #variable to hold the found location, if it exists
    requested_location = None
    #for loop to iterate the LOCATIONS array
    for location in LOCATIONS:
        #if the submitted id has a match in the array,
        if location["id"] == id:
            #store the corresponding object in the location var
            requested_location = location
    return requested_location