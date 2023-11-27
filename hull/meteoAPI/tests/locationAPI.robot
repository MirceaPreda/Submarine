*** Settings ***
Library    ../resources/locationAPIdata.py

*** Variables ***
@{locations} =    Paris    Bucharest    Berlin    Constanta
${apiResponse}
${received}
*** Test Cases ***
## Can connect
## More than one node
## Node 0 is the location requested
## Check for a number of items
Can connect to API
    [Documentation]    API can be called and 200 received
    [Tags]    Regression
    Given a list of locations
    When the API is called
    Then the API returns 200

API contains more than one node per location
    [Documentation]    Location has more than one node
    [Tags]    Regression
    Given a list of locations
    When an item has more than one node
    Then the first node is the correct one

*** Keywords ***
a list of locations
    Should Not Be Empty    ${locations}

the API is called
    ${apiResponse}=    Api Response    ${locations}
    [RETURN]    ${apiResponse}

the API returns 200
    Get Variable Value    ${apiResponse}
    Should Be Equal As Integers    ${apiResponse}    200

an item has more than one node
    ${received} =    Received As Requested    Constanta    CT
    [RETURN]    ${received}
    
the first node is the correct one
    Get Variable Value    ${received}
    Should Be True    ${received}