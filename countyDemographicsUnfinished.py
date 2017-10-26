import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return first


def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    highestYoung = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highestYoung:
            highestYoung = c["Age"]["Percent Under 18 Years"]
            state = c["County"]
            county = c["State"]
    return [str(county),str(state)]


def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highestYoung = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highestYoung:
            highestYoung = c["Age"]["Percent Under 18 Years"]
    return highestYoung


def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    highestYoung = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highestYoung:
            highestYoung = c["Age"]["Percent Under 18 Years"]
            state = c["County"]
            county = c["State"]
    return [str(county),str(state),str(highestYoung)]


def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    #Find the state in the dictionary with the most counties
    #Return the state with the most counties
    states = {str(counties[0]["State"]) : [str(counties[0]["County"])]}
    # print states

    ## dictionarying states and counties
    for c in counties:
        # print c["State"], c["County"]
        state = str(c["State"])
        county = str(c["County"])

        if state in states:
            states[state].append(county)
        else:
            states[state] = [county]
    
    # finding state w/ most counties
    mostCountiesState = ""
    numC = 0
    for state, counties in states.iteritems():
        if numC < len(counties):
            mostCountiesState = state
            numC = len(counties)
    return [mostCountiesState, numC]



def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""

if __name__ == '__main__':
    main()
